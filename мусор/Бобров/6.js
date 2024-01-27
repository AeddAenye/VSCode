function avg(nums) {
    let sum = 0
    nums.forEach(num => {
        sum += num
    });
    
    return sum / nums.length
}

console.log(avg([2, 1]))