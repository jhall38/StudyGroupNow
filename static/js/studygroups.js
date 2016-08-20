
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
