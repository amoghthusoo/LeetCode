/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    
    var i = 0;
    var j = 0;

    var path_stack = [i];
    var index_stack = [j];
    var result_set = new Set();
    var result = [];
    while(path_stack.length != 0){

        i = path_stack[path_stack.length - 1];
        j = index_stack[index_stack.length - 1];

        if(i == graph.length - 1){

            if(!result_set.has(path_stack.toString())){
                result_set.add(path_stack.toString());
                result.push([...path_stack]);
            }
        }

        if(j == graph[i].length){
            path_stack.pop();
            index_stack.pop();
        }
        else{
            index_stack[index_stack.length - 1]++;
            path_stack.push(graph[i][j]);
            index_stack.push(0);
        }
    }

    return result;
};

graph = [[2],[],[1]]
var result = allPathsSourceTarget(graph);
console.log(result);