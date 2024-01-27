function weekly_date(date) {
    if (date !== NaN){
        return ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"][date-1]
    }
}

console.log(weekly_date(7))