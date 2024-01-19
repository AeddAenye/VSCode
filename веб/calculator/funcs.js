let input = document.querySelector("input")
let stop_syms = ['+', '-', '*', '/', '.']


function add_in_input(button) {
    let value = button.innerText;

    if (input.value.endsWith(value) && stop_syms.includes(value)) {
        return;
    }
    input.value += value;
}


function clear_input() {
    input.value = ''
}

function calculate() {
    if (input.value !== "") input.value = eval(input.value)
}

let buttons = document.querySelectorAll(".num_add");
buttons.forEach(button => {
    button.addEventListener("click", function() {
        add_in_input(this);
    });
});