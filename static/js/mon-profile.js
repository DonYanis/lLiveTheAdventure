let changeInfo = document.getElementsByClassName("change-info");
let enregistrer = document.getElementsByClassName("enregistrer");
let darkCover = document.getElementsByClassName("dark-cover")[0];
let tableau = document.getElementsByClassName("tableau")[0];

// image upload and changing

document.getElementById("change-pic").addEventListener("click", () => {
  darkCover.style.display = "block";
  tableau.style.display = "flex";
});
document.getElementsByClassName("close")[0].addEventListener("click", () => {
  darkCover.style.display = "none";
  tableau.style.display = "none";
});


document.getElementById("remove-picture").addEventListener("click", () => {
  darkCover.style.display = "none";
  tableau.style.display = "none";
});

// changing informations

for (let i = 0; i < changeInfo.length; i++) {
  changeInfo[i].addEventListener("click", (e) => {
    console.log(e.target.closest("li").querySelector("div"));
    e.target.closest("li").querySelector("div").style.display = "none";
    e.target.closest("li").querySelector("svg").style.display = "none";
    e.target.closest("li").querySelector("form").style.display = "block";
    e.target.closest("li").querySelector("button").style.display = "block";
  });
}
for (let i = 0; i < enregistrer.length; i++) {
  enregistrer[i].addEventListener("click", (e) => {
    console.log(e.target.closest("li").querySelector("div"));
    e.target.closest("li").querySelector("div").style.display = "block";
    e.target.closest("li").querySelector("svg").style.display = "block";
    e.target.closest("li").querySelector("form").style.display = "none";
    e.target.closest("li").querySelector("button").style.display = "none";
  });
}

/* --------------------- */
function openNavProfile() {
  document.querySelector(".navbar-responsive").style.height = "100%";
  document.querySelector("main").classList.add("blur");
}

function closeNavProfile() {
  document.querySelector(".navbar-responsive").style.height = "0%";
  document.querySelector("main").classList.remove("blur");
}
