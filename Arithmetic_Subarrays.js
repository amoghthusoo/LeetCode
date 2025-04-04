/**
 * @param {number[]} nums
 * @param {number[]} l
 * @param {number[]} r
 * @return {boolean[]}
 */
var checkArithmeticSubarrays = function(nums, l, r) {

    var result = [];
    for(var i = 0; i < l.length; i++){
        
        var apMem = true;
        var subarr = nums.slice(l[i], r[i] + 1);
        subarr.sort((a, b) => a - b);
        var d = subarr[1] - subarr[0];
        
        for(var j = 1; j < subarr.length - 1; j++){
            if(subarr[j + 1] - subarr[j] !== d){
                result.push(false);
                apMem = false;
                break;
            }
        }
        
        if(apMem){
            result.push(true);
        }
    }

    return result;
};

var nums = [-3,-6,-8,-4,-2,-8,-6,0,0,0,0];
var l = [5,4,3,2,4,7,6,1,7];
var r = [6,5,6,3,7,10,7,4,10];
var result = checkArithmeticSubarrays(nums, l, r);
console.log(result);