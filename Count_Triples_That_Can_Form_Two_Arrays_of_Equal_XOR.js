/**
 * @param {number[]} arr
 * @return {number}
 */
var countTriplets = function(arr) {

    var triplesCount = 0;

    for(var i = 0; i < arr.length; i++){
        
        var tempXOR = arr[i];
        for(var j = i + 1; j < arr.length; j++){
            
            tempXOR ^= arr[j];
            if(tempXOR === 0){
                triplesCount += j - i;
            }
        }
    }
    return triplesCount;
};

arr = [2,3,1,6,7];
var result = countTriplets(arr);
console.log(result);