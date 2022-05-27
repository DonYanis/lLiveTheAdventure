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

    if(screen.width>=800){
        if (slider.scrollLeft + 620== slider.scrollWidth){
            sliderRight.style.opacity=".4"
            sliderRight.style.cursor="default"
        } else{
            sliderRight.style.opacity="1"
            sliderRight.style.cursor="pointer"
        }
    }else{
        if (slider.scrollLeft + 400== slider.scrollWidth){
            sliderRight.style.opacity=".4"
            sliderRight.style.cursor="default"
        } else{
            sliderRight.style.opacity="1"
            sliderRight.style.cursor="pointer"
        }
    }
    
    if (slider.scrollLeft ==0){
        sliderLeft.style.opacity=".4"
        sliderLeft.style.cursor="default"
    } else{
        sliderLeft.style.opacity="1"
        sliderLeft.style.cursor="pointer"
    }
})
