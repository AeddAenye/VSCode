function first_letters(text) {
    let words = []
    text.split('.').forEach(rawsent => {
        words.push(rawsent.trim().split(' ')[0])
    })
    return words.filter(function (el) { return (el != "") })
}

console.log(first_letters("One one. Two two. Three three."))