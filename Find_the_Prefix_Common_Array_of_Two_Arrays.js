/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */

function intersectionCount(x, y){
    
    var count = 0;

    for(var e of x){

        if(y.has(e)){
            count++;
        }
    }
    return count;
}

var findThePrefixCommonArray = function(A, B) {

    var setA = new Set();
    var setB = new Set();
    var result = [];

    for(var i = 0; i < A.length; i++){
        setA.add(A[i]);
        setB.add(B[i]);
        
        result.push(intersectionCount(setA, setB));

    }
    return result;
};

A = [2,3,1]
B = [3,1,2]

var result = findThePrefixCommonArray(A, B);
console.log(result);