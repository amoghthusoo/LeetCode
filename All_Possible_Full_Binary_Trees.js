
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {number} n
 * @return {TreeNode[]}
 */

function contructTrees(n){

    if(n === 1){
        var tempNode = new TreeNode(0);
        return [tempNode]
    }

    // var tempNode = new TreeNode(0);
    n--;

    var possibleBifurcations = [];
    for(var i = 1; i < n; i += 2){
        possibleBifurcations.push([i, n - i]);
    }

    var possibleTrees = [];

    for(var bifr of possibleBifurcations){
        var leftTrees = contructTrees(bifr[0]);
        var rightTrees = contructTrees(bifr[1]);

        for(var rootLeft of leftTrees){
            for(var rootRight of rightTrees){
                
                var tempNode = new TreeNode(0);
                tempNode.left = rootLeft;
                tempNode.right = rootRight;
                possibleTrees.push(tempNode);
            
            }
        }
    }

    return possibleTrees;
}

var allPossibleFBT = function (n) {

    if(n % 2 === 0){
        return [];
    }

    return contructTrees(n);
};

var result = allPossibleFBT(5);
console.log(result);