/*For dynamic movement of login page*/
var x = document.getElementById("login");
var y = document.getElementById("register");
var z = document.getElementById("btn");
var a = document.getElementById("form-box");
var b = document.getElementById("social");
var c = document.getElementById("submit-btn");

let button = document.querySelector('.button');
let buttonText = document.querySelector('.tick');

const tickMark = "<svg width=\"45\" height=\"47\" viewBox=\"0 0 58 45\" xmlns=\"http://www.w3.org/2000/svg\"><path fill=\"#fff\" fill-rule=\"nonzero\" d=\"M19.11 44.64L.27 25.81l5.66-5.66 13.18 13.18L52.07.38l5.65 5.65\"/></svg>";
buttonText.innerHTML = "Submit";

button.addEventListener('click', function () {

    if (buttonText.innerHTML !== "Submit") {
        buttonText.innerHTML = "Submit";
    } else if (buttonText.innerHTML === "Submit") {
        buttonText.innerHTML = tickMark;
    }
    this.classList.toggle('button__circle');
});

function social() {
    b.addEventListener("mouseover", function () {
        b.style.backgroundColor = "#a5d8ff";
        b.style.border = "3px";
        b.style.borderRadius = "10px";
    });
    b.addEventListener("mouseout", function () {
        b.style.backgroundColor = "#3b5bdb";
    });
}

function login() {
    x.style.left = "50px";
    y.style.left = "450px";
    z.style.left = "0";
    a.style.height = "480px";
}

function log() {
    c.addEventListener("mouseover", function () {
        c.style.backgroundColor = "#1864ab";
        c.style.color = "#74c0fc";
    })
    c.addEventListener("mouseout", function () {
        c.style.backgroundColor = "#74c0fc";
        c.style.color = "#1864ab";
    })
}

function register() {
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "110px";
    a.style.height = "650px";
    /*Form Validation*/
    const fname = document.getElementById("Firstname");
    const lname = document.getElementById("Lastname");
    const mail = document.getElementById("email");
    const password = document.getElementById("password");
    const confirm = document.getElementById("confirmpassword");
    const form = document.getElementById("register");
    const errorelement = document.getElementById("error2");
    const terms = document.getElementById("terms");
    const container = document.getElementById("form-box");

    form.addEventListener('submit', (e) => {
        let messages2 = []
        if (fname.value === '' || fname.value === null) {
            messages2.push("First name is required");
        }
        if (lname.value === '' || lname.value === null) {
            messages2.push("Last name is required");
        }
        if (email.value === '' || email.value === null) {
            messages2.push("Email is required");
        }
        if (password.value === '' || password.value === null) {
            messages2.push("Password is required");
        }
        if (confirmpassword.value === '' || confirmpassword.value === null) {
            messages2.push("Reconfirm password !!!");
        }
        if (password.value != confirmpassword.value) {
            messages2.push("Passwords don't match!!!");
        }
        /*Display the error in UI*/
        if (messages2.length > 0) {
            e.preventDefault();
            errorelement.style.paddingTop = "10px";
            errorelement.innerText = messages2.join(', ');
            terms.style.paddingBottom = "65px";
            container.style.height = "700px";
        }

        if (password.value != '' || password.value != null) {
            if (password.value.length <= 6) {
                messages2.push("Password must be longer than 6 characters");
            }
            if (password.value.length > 20) {
                messages2.push("Password must not exceed 20 characters");
            }
        }
    })
}


