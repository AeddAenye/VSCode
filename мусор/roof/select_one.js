function handle_click(element) {
    let section = element.closest('.texture, .maker');

    if (section) {
        section.querySelectorAll('.button').forEach(button => {
            button.classList.remove('selected');
        });

        element.classList.add('selected');
    }
}
