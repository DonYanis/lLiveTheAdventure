/* testo player */
var testoPlayer;

var testoPlayer = (id) => {
  let slideIndex = 1;
  playSlider = setInterval(function () {
    let i;
    let sliderShow = document.getElementById(id);
    let slides = sliderShow.getElementsByClassName("testo-slide");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    slideIndex++;

    if (slideIndex > slides.length) {
      slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";
    slides[slideIndex - 1].classList.add("fadeInRight");
  }, 3500);
};
var mySlides = document.querySelectorAll(".testo-slider");
for (let index = 0; index < mySlides.length; index++) {
  var myslide = mySlides[index];
  var thisID = myslide.getAttribute("id");
  testoPlayer(thisID);
}

/* victor hide */
var divscroll = document.getElementsByClassName("divScroll");
for (let i = 0; i < divscroll.length; i++) {
  var div = divscroll[i];
  div.addEventListener("mousewheel", (e) => {
    btnscroll = document.getElementsByClassName("vict-scroll")[i];
    if (e.deltaY > 0) {
      btnscroll.classList.add("fade-vector");
    } else {
      btnscroll.classList.remove("fade-vector");
    }
  });
}
