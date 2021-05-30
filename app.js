const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");


window.history.forward();
        function noBack() {
            window.history.forward();
        }

    


loginButton.addEventListener("click", (e) => 
{
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "web_dev") {
        window.location.replace("index.html");
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})