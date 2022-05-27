let sorties = document.getElementsByClassName("sortie");
let blogs = document.getElementsByClassName("blog");
let darkCover = document.getElementsByClassName("dark-cover")[0];
let tableauLogOut = document.getElementsByClassName("tableau-log-out")[0];
let tableauSorties = document.getElementsByClassName("tableau-sorties")[0];
let tableauBlogs = document.getElementsByClassName("tableau-blogs")[0];
let creerSortie = document.getElementsByClassName("creerSortie")[0];
let creerBlog =document.getElementsByClassName("creerBlog")[0];
let detailsSorties = document.getElementsByClassName("detailsSorties")[0];
let closes = document.getElementsByClassName("close");
let detailsSortie = document.getElementById("detailsSortie");
let annulerSortie = document.getElementById("annulerSortie");
let listeDesInscrits = document.getElementById("liste-des-inscrits");
let modifierStatutSortie= document.getElementById("statut-sortie");
let modifierPointsSortie= document.getElementById("points-sortie");
let modifierStatutListe= document.getElementById("statut-liste");
let modifierPointsListe= document.getElementById("points-liste");
let statutSortie= document.getElementsByClassName("statut-sortie")[0];
let pointsSortie= document.getElementsByClassName("points-sortie")[0];
let statutListe= document.getElementsByClassName("statut-liste")[0];
let pointsListe= document.getElementsByClassName("points-liste")[0];
let modifierPofileSortie= document.getElementById("modifierPofileSortie");
let modifierPofileListe= document.getElementById("modifierPofileListe");
let enregistrerPofileSortie= document.getElementById("enregistrerPofileSortie");
let enregistrerPofileListe= document.getElementById("enregistrerPofileListe");




let chosenSortie;
let chosenBlog;

for (let i = 0; i < closes.length; i++) {
    closes[i].addEventListener("click",()=>{
        darkCover.style.display="none";
        creerSortie.style.display="none";
        creerBlog.style.display="none";
        tableauLogOut.style.display="none";
        listeDesInscrits.style.display="none";
    })
}
document.getElementsByClassName("dark-cover")[0].addEventListener("click",()=>{
    darkCover.style.display="none";;
    tableauLogOut.style.display="none";
    creerSortie.style.display="none";
    creerBlog.style.display="none";
    listeDesInscrits.style.display="none";
})
document.getElementById("log-out").addEventListener("click",()=>{
    darkCover.style.display="block";
    tableauLogOut.style.display="flex";
});
document.getElementById("log-out-non").addEventListener("click",()=>{
    darkCover.style.display="none";
    tableauLogOut.style.display="none";
});
document.getElementById("ajouterSortie").addEventListener("click",()=>{
    darkCover.style.display="block";
    creerSortie.style.display="flex";
});
document.getElementById("ajouterBlog").addEventListener("click",()=>{
    darkCover.style.display="block";
    creerBlog.style.display="flex";
});
