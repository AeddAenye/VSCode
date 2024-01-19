let runner = document.querySelector(".runner");
let score = document.querySelector("span.score")
let counter = 0;

function teleport(){
    runner.style.transition = "0.5s"
    runner.style.left = Math.random() * (window.innerWidth - runner.offsetWidth) + 'px'
    runner.style.top = Math.random() * (window.innerHeight - runner.offsetHeight) + 'px'
    console.log("Бананчики телепортированы")
}

runner.addEventListener('mouseover', teleport)

runner.addEventListener('click', function(){
    score.innerText = ++counter;
    console.log("Бананчик засчитан");
    teleport()
})