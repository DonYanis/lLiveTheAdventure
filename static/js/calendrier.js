function openNavCalendar() {
  document.querySelector(".navbar-responsive").style.height = "100%";
  document.querySelector(".container-calendar").classList.add("blur");
}
function closeNavCalendar() {
  document.querySelector(".navbar-responsive").style.height = "0%";
  document.querySelector(".container-calendar").classList.remove("blur");
}

let sorties = document.getElementsByClassName("sorties");
let idPosition;




for (let i = 0; i < sorties.length; i++) {
    if(sorties[i].id=="active"){
        idPosition=i;
    }
}
document.getElementById("left-arrow").addEventListener("click", ()=>{
    if(idPosition != 0){
        sorties[idPosition].removeAttribute('id');
        sorties[idPosition - 1].id="active"
        idPosition--;
    }
})
document.getElementById("right-arrow").addEventListener("click", ()=>{
    if(idPosition != sorties.length -1){
        sorties[idPosition].removeAttribute('id');
        sorties[idPosition + 1].id="active"
        idPosition++;
    }
})