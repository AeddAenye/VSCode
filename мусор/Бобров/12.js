class Worker{
    #name
    #surname
    #rate
    #days

    constructor(name, surname, rate=1, days=1){
        this.#name = name
        this.#surname = surname
        this.#rate = rate
        this.#days = days
    }

    set name(name){
        this.#name = name
    }

    get name(){
        return this.#name
    }

    set surname(surname){
        this.#surname = surname
    }

    get surname(){
        return this.#surname
    }

    set days(num){
        this.#days = num
    }

    get days(){
        return this.#days
    }

    set rate(num){
        this.#rate = num
    }

    get rate() {
        return this.#rate
    }

    Salary(){
        return Number(this.#rate) * Number(this.#days)
    }
}

let worker = new Worker('Жамшут', 'Корнеплод', 3, 10);


console.log(`рабочий ${worker.name} ${worker.surname} заработал ${worker.Salary()}у.е. за ${worker.days} дня/дней`)
