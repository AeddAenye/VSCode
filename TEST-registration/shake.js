export function shake(element) {
    element.classList.add('shake');
    setTimeout(() => {
        element.classList.remove('shake');
        element.classList.add('reset-color');
        setTimeout(() => {
            element.classList.remove('reset-color');
        }, 500);
    }, 500);
}