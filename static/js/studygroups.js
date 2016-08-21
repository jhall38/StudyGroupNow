
/* validate login page */
function validateLogin() {
    var username = document.forms["login"]["username"].value;
    var password = document.forms["login"]["password"].value;
    if (username == null || username == "") {
        alert("Please enter a username");
        return false;
    } else if (password == null || password == "") {
    	alert("Please enter a password");
        return false;
    }
}

/* validate signup page */
function validateSignup() {
    var username = document.forms["signup"]["username"];
    var email = document.forms["signup"]["email"];
    var regex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
    var password = document.forms["signup"]["password"];
    var confirmpassword = document.forms["signup"]["confirmpassword"];
    if (username.value == null || username.value == "") {
        document.getElementById("errors").innerHTML = "Please enter a username!";
        return false;
    } else if (email.value.search(regex) == -1) {
        document.getElementById("errors").innerHTML = "Please enter a valid email address!";
        return false;
    } else if (password.value == null || password.value == "") {
         document.getElementById("errors").innerHTML = "Please enter a password!";
        return false;
    } else if (confirmpassword.value == null || confirmpassword.value == "") {
        document.getElementById("errors").innerHTML = "Please confirm your password!";
        return false;
    } else if (password.value != confirmpassword.value) {
         document.getElementById("errors").innerHTML = "Passwords do not match try again!";
        return false;
    }
}