/**
 * @param {number} rows
 * @param {number} cols
 * @param {number} rStart
 * @param {number} cStart
 * @return {number[][]}
 */
var spiralMatrixIII = function(rows, cols, rStart, cStart) {
    
    var x = rStart;
    var y = cStart;
    var direction = "R";
    var walkStraightFor = 1;
    var straightWalkCount = 0;
    var noOfStraightWalks = 0;
    var result = [];

    while(true){

        if(x >= 0 && x < rows && y >= 0 && y < cols){
            result.push([x, y]);
            if(result.length === (rows * cols)){
                return result;
            }
        }

        if(direction === "R"){
            y++;
        }
        else if(direction === "D"){
            x++;
        }
        else if(direction === "L"){
            y--;
        }
        else if(direction === "T"){
            x--;
        }
        straightWalkCount++;

        if(straightWalkCount === walkStraightFor){
            straightWalkCount = 0;
            noOfStraightWalks++;

            if(direction === "R"){
                direction = "D";
            }
            else if(direction === "D"){
                direction = "L";
            }
            else if(direction === "L"){
                direction = "T"
            }
            else if(direction === "T"){
                direction = "R";
            }
        }

        if(noOfStraightWalks === 2){
            noOfStraightWalks = 0;
            walkStraightFor++;
        }
    }

};

rows = 5;
cols = 6;
rStart = 1;
cStart = 4
var result = spiralMatrixIII(rows, cols, rStart, cStart);
console.log(result);