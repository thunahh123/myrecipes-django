function getYear(){
    var date = new Date().getFullYear();
    document.getElementById('date').innerHTML = date;
    
}

document.addEventListener('DOMContentLoaded', getYear);