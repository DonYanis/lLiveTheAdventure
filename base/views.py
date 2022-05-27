import uuid
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import FeedBack, Notification, User,Trip,TripType,Blog,TripImage,Profile
from .forms import ChangeAvatarForm, ChangeEmailForm, ChangeNameForm, ChangePhoneForm, ChangeUsernameForm, FeedbackForm, LoginForm, UserForm,CreateUserForm,TripForm,BlogForm,StatusForm
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def logoutuser(request):
    logout(request)
    return redirect('home')

#main page
def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    trips=Trip.objects.filter(
        Q(type__code__icontains=q)
    )
    
    clients=User.objects.filter(is_client=True)
    blogs=Blog.objects.all()
    tripcount=trips.count()
    types=TripType.objects.all()
    feedbacks=FeedBack.objects.all()
    
    notificated=False
    if request.user.is_authenticated:
        notifications=Notification.objects.filter(user=request.user)
        if len(notifications)>0:
            notificated=True
    else:
        notifications=[]
    
    #load forms:
    tripform=TripForm()
    blogform=BlogForm()
    createuser=CreateUserForm()
    loginform=LoginForm()
    feedform=FeedbackForm()
    
    if request.method=='POST':

        if 'login_user_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
            except:
                messages.error(request,'Votre email est incorrecte')
                return redirect('message_page')
            
            
            profile_obj = Profile.objects.filter(user = user ).first()
            if profile_obj is not None:
                if not profile_obj.is_verified:
                    messages.success(request, 'Votre Compte n est pas encore vérifié')
                    return redirect('message_page')
            
            user = authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Votre mot de passe est incorrecte , veuillez réessayer ou cliquer sur mot de passe oublié dans la fenêtre de Login')
                return redirect('message_page')
    #------------------------------------------------------------------
        elif 'create_user_form' in request.POST:
            
            name=request.POST.get('name')
            phonenumber=request.POST.get('number')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            if User.objects.filter(email=email).exists():
                messages.error(request,'Addresse mail existe déja ')
                return redirect('message_page')

            if User.objects.filter(username=username).exists():   
                messages.error(request,'username existe déja ')
                return redirect('message_page')

            if len(password)<4:
                messages.error(request,'mot de passe est très court ')
                return redirect('message_page')

            try:    
                user = User.objects.create(
                    name=name,
                    phonenumber=phonenumber,
                    email=email,
                    username=username,
                ) 
                user.set_password(password)
                user.username = user.username.lower()
                user.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
                profile_obj.save()
                current_site = get_current_site(request)
                print(current_site.domain)
                domain='http://127.0.0.1:8000/'
                send_mail_after_registration(user.username,email , auth_token,domain)
                return redirect('/token')

            except Exception as e:
                print(e)
        #-------------------------------------------
        elif 'trip_form' in request.POST:
            type_name=request.POST.get('categorie')
            trip=Trip.objects.create(
                type=TripType.objects.get(name=type_name),
                name=request.POST.get('NomSortie'),
                description=request.POST.get('description'),
                level=request.POST.get('niveau'),
                blog_link=request.POST.get('lienBlog'),
                depart=request.POST.get('depart'),
                retour=request.POST.get('retour'),
                depart_place=request.POST.get('pointRV'),
                total_places=request.POST.get('nombrePlaces'),
                price=request.POST.get('prix'),
                program=request.POST.get('programme'),
                prevoir=request.POST.get('prevoir'),
                prixComprend=request.POST.get('prixComprend'),   
            )

            month=trip.depart.strftime('%m')
            trip.month_name=getMonth(month)
            trip.save()

            album=request.FILES.getlist('insererPhotosSortie') 
            for image in album:
                TripImage.objects.create(
                    avatar=image,
                    trip=trip,
                ) 
            return redirect('home')

        elif 'edit_blog' in request.POST:
        #create blog:
            Blog.objects.create(
                name=request.POST.get('nomBlog'),
                main_section=request.POST.get('blogSection1'),
                section2=request.POST.get('blogSection2'),
                section2_title=request.POST.get('titresection2'),
                section3=request.POST.get('blogSection3'),
                section3_title=request.POST.get('titresection3'),
                section4=request.POST.get('blogSection4'),
                section4_title=request.POST.get('titresection4'),
                section5=request.POST.get('blogSection5'),
                section5_title=request.POST.get('titresection5'),
                main_image=request.FILES.get('insererPhotoPrincipale'),
                section2_image=request.FILES.get('insererPhotosSection2'),
                section3_image=request.FILES.get('insererPhotosSection3'),
                section4_image=request.FILES.get('insererPhotosSection4'),
                section5_image=request.FILES.get('insererPhotosSection5'),
            )
              
            
            return redirect('home')
        elif 'feed_form' in request.POST:

            for i in range(20):
                name='rating'+str(i+1)
                rate=request.POST.get(name)
                if rate is not None:
                    break
            FeedBack.objects.create(
                user=request.user,
                body=request.POST.get('comment'),
                rate=int(rate)//2
            )
            return redirect('home')

    context={'types':types,'trips':trips,'tripcount':tripcount,
             'clients':clients,'blogs':blogs,'tripform':tripform,
             'blogform':blogform,'loginform':loginform,'createuser':createuser,
             'notificated':notificated,'feedbacks':feedbacks,'page':'home',
             'feedform':feedform,'range':range(5)}

    return render(request,'home.html',context)

#admin_trip_page
@login_required(login_url='login')
def tripPage(request,pk,sk):
    trip=Trip.objects.get(id=pk)
    waitinglist=trip.waitinglist.all()
    participants=trip.participants.all()
    types=TripType.objects.all()
    tripform=TripForm()
    page='trip'
    try:
        currentuser=User.objects.get(id=sk)
    except:
        if len(waitinglist)>0:
            currentuser=waitinglist[0]
        elif len(participants)>0:
            currentuser=participants[0]
        else :
            currentuser=None
    currentuser_accepted=False
    if currentuser is not None:
        if currentuser in participants :
            currentuser_accepted=True
            
    
    if request.method=='POST':
        if 'trip_form' in request.POST:
            type_name=request.POST.get('categorie')
            trip=Trip.objects.get(id=pk)
            trip.type=TripType.objects.get(name=type_name)
            trip.name=request.POST.get('NomSortie')
            trip.description=request.POST.get('description')
            trip.level=request.POST.get('niveau')
            trip.blog_link=request.POST.get('lienBlog')
            trip.depart=request.POST.get('depart')
            trip.retour=request.POST.get('retour')
            trip.depart_place=request.POST.get('pointRV')
            trip.total_places=request.POST.get('nombrePlaces')
            trip.price=request.POST.get('prix')
            trip.program=request.POST.get('programme')
            trip.prevoir=request.POST.get('prevoir')
            trip.prixComprend=request.POST.get('prixComprend')   
            trip.month_name=getMonth(trip.depart.strftime('%m'))
            trip.save()
            album=request.FILES.getlist('insererPhotosSortie') 
            for image in album:
                TripImage.objects.create(
                    avatar=image,
                    trip=trip,
                ) 
            return redirect('home')
        else:
            currentuser.status=request.POST.get('statut-sortie')
            currentuser.points=request.POST.get('points-sortie')
            currentuser.save()
            Notification.objects.create(
                name='Statut mis à jour',
                body=f'Vous etes devenus un utilisateur {currentuser.status}, avec {currentuser.points} points ',
                user=currentuser
            )
            return redirect('tripPage',pk=trip.id,sk=currentuser.id)

    context={'trip':trip,'waitinglist':waitinglist,
            'participants':participants,'page':page,
            'currentuser':currentuser,'currentuser_accepted':currentuser_accepted,
            'types':types,'tripform':tripform,}
    return render(request,'trip.html',context)

#user_profile_page
@login_required(login_url='login')
def userProfile(request):
    page='profile'
    user=request.user
    edit_name=ChangeNameForm
    edit_phone=ChangePhoneForm
    edit_username=ChangeUsernameForm
    edit_email=ChangeEmailForm
    edit_avatar=ChangeAvatarForm

    if request.method=='POST':
       
        if 'change_name_form' in request.POST:
            
            name=request.POST.get('name')
            if len(name)>0:
                user.name=name
                user.save()
            return redirect('userprofile')

        elif 'change_phone_form' in request.POST:
            phone=request.POST.get('phone')
            user.phonenumber=phone
            user.save()
            return redirect('userprofile')
        elif 'change_username_form' in request.POST:
            username=request.POST.get('username')
            if User.objects.filter(username=username).exists() or len(username)<1:
                pass
            else:
                user.username=username
                user.save()
            return redirect('userprofile')
        elif 'change_email_form' in request.POST:
            email=request.POST.get('email')
            user.email=email
            user.save()
            return redirect('userprofile')
        elif 'change_avatar_form' in request.POST:
            user.avatar=request.POST.get('upload-picture')
            user.has_avatar=True
            user.save()
            return redirect('userprofile')
        elif 'feed_form' in request.POST:
            for i in range(20):
                name='rating'+str(i+1)
                rate=request.POST.get(name)
                if rate is not None:
                    break
            FeedBack.objects.create(
                user=request.user,
                body=request.POST.get('comment'),
                rate=int(rate)//2
            )
            return redirect('userprofile')
            

    notificated=False
    notifications=Notification.objects.filter(user=request.user)
    if len(notifications)>0:
        notificated=True
    feedform=FeedbackForm()
    context={'page':page,'nameform':edit_name,'emailform':edit_email,
                'phoneform':edit_phone,'usernameform':edit_username,
                'feedform':feedform,'notificated':notificated,
                'avatarform':edit_avatar}
    return render(request,'profile.html',context)


#admin_delete_trip
@login_required(login_url='login')
def deleteTrip(request,pk):
    trip= Trip.objects.get(id=pk)

    trip.delete()
    return redirect('home')

#user_join_trip
@login_required(login_url='login')
def joinTrip(request,pk):
    trip= Trip.objects.get(id=pk)
    trip.waitinglist.add(request.user)
    return redirect('home')

#user_blogs_page
def blogPage(request):
    blogs=Blog.objects.all()
    group=[]
    groups=[]
    i=0
    for blog in blogs:
        if i<3 :
            group.append(blog)
            i+=1
        else:
            i=0
            groups.append(group)
            group=[]
    if i > 0:
        groups.append(group)
    
    createuser=CreateUserForm()
    loginform=LoginForm()
    feedform=FeedbackForm()
    if request.method=='POST':
        
        if 'login_user_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
                
            except:
                messages.error(request,'Votre email est incorrecte')
                return redirect('message_page')
            
            
            profile_obj = Profile.objects.filter(user = user ).first()
            if profile_obj is not None:
                if not profile_obj.is_verified:
                    messages.success(request, 'Votre Compte n est pas encore vérifié')
                    return redirect('message_page')
            
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Votre mot de passe est incorrecte , veuillez réessayer ou cliquer sur mot de passe oublié dans la fenêtre de Login')
                return redirect('message_page')
    #------------------------------------------------------------------
        elif 'create_user_form' in request.POST:
            
            name=request.POST.get('name')
            phonenumber=request.POST.get('number')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            if User.objects.filter(email=email).exists():
                messages.error(request,'Addresse mail existe déja ')
                return redirect('message_page')

            if User.objects.filter(username=username).exists():   
                messages.error(request,'username existe déja ')
                return redirect('message_page')

            if len(password)<4:
                messages.error(request,'mot de passe est très court ')
                return redirect('message_page')

            try:    
                user = User.objects.create(
                    name=name,
                    phonenumber=phonenumber,
                    email=email,
                    username=username,
                ) 
                user.set_password(password)
                user.username = user.username.lower()
                user.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
                profile_obj.save()
                current_site = get_current_site(request)
                print(current_site.domain)
                domain='http://127.0.0.1:8000/'
                send_mail_after_registration(user.username,email , auth_token,domain)
                return redirect('/token')

            except Exception as e:
                print(e)
        elif 'feed_form' in request.POST:

            for i in range(20):
                name='rating'+str(i+1)
                rate=request.POST.get(name)
                if rate is not None:
                    break
            FeedBack.objects.create(
                user=request.user,
                body=request.POST.get('comment'),
                rate=int(rate)//2
            )
            return redirect('home')
    
    notificated=False
    if request.user.is_authenticated:
        notifications=Notification.objects.filter(user=request.user)
        if len(notifications)>0:
            notificated=True
    page='blogs'
    context={'groups':groups,
            'loginform':loginform,'createuser':createuser,
            'notificated':notificated,'page':page, 'feedform':feedform}
    return render(request,'blogs.html',context)

#user_blog_page
def blog(request,pk):
    blog=Blog.objects.get(id=pk)
    sblogs=Blog.objects.all()
    
    page='bloguserpage'
    createuser=CreateUserForm()
    loginform=LoginForm()
    feedform=FeedbackForm()
    if request.method=='POST':
        
        if 'login_user_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
                
            except:
                messages.error(request,'Votre email est incorrecte')
                return redirect('message_page')
            
            
            profile_obj = Profile.objects.filter(user = user ).first()
            if profile_obj is not None:
                if not profile_obj.is_verified:
                    messages.success(request, 'Votre Compte n est pas encore vérifié')
                    return redirect('message_page')
            
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Votre mot de passe est incorrecte , veuillez réessayer ou cliquer sur mot de passe oublié dans la fenêtre de Login')
                return redirect('message_page')
    #------------------------------------------------------------------
        elif 'create_user_form' in request.POST:
            
            name=request.POST.get('name')
            phonenumber=request.POST.get('number')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            if User.objects.filter(email=email).exists():
                messages.error(request,'Addresse mail existe déja ')
                return redirect('message_page')

            if User.objects.filter(username=username).exists():   
                messages.error(request,'username existe déja ')
                return redirect('message_page')

            if len(password)<4:
                messages.error(request,'mot de passe est très court ')
                return redirect('message_page')

            try:    
                user = User.objects.create(
                    name=name,
                    phonenumber=phonenumber,
                    email=email,
                    username=username,
                ) 
                user.set_password(password)
                user.username = user.username.lower()
                user.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
                profile_obj.save()
                current_site = get_current_site(request)
                print(current_site.domain)
                domain='http://127.0.0.1:8000/'
                send_mail_after_registration(user.username,email , auth_token,domain)
                return redirect('/token')

            except Exception as e:
                print(e)
        elif 'feed_form' in request.POST:

            for i in range(20):
                name='rating'+str(i+1)
                rate=request.POST.get(name)
                if rate is not None:
                    break
            FeedBack.objects.create(
                user=request.user,
                body=request.POST.get('comment'),
                rate=int(rate)//2
            )
            return redirect('home')
    
    notificated=False
    if request.user.is_authenticated:
        notifications=Notification.objects.filter(user=request.user)
        if len(notifications)>0:
            notificated=True
    context={'blog':blog,'sblogs':sblogs,'page':page,'loginform':loginform,'createuser':createuser,
            'notificated':notificated, 'feedform':feedform}
    
    return render(request,'blog.html',context)

#admin_blog_page
@login_required(login_url='login')
def tripBlog(request,pk):
    blog=Blog.objects.get(id=pk)
    page='blog'
    context={'blog':blog,'page':page}
    if request.method=='POST':
        blog.name=request.POST.get('nomBlog')
        blog.main_section=request.POST.get('blogSection1')
        blog.section2=request.POST.get('blogSection2')
        blog.section2_title=request.POST.get('titresection2')
        blog.section3=request.POST.get('blogSection3')
        blog.section3_title=request.POST.get('titresection3')
        blog.section4=request.POST.get('blogSection4')
        blog.section4_title=request.POST.get('titresection4')
        blog.section5=request.POST.get('blogSection5')
        blog.section5_title=request.POST.get('titresection5')
        blog.main_image=request.FILES.get('insererPhotoPrincipale')
        blog.section2_image=request.FILES.get('insererPhotosSection2')
        blog.section3_image=request.FILES.get('insererPhotosSection3')
        blog.section4_image=request.FILES.get('insererPhotosSection4')
        blog.section5_image=request.FILES.get('insererPhotosSection5')
        
        blog.save()
            
        return redirect('home')
    return render(request,'admin_blog.html',context)

#admin_delete_blog
@login_required(login_url='login')
def deleteBlog(request,pk):
    blog= Blog.objects.get(id=pk)

    blog.delete()
    return redirect('home')


#admin_accepts_reservation
@login_required(login_url='login')
def acceptReservation(request,pk,sk):
    trip= Trip.objects.get(id=pk)
    user= User.objects.get(id=sk)
    trip.waitinglist.remove(user)
    trip.participants.add(user)
    Notification.objects.create(
        name=trip.name,
        body=f'Félicitations: Vous étiez accépté pour rejoindre cette sortie le {trip.depart} ',
        user=user
    )

    try :
        subject = trip.name
        message = f'Bonjour {user.username} vous etes accetpés pour la sortie de {trip.name}, rendez-vous  {trip.depart}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message , email_from ,recipient_list )
    except :
        pass
    user.save()
    return redirect('tripPage',pk=trip.id,sk=user.id)

#admin_refuses_reservation
@login_required(login_url='login')
def refuseReservation(request,pk,sk):
    trip= Trip.objects.get(id=pk)
    user= User.objects.get(id=sk)

    trip.waitinglist.remove(user)
    Notification.objects.create(
        name=trip.name,
        body=f'Désolé: Votre demande de réservation a été refusée ',
        user=user
    )
    
    user.save()
    return redirect('tripPage',pk=trip.id,sk=0)

#admin_delete_participant_from_list
@login_required(login_url='login')
def deleteReservation(request,pk,sk):
    trip= Trip.objects.get(id=pk)
    user= User.objects.get(id=sk)

    trip.participants.remove(user)

    Notification.objects.create(
            name=trip.name,
            body=f'Désolé : Vous etes retirés de la liste des participants ',
            user=user 
        )
    return redirect('tripPage',pk=trip.id)

#email_cheked_message
def success(request):
    createuser=CreateUserForm()
    loginform=LoginForm()
    if request.method=='POST':
        
        if 'login_user_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
                
            except:
                messages.error(request,'Votre email est incorrecte')
                return redirect('message_page')
            
            
            profile_obj = Profile.objects.filter(user = user ).first()
            if profile_obj is not None:
                if not profile_obj.is_verified:
                    messages.success(request, 'Votre Compte n est pas encore vérifié')
                    return redirect('message_page')
            
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Votre mot de passe est incorrecte , veuillez réessayer ou cliquer sur mot de passe oublié dans la fenêtre de Login')
                return redirect('message_page')
    #------------------------------------------------------------------
        elif 'create_user_form' in request.POST:
            
            name=request.POST.get('name')
            phonenumber=request.POST.get('number')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            if User.objects.filter(email=email).exists():
                messages.error(request,'Addresse mail existe déja ')
                return redirect('message_page')

            if User.objects.filter(username=username).exists():   
                messages.error(request,'username existe déja ')
                return redirect('message_page')

            if len(password)<4:
                messages.error(request,'mot de passe est très court ')
                return redirect('message_page')

            try:    
                user = User.objects.create(
                    name=name,
                    phonenumber=phonenumber,
                    email=email,
                    username=username,
                ) 
                user.set_password(password)
                user.username = user.username.lower()
                user.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
                profile_obj.save()
                current_site = get_current_site(request)
                print(current_site.domain)
                domain='http://127.0.0.1:8000/'
                send_mail_after_registration(user.username,email , auth_token,domain)
                return redirect('/token')

            except Exception as e:
                print(e)
        
   
    context={'loginform':loginform,'createuser':createuser}
    
    return render(request , 'success.html',context)

#email_verification_send
def token_send(request):
    createuser=CreateUserForm()
    loginform=LoginForm()
    if request.method=='POST':
        
        if 'login_user_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
                
            except:
                messages.error(request,'Votre email est incorrecte')
                return redirect('message_page')
            
            
            profile_obj = Profile.objects.filter(user = user ).first()
            if profile_obj is not None:
                if not profile_obj.is_verified:
                    messages.success(request, 'Votre Compte n est pas encore vérifié')
                    return redirect('message_page')
            
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Votre mot de passe est incorrecte , veuillez réessayer ou cliquer sur mot de passe oublié dans la fenêtre de Login')
                return redirect('message_page')
    #------------------------------------------------------------------
        elif 'create_user_form' in request.POST:
            
            name=request.POST.get('name')
            phonenumber=request.POST.get('number')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            if User.objects.filter(email=email).exists():
                messages.error(request,'Addresse mail existe déja ')
                return redirect('message_page')

            if User.objects.filter(username=username).exists():   
                messages.error(request,'username existe déja ')
                return redirect('message_page')

            if len(password)<4:
                messages.error(request,'mot de passe est très court ')
                return redirect('message_page')

            try:    
                user = User.objects.create(
                    name=name,
                    phonenumber=phonenumber,
                    email=email,
                    username=username,
                ) 
                user.set_password(password)
                user.username = user.username.lower()
                user.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
                profile_obj.save()
                current_site = get_current_site(request)
                print(current_site.domain)
                domain='http://127.0.0.1:8000/'
                send_mail_after_registration(user.username,email , auth_token,domain)
                return redirect('/token')

            except Exception as e:
                print(e)
        
   
    context={'loginform':loginform,'createuser':createuser}
    return render(request , 'token_send.html', context)


#verify_email
def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('message_page')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Votre compte a été vérifié avec succès, vous pouvez connecter à votre compte ')
            return redirect('message_page')
        else:
            return redirect('error')
    except Exception as e:
        print(e)
        return redirect('home')

def error_page(request):
    return  render(request , 'error.html')


def send_mail_after_registration(username,email , token,domain):
    
    subject = 'Vérification de votre compte'
    message = f'Bonjour {username} cliquez sur ce lien pour valider votre inscription sur Live The Adventure, {domain}/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

def messagesPage(request):
    createuser=CreateUserForm()
    loginform=LoginForm()
    if request.method=='POST':
        
        if 'login_user_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
                
            except:
                messages.error(request,'Votre email est incorrecte')
                return redirect('message_page')
            
            
            profile_obj = Profile.objects.filter(user = user ).first()
            if profile_obj is not None:
                if not profile_obj.is_verified:
                    messages.success(request, 'Votre Compte n est pas encore vérifié')
                    return redirect('message_page')
            
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Votre mot de passe est incorrecte , veuillez réessayer ou cliquer sur mot de passe oublié dans la fenêtre de Login')
                return redirect('message_page')
    #------------------------------------------------------------------
        elif 'create_user_form' in request.POST:
            
            name=request.POST.get('name')
            phonenumber=request.POST.get('number')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            if User.objects.filter(email=email).exists():
                messages.error(request,'Addresse mail existe déja ')
                return redirect('message_page')

            if User.objects.filter(username=username).exists():   
                messages.error(request,'username existe déja ')
                return redirect('message_page')

            if len(password)<4:
                messages.error(request,'mot de passe est très court ')
                return redirect('message_page')

            try:    
                user = User.objects.create(
                    name=name,
                    phonenumber=phonenumber,
                    email=email,
                    username=username,
                ) 
                user.set_password(password)
                user.username = user.username.lower()
                user.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
                profile_obj.save()
                current_site = get_current_site(request)
                print(current_site.domain)
                domain='http://127.0.0.1:8000/'
                send_mail_after_registration(user.username,email , auth_token,domain)
                return redirect('/token')

            except Exception as e:
                print(e)
        elif 'feed_form' in request.POST:

            for i in range(20):
                name='rating'+str(i+1)
                rate=request.POST.get(name)
                if rate is not None:
                    break
            FeedBack.objects.create(
                user=request.user,
                body=request.POST.get('comment'),
                rate=int(rate)//2
            )
            return redirect('home')
    feedform=FeedbackForm()
    context={'loginform':loginform,'createuser':createuser,'feedform':feedform}
    return render(request,'messages.html',context)



def password_reset_request(request):

    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            email = password_reset_form.cleaned_data['email']
            user = User.objects.get(email=email)
            if user is not None :

                subject='Password Reset Requested'
                current_site = get_current_site(request)
                token=default_token_generator.make_token(user)
                uid=urlsafe_base64_encode(force_bytes(user.pk))
                message = f'Hi {user.username} Please click on the link to reset  your password in Live The Adventure Website, {current_site.domain}/reset/{uid}/{token}/'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                
                try:
                    send_mail(subject, message , email_from ,recipient_list )
                except BadHeaderError:

                    return HttpResponse('Invalid header found.')
                    
                messages.success(request, 'Vérifier votre boite mail')
                return redirect ('message_page')
            messages.error(request, 'Email invalide !')
    password_reset_form = PasswordResetForm()
    return render(request, 'password_reset.html',{'password_reset_form':password_reset_form})

#admin_client_list_page
def clientList(request,pk):

    clients=User.objects.filter(is_client=True)
    try:
        user=User.objects.get(id=pk)
    except:
        user=clients[0]
    page='clients'

    if request.method=='POST':
        user.status=request.POST.get('statut-liste')
        user.points=request.POST.get('points-liste')
        user.save()
        Notification.objects.create(
            name='Status mis à jour',
            body=f'Votre status a été mis à jour : membre {user.status} avec {user.points} points',
            user=user
        )
        return redirect('clientlist',pk=user.id)
    context={'currentuser':user,'clients':clients,'page':page}
    return render(request,'clientList.html',context)

#close_inscriptions_in_a_trip
def closeInscrisptions(request,pk):
    trip=Trip.objects.get(id=pk)
    trip.is_closed=True
    trip.save()
    users=trip.waitinglist.all()
    for user in users:
        Notification.objects.create(
            user=user,
            name=trip.name,
            body=f'Inscriptions sont fermées'
        )
    
    return redirect('tripPage',pk=trip.id,sk=0)

#admin_feedback_page
def Feedbacks(request):

    feedbacks=FeedBack.objects.all()
    page='feedbackpage'
    context={'feedbacks':feedbacks,'page':page,'range':range(5)}
    return render(request,'feedbackList.html',context)

#admin_accept_feed
def AcceptFeed(request,pk):
    feed=FeedBack.objects.get(id=pk)
    feed.is_accepted=True
    feed.save()
    Notification.objects.create(
            user=feed.user,
            name='Feedback',
            body=f'Votre feedback a été accepté'
        )
    return redirect('feedbackpage')

def DeleteFeed(request,pk):
    feed=FeedBack.objects.get(id=pk)
    feed.delete()
    return redirect('feedbackpage')

#user_calendar_page
def calendar(request):

    page='calendar'
    notificated=False
    if request.user.is_authenticated:
        notifications=Notification.objects.filter(user=request.user)
        if len(notifications)>0:
            notificated=True

    trips=Trip.objects.all()
    months=[]
    monthnames=[]
    for trip in trips:
        month=trip.depart.strftime('%m')
        if not month in months :
            months.append(month)
    months.sort()
    if len(months) > 0 :
        firstmonth=getMonth(months[0])
        for month in months:
            if firstmonth != getMonth(month) :
                monthnames.append(getMonth(month))

    createuser=CreateUserForm()
    loginform=LoginForm()
    feedform=FeedbackForm()
    if request.method=='POST':
        
        if 'login_user_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
                
            except:
                messages.error(request,'Votre email est incorrecte')
                return redirect('message_page')
            
            
            profile_obj = Profile.objects.filter(user = user ).first()
            if profile_obj is not None:
                if not profile_obj.is_verified:
                    messages.success(request, 'Votre Compte n est pas encore vérifié')
                    return redirect('message_page')
            
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Votre mot de passe est incorrecte , veuillez réessayer ou cliquer sur mot de passe oublié dans la fenêtre de Login')
                return redirect('message_page')
    #------------------------------------------------------------------
        elif 'create_user_form' in request.POST:
            
            name=request.POST.get('name')
            phonenumber=request.POST.get('number')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            if User.objects.filter(email=email).exists():
                messages.error(request,'Addresse mail existe déja ')
                return redirect('message_page')

            if User.objects.filter(username=username).exists():   
                messages.error(request,'username existe déja ')
                return redirect('message_page')

            if len(password)<4:
                messages.error(request,'mot de passe est très court ')
                return redirect('message_page')

            try:    
                user = User.objects.create(
                    name=name,
                    phonenumber=phonenumber,
                    email=email,
                    username=username,
                ) 
                user.set_password(password)
                user.username = user.username.lower()
                user.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
                profile_obj.save()
                current_site = get_current_site(request)
                print(current_site.domain)
                domain='http://127.0.0.1:8000/'
                send_mail_after_registration(user.username,email , auth_token,domain)
                return redirect('/token')

            except Exception as e:
                print(e)
        elif 'feed_form' in request.POST:

            for i in range(20):
                name='rating'+str(i+1)
                rate=request.POST.get(name)
                if rate is not None:
                    break
            FeedBack.objects.create(
                user=request.user,
                body=request.POST.get('comment'),
                rate=int(rate)//2
            )
            return redirect('home')
    
    
    context={'page':page,'loginform':loginform,'createuser':createuser,
            'notificated':notificated, 'feedform':feedform,'months':monthnames,
            'firstmonth':firstmonth,'trips':trips}
    
    return render(request,'calendar.html',context)

def deleteNotif(request,pk):
    notif=Notification.objects.get(id=pk)
    notif.delete()
    return redirect('home')

def getMonth(number):

    months={
        '01':'Janvier',
        '02':'Février',
        '03':'Mars',
        '04':'Avril',
        '05':'Mai',
        '06':'Juin',
        '07':'Juillet',
        '08':'Aout',
        '09':'Septembre',
        '10':'Octobre',
        '11':'Novembre',
        '12':'Décembre',
                        }
    return months[number]


def homeTrip(request,pk):

    currenttrip=Trip.objects.get(id=pk)
    trips2=[currenttrip]
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    trips=Trip.objects.filter(
        Q(type__code__icontains=q)
    )
    for trip in trips :
        if not trip in trips2:
            trips2.append(trip)


    tripcount=trips.count()
    types=TripType.objects.all()
    feedbacks=FeedBack.objects.all()
    
    notificated=False
    if request.user.is_authenticated:
        notifications=Notification.objects.filter(user=request.user)
        if len(notifications)>0:
            notificated=True
    else:
        notifications=[]
    
    #load forms:
    createuser=CreateUserForm()
    loginform=LoginForm()
    feedform=FeedbackForm()
    
    if request.method=='POST':

        if 'login_user_form' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(email=email)
            except:
                messages.error(request,'Votre email est incorrecte')
                return redirect('message_page')
            
            
            profile_obj = Profile.objects.filter(user = user ).first()
            if profile_obj is not None:
                if not profile_obj.is_verified:
                    messages.success(request, 'Votre Compte n est pas encore vérifié')
                    return redirect('message_page')
            
            user = authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Votre mot de passe est incorrecte , veuillez réessayer ou cliquer sur mot de passe oublié dans la fenêtre de Login')
                return redirect('message_page')
    #------------------------------------------------------------------
        elif 'create_user_form' in request.POST:
            
            name=request.POST.get('name')
            phonenumber=request.POST.get('number')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')

            
            if User.objects.filter(email=email).exists():
                messages.error(request,'Addresse mail existe déja ')
                return redirect('message_page')

            if User.objects.filter(username=username).exists():   
                messages.error(request,'username existe déja ')
                return redirect('message_page')

            if len(password)<4:
                messages.error(request,'mot de passe est très court ')
                return redirect('message_page')

            try:    
                user = User.objects.create(
                    name=name,
                    phonenumber=phonenumber,
                    email=email,
                    username=username,
                ) 
                user.set_password(password)
                user.username = user.username.lower()
                user.save()
                
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
                profile_obj.save()
                current_site = get_current_site(request)
                print(current_site.domain)
                domain='http://127.0.0.1:8000/'
                send_mail_after_registration(user.username,email , auth_token,domain)
                return redirect('/token')

            except Exception as e:
                print(e)
        
        elif 'feed_form' in request.POST:

            for i in range(10):
                name='rating'+str(i+1)
                rate=request.POST.get(name)
                if rate is not None:
                    break
            FeedBack.objects.create(
                user=request.user,
                body=request.POST.get('comment'),
                rate=int(rate)//2
            )
            return redirect('home')

    context={'types':types,'trips':trips2,'tripcount':tripcount,
             'loginform':loginform,'createuser':createuser,
             'notificated':notificated,'feedbacks':feedbacks,'page':'home',
             'feedform':feedform,'range':range(5)}

    return render(request,'homeTrip.html',context)