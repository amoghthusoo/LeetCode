function getPermutation(s) {

    if (s.length === 1) {
        return s;
    }

    var permutations = [];

    for (var i = 0; i < s.length; i++) {

        var ch = s[i];
        var remainingStr = s.slice(0, i) + s.slice(i + 1, s.length);

        var interPermutations = getPermutation(remainingStr);
        for (var j = 0; j < interPermutations.length; j++) {
            permutations.push(ch + interPermutations[j]);
        }
    }
    return permutations;
}

function getCombinations(s){

    var n = 2 ** s.length;
    var result = [];

    for(var i = 1; i < n; i++){
        
        var binStr = i.toString(2).padStart(s.length);
        var tempStr = "";
        
        for(var j = 0; j < binStr.length; j++){
            if(binStr[j] === "1"){
                tempStr += s[j];
            }
        }
        
        result.push(tempStr);
    }
    return result;
}


var numTilePossibilities = function(tiles) {
    
    var combinations = getCombinations(tiles);
    var set = new Set();

    for(var combination of combinations){
        if(!set.has(combination)){
            set.add(combination);

            for(var e of getPermutation(combination)){
                set.add(e);
            }
        }
    }
    return set.size;
};


var tiles = "";
console.time();
var result = numTilePossibilities(tiles);
console.timeEnd();
console.log(result);
// console.log(getPermutation(tiles));
// console.log(getCombinations(tiles));