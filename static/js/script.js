function getYear(){
    var date = new Date().getFullYear();
    document.getElementById('date').innerHTML = date;
    
}

document.addEventListener('DOMContentLoaded', getYear);


function toggleMenu() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }