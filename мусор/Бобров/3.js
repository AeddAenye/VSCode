function hello(name) {
    let hour = Number(new Date().getHours())

    if (hour >= 5 && hour <= 12){
        return `Доброе утро ${name}`
    }
    else if (hour >= 13 && hour <= 16){
        return `Добрый день ${name}`
    }

    else if (hour >= 17 && hour <= 20){
        return `Добрый вечер ${name}`
    }

    else if (hour >= 21 && hour <= 4){
        return `Доброй ночи ${name}`
    }

    else {
        return `Неизвестное время ${name}`
    }
}


console.log(hello("ADAE"))