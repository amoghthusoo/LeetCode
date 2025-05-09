
//   Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {number}
 */

var sum;
function traverse(root){

    if(root === null){
        return 0;
    }

    if(root.val % 2 === 0){

        try{
            sum += root.left.left.val;
        }
        catch{}

        try{
            sum += root.left.right.val;
        }
        catch{}
        
        try{
            sum += root.right.left.val;
        }
        catch{}
        
        try{
            sum += root.right.right.val;
        }
        catch{}
    }

    traverse(root.left);
    traverse(root.right);
}

var sumEvenGrandparent = function (root) {
    sum = 0;
    traverse(root);
    return sum;
};