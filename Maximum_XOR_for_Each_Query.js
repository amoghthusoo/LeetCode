/**
 * @param {number[]} nums
 * @param {number} maximumBit
 * @return {number[]}
 */
var getMaximumXor = function(nums, maximumBit) {
    
    var maxPossibleXOR = 2 ** maximumBit - 1;
    var resultArr = [];

    var cummulativeXOR = 0;
    for(var e of nums){
        cummulativeXOR ^= e;

        var tempXOR = cummulativeXOR ^ maxPossibleXOR;
        resultArr.push(tempXOR);
    }
    resultArr.reverse();
    return resultArr;
};

nums = [2,3,4,7];
maximumBit = 3;
var result = getMaximumXor(nums, maximumBit);
console.log(result);