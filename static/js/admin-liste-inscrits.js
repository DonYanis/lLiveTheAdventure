let sorties = document.getElementsByClassName("sortie");
let darkCover = document.getElementsByClassName("dark-cover")[0];
let tableauAnnuler = document.getElementsByClassName("tableau-annuler")[0];
let tableauFermerInscription = document.getElementsByClassName("tableau-fermer-inscription")[0];
let creerSortie = document.getElementsByClassName("creerSortie")[0];
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






document.getElementsByClassName("dark-cover")[0].addEventListener("click",()=>{
    darkCover.style.display="none";
    tableauLogOut.style.display="none";
    creerSortie.style.display="none";
    tableauAnnuler.style.display="none";
    tableauFermerInscription.style.display="none";
})
modifierPofileListe.addEventListener("click",()=>{
    modifierStatutListe.style.display="block";
    modifierPointsListe.style.display="block";
    statutListe.style.display="none";
    pointsListe.style.display="none";
    modifierPofileListe.style.display="none";
    enregistrerPofileListe.style.display="block";
})
enregistrerPofileListe.addEventListener("click",()=>{
    modifierStatutListe.style.display="none";
    modifierPointsListe.style.display="none";
    statutListe.style.display="block";
    pointsListe.style.display="block";
    modifierPofileListe.style.display="block";
    enregistrerPofileListe.style.display="none";
})


// -------------log out-----------------


let tableauLogOut = document.getElementsByClassName("tableau-log-out")[0];

document.getElementById("log-out").addEventListener("click",()=>{
    darkCover.style.display="block";
    tableauLogOut.style.display="flex";
});
document.getElementById("log-out-non").addEventListener("click",()=>{
    darkCover.style.display="none";
    tableauLogOut.style.display="none";
});