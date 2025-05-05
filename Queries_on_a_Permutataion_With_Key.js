/**
 * @param {number[]} queries
 * @param {number} m
 * @return {number[]}
 */
var processQueries = function(queries, m) {
    
    var P = [];
    for(var i = 1; i <= m; i++){
        P.push(i);
    }

    var result = [];

    for(var i = 0; i < queries.length; i++){
        var index = P.indexOf(queries[i]);
        result.push(index);
        var [deleted] = P.splice(index, 1);
        P.unshift(deleted);
    }

    return result;
};

queries = [7,5,5,8,3];
m = 8;
var result = processQueries(queries, m);
console.log(result)