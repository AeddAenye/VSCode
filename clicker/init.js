class Enemy {
    #hp;
    #max_hp;
    #img;
    #money_drop

    constructor(enemy) {
        this.#hp = enemy.hp;
        this.#max_hp = this.#hp;
        this.#img = enemy.img;
        this.#money_drop = enemy.drop_money
        document.querySelector("div.click-area img").src = enemy.img
        document.querySelector('div#entity-name ').innerText = enemy.name    
    }

    hit(damage = 1) {
        this.#hp -= damage
    }

    get hp() {
        return this.#hp
    }

    get max_hp() {
        return this.#max_hp
    }

    get drop_money() {
        return this.#money_drop
    }
}

document.addEventListener('DOMContentLoaded', function () {
    fetch('./enemies.json').then(response => response.json())
        .then(json => {
            let enemies = json.enemies

            let health = document.querySelector('div#entity-hp')
            
            let clicker = document.querySelector('div.click-area')
            let money = document.querySelector('span#money')
            let entity = new Enemy(enemies[Math.floor(Math.random() * (enemies.length))]);

            clicker.addEventListener('click', function () {
                entity.hit()
                health.style.width = `${(entity.hp / entity.max_hp) * 100}%`

                if (entity.hp === 0) {
                    health.style.width = '100%'
                    money.textContent = Number(money.textContent) + Number(entity.drop_money)
                    entity = new Enemy(enemies[Math.floor(Math.random() * (enemies.length))]);
                }
            })
        })

})

