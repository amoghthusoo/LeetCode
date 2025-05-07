/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var diagonalSort = function(mat) {
    
    var map = new Map();
    var start_indices = new Map();

    for(var i = 0; i < mat.length; i++){
        for(var j = 0; j < mat[0].length; j++){
            if(!map.has(i - j)){
                map.set(i - j, []);
                start_indices.set(i - j, [i, j]);
            }
            var temp_arr = map.get(i - j);
            temp_arr.push(mat[i][j]);
            map.set(i - j, temp_arr);
        }
    }
    for(var key of map.keys()){
        temp_arr = map.get(key);
        temp_arr.sort((a, b) => a - b);
        map.set(key, temp_arr);
    }
    
    // console.log(map);
    // console.log(start_indices);

    var i, j, k, tempArr;
    for(var key of map.keys()){
        [i, j] = start_indices.get(key);
        tempArr = map.get(key);
        k = 0;
        while(k < tempArr.length){
            mat[i][j] = tempArr[k];
            i++;
            j++;
            k++;
        }  
    }

    return mat;
};

var mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]];
var result = diagonalSort(mat);
console.log(result);