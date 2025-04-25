/**
 * @param {number} n
 * @return {string[]}
 */
var validStrings = function(n) {
    
    var result = [];
    for(var i = 0; i < 2 ** n; i++){
        var bin_str = i.toString(2).padStart(n, "0");

        if(bin_str.match("00") === null){
            result.push(bin_str);
        }
    }
    return result;
};

n = 1;
result = validStrings(n);
console.log(result);