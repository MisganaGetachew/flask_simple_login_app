
let subBtn = document.getElementById('submit_btn')
subBtn.disabled = true

function clicked(input) {
    let value = input.value

    if (value > 0 && value <= 100) {
        input.style.borderColor = "";
        subBtn.disabled = false

    }
    else {
        subBtn.disabled = true
        input.style.borderColor = "red";
        // note = document.getElementById('note')
        // note.innerHtml = 'please insert values'
    }

}