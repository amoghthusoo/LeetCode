/**
 * @param {number[]} nums
 * @return {number}
 */
var countMaxOrSubsets = function(nums) {
    var n = nums.length
    
    var or_arr = [];
    var i = 0;
    while(i < 2 ** n){
        var bin_str = i.toString(2).padStart(n, "0");
        var or = 0 
        var j = 0;
        while(j < n){
            if(bin_str[j] === "1"){
                or = or | nums[j];
            }
            j++;
        }
        or_arr.push(or);
        i++;       
    }
    var max = Math.max(...or_arr);
    var result = or_arr.filter((e) => e === max).length;
    return result;
};

nums = [3,2,1,5];
var result = countMaxOrSubsets(nums);
console.log(result);