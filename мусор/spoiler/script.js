let spoilers = document.querySelectorAll('.spoilers .spoiler_wrapper')

spoilers.forEach((elem) => {
    let title = elem.querySelector('.spoiler_title')
    let text = elem.querySelector('.spoiler_text')
    title.addEventListener('click', function () {
        text.classList.toggle('open')
        title.classList.toggle('open')
    })
})