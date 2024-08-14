function toggleBackground(){
const body = document.querySelector("body");
const toggle = document.getElementById("wrapper");
const circle = document.querySelector(".circle");
const checkbox = document.getElementById("checkbox");
toggle.onclick = function () {
    if (checkbox.checked) {
        toggle.classList.toggle("active");
        body.classList.toggle("active");
    }
};  
}