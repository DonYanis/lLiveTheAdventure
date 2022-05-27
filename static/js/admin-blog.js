


// -------------log out-----------------


let darkCover = document.getElementsByClassName("dark-cover")[0];
let tableauLogOut = document.getElementsByClassName("tableau-log-out")[0];

document.getElementsByClassName("dark-cover")[0].addEventListener("click",()=>{
    darkCover.style.display="none";;
    tableauLogOut.style.display="none";
})
document.getElementById("log-out").addEventListener("click",()=>{
    darkCover.style.display="block";
    tableauLogOut.style.display="flex";
});
document.getElementById("log-out-non").addEventListener("click",()=>{
    darkCover.style.display="none";
    tableauLogOut.style.display="none";
});