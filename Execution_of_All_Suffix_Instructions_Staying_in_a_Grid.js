/**
 * @param {number} n
 * @param {number[]} startPos
 * @param {string} s
 * @return {number[]}
 */
var executeInstructions = function(n, startPos, s) {
    
    var x, y, count;

    var result = [];
    
    for(var i = 0; i < s.length; i++){
        x = startPos[0];
        y = startPos[1];    
        count = 0;
        for(var j = i; j < s.length; j++){

            if(s[j] === "R"){
                y++;
            }
            else if(s[j] === "D"){
                x++;
            }
            else if(s[j] === "L"){
                y--;
            }
            else if(s[j] === "U"){
                x--;
            }

            if(x >= 0 && x < n && y >= 0 && y < n){
                count++;

                if(j == s.length - 1){
                    result.push(count);
                }
            }
            else{
                result.push(count);
                break;
            }
        }
    }

    return result;

};

n = 3;
startPos = [0,1];
s = "RRDDLU";

var result = executeInstructions(n, startPos, s);
console.log(result);
