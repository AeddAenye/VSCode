function count(element) {
    let section = element.closest('.area, .cornets, .torch, .lamp');

    if(section && section.classList.contains("cornets")){
        let count_elem = section.querySelector('.count');
        let count = parseInt(count_elem.innerText);
        const action = element.classList.contains('plus') ? 'increment' : 'decrement';

        if (action === 'increment') {
            ++count;
        } else if (action === 'decrement' && count > 4) {
            --count;
        }

        count_elem.innerText = count;

    }
    else if (section) {
        let count_elem = section.querySelector('.count');
        let count = parseInt(count_elem.innerText);
        const action = element.classList.contains('plus') ? 'increment' : 'decrement';

        if (action === 'increment') {
            ++count;
        } else if (action === 'decrement' && count > 0) {
            --count;
        }

        count_elem.innerText = count;
    }
}
