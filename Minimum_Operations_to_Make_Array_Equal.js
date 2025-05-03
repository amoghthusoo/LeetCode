/**
 * @param {number} n
 * @return {number}
 */
var minOperations = function(n) {
    
    if(n % 2 === 0) return n ** 2 / 4;
    return (n ** 2 - 1) / 4;
};