/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */

function getCombinations(arr = ["a", "b", "c"]){
    
    var resultArr = [];

    for(var str of arr){

        if(str[str.length - 1] === "a"){
            resultArr.push(str + "b");
            resultArr.push(str + "c");
        }
        else if(str[str.length - 1] === "b"){
            resultArr.push(str + "a");
            resultArr.push(str + "c");
        }
        else if(str[str.length - 1] === "c"){
            resultArr.push(str + "a");
            resultArr.push(str + "b");
        }
    }
    return resultArr;
}

var getHappyString = function(n, k) {
    
    var combinationArr = ["a", "b", "c"];

    if(n !== 1){
        
        for(var i = 0; i < n - 1; i++){
            combinationArr = getCombinations(combinationArr);
        }

    }

    if((k - 1) < combinationArr.length){
        return combinationArr[k - 1];
    }
    else{
        return ""
    }
};


var result = getHappyString(3, 9);
console.log(result);