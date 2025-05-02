/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {

    var map = new Map();

    for(var ch of s){
        if(!map.has(ch)){
            map.set(ch, 1);
        }
        else{
            map.set(ch, map.get(ch) + 1);
        }
    }

    var result = 0;
    for(var ch of t){
        if(map.has(ch)){
            
            if(map.get(ch) !== 0){
                map.set(ch, map.get(ch) - 1);
            }
            else{
                result++;
            }
        }
        else{
            result++;
        }
    }

    return result;
};

s = "anagram";
t = "mangaar";
result = minSteps(s, t);
console.log(result);