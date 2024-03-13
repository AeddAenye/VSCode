let addBtn = document.querySelector('#add')
let tasks = []
let cardsContainer = document.querySelector('.cards')

cardsContainer.addEventListener('click', function(event){
    if (event.target.classList.contains('del')) {
        let card = event.target.closest('.card')
        let taskIndex = tasks.findIndex(task => task.text === card.querySelector('.text').textContent)
        tasks.splice(taskIndex, 1)
        card.remove()
    }
})

addBtn.addEventListener('click', function(){
    let input = document.querySelector('#tasktext')
    if (input.value !== ''){
        let newTask = {text: input.value, id: Date.now()}
        
        cardsContainer.innerHTML += 
        `<div class="card">
            <span class="text">${input.value}</span>
            <button type="button" class="del">Del</button>
        </div>`

        tasks.push(newTask)
        input.value = ''
    }
})
