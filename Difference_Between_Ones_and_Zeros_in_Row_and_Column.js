/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var onesMinusZeros = function(grid) {

    var onesInRows = new Map();
    var onesInColumns = new Map();

    for(var i = 0; i < grid.length; i++){
        for(var j = 0; j < grid[0].length; j++){
            if(grid[i][j] === 1){
                if(onesInRows.has(i)){
                    onesInRows.set(i , onesInRows.get(i) + 1);
                }
                else{
                    onesInRows.set(i , 1);
                }

                if(onesInColumns.has(j)){
                    onesInColumns.set(j, onesInColumns.get(j) + 1);
                }
                else{
                    onesInColumns.set(j, 1);
                }
            }
            else{
                if(!onesInRows.has(i)){
                    onesInRows.set(i, 0);
                }
                if(!onesInColumns.has(j)){
                    onesInColumns.set(j, 0);
                }
            }

        }
    }

    var result = [];
    var n = grid.length;
    var m = grid[0].length;

    for(var i = 0; i < n; i++){
        var temp = [];
        for(var j = 0; j < m; j++){
            temp.push(onesInRows.get(i) + onesInColumns.get(j) - (n - onesInRows.get(i)) - (m - onesInColumns.get(j)));        
        }
        result.push(temp);
    }
    
    return result;
};

var grid = [[0]];
var result = onesMinusZeros(grid);
console.log(result);