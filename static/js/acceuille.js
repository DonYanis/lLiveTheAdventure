function dropthum() {
  document.getElementById("profil-menu").classList.toggle("show");
}
window.onclick = function (event) {
  if (!event.target.matches("#thum")) {
    var openDropdown2 = document.querySelector(".dropdown-content");
    if (openDropdown2.classList.contains("show")) {
      openDropdown2.classList.remove("show");
    }
  }
};

/* -------------------------bg lancer */
const notBtns = document.getElementsByClassName("btn-primary");
for (let i = 0; i < notBtns.length; i++) {
  var notBtn = notBtns[i];
  notBtn.addEventListener("click", () => {
    const bgContainer = document.querySelector(".bg-container");
    console.log(bgContainer);
    bgContainer[i].style.display = "block";
  });
}
/* -----------------------------voir plus sliderShow --------------------------------*/
let slidesPlus = 0;
showSlidesPlusVue();

function showSlidesPlusVue() {
  let i;
  let slides = document.getElementsByClassName("imgSlidePlus");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slidesPlus++;
  if (slidesPlus > slides.length) {
    slidesPlus = 1;
  }
  slides[slidesPlus - 1].style.display = "block";
  slides[slideIndex - 1].classList.add("fadeImg2");

  setTimeout(showSlidesPlusVue, 2000);
}
function openNav() {
  /* ---------------------new modifications----------------------- */
  document.querySelector("#main-nav").style.height = "100%";
  document.querySelector("main").classList.add("blur");
  document.querySelector("body").classList.add("stop");
}

function closeNav() {
  /* ---------------------new modifications----------------------- */

  var navs = document.getElementsByClassName("navbar-responsive");
  for (let i = 0; i < navs.length; i++) {
    var nav = navs[i];
    nav.style.height = "0%";
  }
  document.querySelector("main").classList.remove("blur");
  document.querySelector("body").classList.remove("stop");
  var drop = document.querySelector(".navbar-nav-resp");
  if (drop.classList.contains("prolonge")) {
    drop.classList.remove("prolonge");
  }
}
function dropdown() {
  var drop = document.querySelector(".navbar-nav-resp");
  if (drop.classList.contains("prolonge")) {
    drop.classList.remove("prolonge");
  } else {
    drop.classList.add("prolonge");
  }
}
/* ---------------------LOADING NOTIFICATIONS MOBILE VIEWPORT------------------------------- */
function loadNotification() {
  /* ---------------------new modifications----------------------- */
  var message = document.getElementById("message-congrat-resp");
  message.style.height = "100%";
  document.querySelector("#main-nav").style.height = "0%";
  document.querySelector("main").classList.add("blur");
}
function loadFeedback() {
  var message = document.getElementById("feedback-resp");
  message.style.height = "100%";
  document.querySelector("#main-nav").style.height = "0%";
  document.querySelector("main").classList.add("blur");
}
function returnMainNav() {
  var navs = document.getElementsByClassName("navbar-responsive");
  for (let i = 0; i < navs.length; i++) {
    var nav = navs[i];
    nav.style.height = "0%";
  }
  openNav();
}
