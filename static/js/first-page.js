var slideIndex = 1;

var myTimer;

var slideshowContainer;

function numbSlide(n) {
  const numslide = document.getElementById("num-indicator");
  numslide.textContent = n.toString();
}

window.addEventListener("load", function () {
  showSlides(slideIndex);
  myTimer = setInterval(function () {
    plusSlides(1);
  }, 9000);

  //COMMENT OUT THE LINE BELOW TO KEEP ARROWS PART OF MOUSEENTER PAUSE/RESUME
  slideshowContainer = document.getElementsByClassName(
    "slideshow-container"
  )[0];

  //UNCOMMENT OUT THE LINE BELOW TO KEEP ARROWS PART OF MOUSEENTER PAUSE/RESUME
  // slideshowContainer = document.getElementsByClassName('slideshow-container')[0];

  slideshowContainer.addEventListener("mouseenter", pause);
  slideshowContainer.addEventListener("mouseleave", resume);
});

// NEXT AND PREVIOUS CONTROL
function plusSlides(n) {
  clearInterval(myTimer);
  if (n < 0) {
    showSlides((slideIndex -= 1));
  } else {
    showSlides((slideIndex += 1));
  }

  //COMMENT OUT THE LINES BELOW TO KEEP ARROWS PART OF MOUSEENTER PAUSE/RESUME

  if (n === -1) {
    myTimer = setInterval(function () {
      plusSlides(n + 2);
    }, 9000);
  } else {
    myTimer = setInterval(function () {
      plusSlides(n + 1);
    }, 9000);
  }
}

//Controls the current slide and resets interval if needed
function currentSlide(n) {
  clearInterval(myTimer);
  myTimer = setInterval(function () {
    plusSlides(n + 1);
  }, 9000);
  showSlides((slideIndex = n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot-icons");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
    numbSlide(slideIndex);
  }
  slides[slideIndex - 1].style.display = "block";
  slides[slideIndex - 1].classList.add("fadeIn");
  dots[slideIndex - 1].className += " active";
}

pause = () => {
  clearInterval(myTimer);
};

resume = () => {
  clearInterval(myTimer);
  myTimer = setInterval(function () {
    plusSlides(slideIndex);
  }, 8000);
};

/* /////////////////////////autoplay img //////////////////////////*/

/* ///////---------------bgPlay-----------//////////// */
const button = document.getElementById("connect");
const button2 = document.getElementById("sign-up");

button.addEventListener("click", () => {
  const bgContainer = document.querySelector(".bg-container");
  bgContainer.style.display = "block";
});
button2.addEventListener("click", () => {
  const bgContainer = document.querySelector(".bg-container");

  bgContainer.style.display = "block";
});

function password_show_hide() {
  var show_eye = document.getElementById("show_eye1");
  var hide_eye = document.getElementById("hide_eye1");
  var x = document.getElementById("password-signup");
  hide_eye.classList.remove("d-none");
  if (x.type === "password") {
    x.type = "text";
    show_eye.style.display = "none";
    hide_eye.style.display = "block";
  } else {
    x.type = "password";
    show_eye.style.display = "block";
    hide_eye.style.display = "none";
  }
}
function password_show_hide_login() {
  var x = document.getElementById("password-login");
  var show_eye = document.getElementById("show_eye");
  var hide_eye = document.getElementById("hide_eye");
  hide_eye.classList.remove("d-none");
  if (x.type === "password") {
    x.type = "text";
    show_eye.style.display = "none";
    hide_eye.style.display = "block";
  } else {
    x.type = "password";
    show_eye.style.display = "block";
    hide_eye.style.display = "none";
  }
}
/* password checker */
const pwdIndicators = document.querySelector(".pwdchecker");
const input = document.querySelector("#password-signup");
const weak = document.querySelector(".weak");
const medium = document.querySelector(".medium");
const strong = document.querySelector(".strong");
const text = document.querySelector(".textcheker");
let regExpWeak = /[A-Za-z0-9]/;
let regExpMedium = /\d+/;
let regExpStrong = /.[!,@,#,$,%,^,&,*,?,_,~,-,(,)]/;
function trigger() {
  if (input.value != "") {
    pwdIndicators.style.display = "block";
    pwdIndicators.style.display = "flex";
    if (
      input.value.length <= 3 &&
      (input.value.match(regExpWeak) ||
        input.value.match(regExpMedium) ||
        input.value.match(regExpStrong))
    )
      no = 1;
    if (
      input.value.length >= 6 &&
      ((input.value.match(regExpWeak) && input.value.match(regExpMedium)) ||
        (input.value.match(regExpMedium) && input.value.match(regExpStrong)) ||
        (input.value.match(regExpWeak) && input.value.match(regExpStrong)))
    )
      no = 2;
    if (
      input.value.length >= 6 &&
      input.value.match(regExpWeak) &&
      input.value.match(regExpMedium) &&
      input.value.match(regExpStrong)
    )
      no = 3;
    if (no == 1) {
      weak.classList.add("active");
      text.style.display = "block";
      text.textContent = "Votre mot de passe est trop faible";
      text.classList.add("weak");
    }
    if (no == 2) {
      medium.classList.add("active");
      text.textContent = "Votre mot de passe est moyen";
      text.classList.add("medium");
    } else {
      medium.classList.remove("active");
      text.classList.remove("medium");
    }
    if (no == 3) {
      weak.classList.add("active");
      medium.classList.add("active");
      strong.classList.add("active");
      text.textContent = "Votre mot de passe est fort";
      text.classList.add("strong");
    } else {
      strong.classList.remove("active");
      text.classList.remove("strong");
    }
  } else {
    pwdIndicators.style.display = "none";
    text.style.display = "none";
  }
}

