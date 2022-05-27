document.onreadystatechange = function () {
    if (document.readyState !== "complete") {
      document.querySelector("body").style.visiblity = "none";
      document.querySelector("header").style.display = "none";
      document.querySelector("main").style.display = "none";
      document.querySelector(".spinner-container").style.display = "auto";
  
      document.querySelector(".dot-container").classList.add("hide-loading");
    } else {
      document.querySelector(".spinner-container").style.display = "none";
      document.querySelector("header").style.display = "block";
      document.querySelector("main").style.display = "block";
      document.querySelector("body").style.visiblity = "visible";
      document.querySelector(".dot-container").classList.remove("hide-loading");
    }
  };
  