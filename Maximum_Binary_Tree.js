
//  Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */

function constructTree(vals){

    if(vals.length === 0){
        return null;
    }

    var max = Math.max(...vals);
    var maxIndex = vals.indexOf(max);
    var leftVals = vals.slice(0, maxIndex);
    var rightVals = vals.slice(maxIndex + 1, vals.length);

    var tempNode = new TreeNode(max);
    tempNode.left = constructTree(leftVals);
    tempNode.right = constructTree(rightVals);

    return tempNode;

}

var constructMaximumBinaryTree = function (nums) {  

    return constructTree(nums);
};

var arr = [1, 2, 3];
console.log(arr.indexOf(2));