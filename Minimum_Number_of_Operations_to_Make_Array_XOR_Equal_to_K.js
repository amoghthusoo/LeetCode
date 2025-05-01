/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    
    var arrXor = 0;
    for(var num of nums){
        arrXor ^= num;
    }

    var xorWithK = (k ^ arrXor).toString(2);

    var count = 0;
    for(var ch of xorWithK){
        if(ch === "1"){
            count++;
        }
    }

    return count;
};

nums = [2,0,2,0];
k = 0;
console.log(minOperations(nums, k));