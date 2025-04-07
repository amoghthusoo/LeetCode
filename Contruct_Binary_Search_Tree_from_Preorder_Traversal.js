
// Definition for a binary tree node.

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
 
/**
 * @param {number[]} preorder
 * @return {TreeNode}
 */

function constructTree(preorder, inorder){

    if(inorder.length === 0){
        return [null, preorder];
    }

    var root = preorder.shift();

    var temp = new TreeNode(root);

    var index = inorder.indexOf(root);
    var left = inorder.slice(0, index);
    var right = inorder.slice(index + 1, inorder.length);

    [temp.left, preorder] = constructTree(preorder, left);
    [temp.right, preorder] = constructTree(preorder, right);

    return [temp, preorder];

}

var bstFromPreorder = function(preorder) {

    var inorder = [...preorder].sort((a, b) => a - b);
    var [root, preorder] = constructTree(preorder, inorder);
    return root;
};

var preorder = [8,5,1,7,10,12]
var root = bstFromPreorder(preorder);