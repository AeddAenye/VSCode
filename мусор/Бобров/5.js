function fives(nums) {
    let arr = []
    nums.forEach(num => {
        if (num % 5 === 0) {
            arr.push(num)
        }
    });
    
    return arr
}

console.log(fives([1, 2, 3, 4, 5, 10]))