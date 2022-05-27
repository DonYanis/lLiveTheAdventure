/* /////////////------------------Auto play------------------/////////////////// */
var playSlider;

var repeater = (id) => {
  let slideIndex = 1;
  playSlider = setInterval(function () {
    let i;
    let sliderShow = document.getElementById(id);
    let slides = sliderShow.getElementsByClassName("imgSlide");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    slideIndex++;

    if (slideIndex > slides.length) {
      slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";
    slides[slideIndex - 1].classList.add("fadeImg");
  }, 3000);
};
var mySlides = document.querySelectorAll(".sliderShow");
for (let index = 0; index < mySlides.length; index++) {
  var myslide = mySlides[index];
  var thisID = myslide.getAttribute("id");
  repeater(thisID);
}
