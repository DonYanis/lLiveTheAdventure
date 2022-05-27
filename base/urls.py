from django.urls import include, path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/',views.logoutuser,name='logout'),
    path('',views.home,name='home'),

    path('token' , views.token_send , name='token_send'),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name='verify'),
    path('error' , views.error_page , name='error'),
    path('info' , views.messagesPage , name='message_page'),

    path('accounts/', include('allauth.urls')),

    path('trip/<str:pk>/<str:sk>/',views.tripPage,name='tripPage'),
    path('deletetrip/<str:pk>/',views.deleteTrip,name='delete_trip'),
    path('jointrip/<str:pk>/',views.joinTrip,name='join_trip'),
    path('acceptreservation/<str:pk>/<str:sk>/',views.acceptReservation,name='acceptreservation'),
    path('refusereservation/<str:pk>/<str:sk>/',views.refuseReservation,name='refusereservation'),
    path('deletereservation/<str:pk>/<str:sk>/',views.deleteReservation,name='deletereservation'),
    path('profile/',views.userProfile,name='userprofile'),
    path('adminblog/<str:pk>/',views.tripBlog,name='blog'),
    path('blog/<str:pk>/',views.blog,name='blogdetail'),
    path('blogs/',views.blogPage,name='blogs'),
    path('deleteblog/<str:pk>/',views.deleteBlog,name='delete_blog'),
    path('clientlist/<str:pk>/',views.clientList,name='clientlist'),
    path('closetrip/<str:pk>/',views.closeInscrisptions,name='closetrip'),
    path('feedbacks/',views.Feedbacks,name='feedbackpage'),
    path('acceptfeed/<str:pk>/',views.AcceptFeed,name='acceptfeed'),
    path('deletefeed/<str:pk>/',views.DeleteFeed,name='deletefeed'),
    path('calendar/',views.calendar,name='calendar'),
    path('deletenotif/<str:pk>/',views.deleteNotif,name='deletenotif'),
    path('hometrip/<str:pk>/',views.homeTrip,name='homespecial'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),      
    path('password_reset/', views.password_reset_request, name="password_reset"),
]