/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */

var addSpaces = function(s, spaces) {
    
    var nextSpace;
    var j = 0;
    
    nextSpace = spaces[j++];

    var output = "";

    for(var i = 0; i < s.length; i++){

        if(i === nextSpace){
            output += " " + s[i];
            nextSpace = spaces[j++];
        }

        else{
            output += s[i];
        }
    }

    return output;
};

s = "spacing";
spaces = [0,1,2,3,4,5,6];
console.log(addSpaces(s, spaces));