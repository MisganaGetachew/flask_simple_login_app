let submitBtn = document.getElementById('smbtn')
let password = document.getElementById('passId')
let passwordConfirm = document.getElementById('passIdconfirm')
let userID = document.getElementById('userId')
let message = document.getElementById('error-message')
submitBtn.disabled = false
function clicked() {

    var regexUser = /^[a-zA-Z]+$/;
    // var regexpassword = /^[0-9+$]/
    // checkPassword = regexpassword.test(password.value)
    checkUser = regexUser.test(userID.value)

    if (checkUser) {
        submitBtn.disabled = false
        userID.style.borderColor = ''
        message.innerText = ''


    }
    else {
        submitBtn.disabled = true
        userID.style.borderColor = "red"
        message.innerText = "Incorrect username. Please try again."
    }

}

function clicked1() {

    if (passwordConfirm.value == password.value) {
        submitBtn.disabled = false
        password.style.borderColor = ""
        passwordConfirm.style.borderColor = ""
        message.innerText = ''

    }

    else {
        submitBtn.disabled = true
        password.style.borderColor = "red"
        passwordConfirm.style.borderColor = "red"
        message.innerText = "The password doesn't match. Please try again."
    }

}