class Slider {
    constructor(document_select, index = 0) {
        this.slides = document.querySelectorAll(document_select);
        this.current_index = index;
        this.init();
    }

    get index() {
        return this.current_index;
    }

    set index(value) {
        this.current_index = value;
    }

    init() {
        this.showSlide(this.index);
        document.querySelector('.next-slide button').addEventListener('click', () => this.nextSlide());
        document.querySelector('.prev-slide button').addEventListener('click', () => this.prevSlide());
    }

    showSlide(index) {
        this.slides.forEach((slide) => slide.classList.remove('active'));
        this.slides[index].classList.add('active');
    }

    nextSlide() {
        this.index = (this.index + 1) % this.slides.length;
        this.showSlide(this.index);
    }

    prevSlide() {
        this.index = (this.index - 1 + this.slides.length) % this.slides.length;
        this.showSlide(this.index);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const slider = new Slider(document_select = '.slider li', index = 0);
});
