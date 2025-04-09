
//  Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @return {number}
 */

var sum, count;

var calculateSumCount = function (root) {

    if (root === null) {
        return;
    }

    sum += root.val;
    count++;
    calculateSumCount(root.left, sum, count);
    calculateSumCount(root.right, sum, count);

}

var result;
var traverse = function(root){

    if(root === null){
        return;
    }

    sum = 0;
    count = 0;
    calculateSumCount(root);

    if(Math.floor(sum/count) === root.val){
        result++;
    } 

    traverse(root.left);
    traverse(root.right);
}

var averageOfSubtree = function (root) {
    result = 0;
    traverse(root);
    return result;
};

var root = new TreeNode(
    4,
    new TreeNode(
        8,
        new TreeNode(0),
        new TreeNode(1)
    ),
    new TreeNode(
        5,
        null,
        new TreeNode(6)
    )
);

var output = averageOfSubtree(root);
console.log(output);