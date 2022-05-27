


// ----------mobile slider---------------

let slider = document.getElementsByClassName("slider")[0];
let sliderLeft = document.getElementsByClassName("go-left")[0];
let sliderRight = document.getElementsByClassName("go-right")[0];
sliderLeft.addEventListener("click", ()=>{ 
        slider.scrollTo({top: 0,left: slider.scrollLeft - 340,behavior: "smooth"});
})
sliderRight.addEventListener("click", ()=>{
        slider.scrollTo({top: 0,left: slider.scrollLeft + 340,behavior: "smooth"});
})
slider.addEventListener("scroll", (e)=>{
    if (slider.scrollLeft + 400== slider.scrollWidth){
        sliderRight.style.opacity=".4"
        sliderRight.style.cursor="default"
    } else{
        sliderRight.style.opacity="1"
        sliderRight.style.cursor="pointer"
    }
    if (slider.scrollLeft ==0){
        sliderLeft.style.opacity=".4"
        sliderLeft.style.cursor="default"
    } else{
        sliderLeft.style.opacity="1"
        sliderLeft.style.cursor="pointer"
    }
})





// ----------desktop slider---------------
let blogs = document.getElementsByClassName("main-blogs");
let leftArrow = document.getElementsByClassName("left-arrow");
let rightArrow = document.getElementsByClassName("right-arrow");



for (let i = 0; i < leftArrow.length; i++) {
    leftArrow[i].addEventListener("click", ()=>{
        blogs[0].before(blogs[blogs.length - 1]);
    })
}
for (let i = 0; i < rightArrow.length; i++) {
    rightArrow[i].addEventListener("click", ()=>{
        let blogs0=blogs[0]
        for (let i = blogs.length -1; i = 0; i--) {
            blogs[i-1].before(blogs[i]);
        }
        blogs[blogs.length - 1].after(blogs[0]);
        blogs[blogs[blogs.length - 1]]=blogs0
    })   
}
