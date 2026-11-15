

const isSubmited = document.getElementById("contact-form");
const success = document.getElementById("success");

isSubmited.addEventListener("submit", function (event){
    event.preventDefault();

    success.style.display ="block";
})