/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */

var stringHash = function(s, k) {
    
    var output = "";
    var count = 0;
    var temp = 0;
    for(var i = 0; i < s.length; i++){

        temp += s[i].charCodeAt(0) - 97;
        count++;

        if(count === k){
            count = 0;
            temp = temp % 26;
            output += String.fromCharCode(temp + 97)
            temp = 0;
        }
    }

    return output;
};


s = "mxz";
k = 3;
var output = stringHash(s, k);
console.log(output);