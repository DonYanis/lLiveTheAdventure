let sorties = document.getElementsByClassName("sortie");
let darkCover = document.getElementsByClassName("dark-cover")[0];
let tableauLogOut = document.getElementsByClassName("tableau-log-out")[0];
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





for (let i = 0; i < closes.length; i++) {
    closes[i].addEventListener("click",()=>{
        darkCover.style.display="none";
        creerSortie.style.display="none";
        listeDesInscrits.style.display="none";
    })
}
document.getElementsByClassName("dark-cover")[0].addEventListener("click",()=>{
    darkCover.style.display="none";
    tableauLogOut.style.display="none";
    creerSortie.style.display="none";
    tableauAnnuler.style.display="none";
    tableauFermerInscription.style.display="none";
})
document.getElementById("log-out").addEventListener("click",()=>{
    darkCover.style.display="block";
    tableauLogOut.style.display="flex";
});
document.getElementById("log-out-non").addEventListener("click",()=>{
    darkCover.style.display="none";
    tableauLogOut.style.display="none";
});
document.getElementById("annuler").addEventListener("click",()=>{
    darkCover.style.display="block";
    tableauAnnuler.style.display="flex";
});
document.getElementById("annuler-non").addEventListener("click",()=>{
    darkCover.style.display="none";
    tableauAnnuler.style.display="none";
});
document.getElementById("fermer-inscription").addEventListener("click",()=>{
    darkCover.style.display="block";
    tableauFermerInscription.style.display="flex";
});
document.getElementById("fermer-inscription-non").addEventListener("click",()=>{
    darkCover.style.display="none";
    tableauFermerInscription.style.display="none";
});
document.getElementById("modifierSortie").addEventListener("click",()=>{
    creerSortie.style.display="flex";
    darkCover.style.display="block";
});
modifierPofileSortie.addEventListener("click",()=>{
    modifierStatutSortie.style.display="block";
    modifierPointsSortie.style.display="block";
    statutSortie.style.display="none";
    pointsSortie.style.display="none";
    modifierPofileSortie.style.display="none";
    enregistrerPofileSortie.style.display="block";
})
enregistrerPofileSortie.addEventListener("click",()=>{
    modifierStatutSortie.style.display="none";
    modifierPointsSortie.style.display="none";
    statutSortie.style.display="block";
    pointsSortie.style.display="block";
    modifierPofileSortie.style.display="block";
    enregistrerPofileSortie.style.display="none";
})