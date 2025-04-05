
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */

var nodes;

function traverse(root) {

    if (root === null) {
        return;
    }

    traverse(root.left);
    nodes.push(root.val);
    // console.log(root.val);
    traverse(root.right);
}

function insert(root, value) {

    if (root === null) {
        var temp = new TreeNode(value);
        root = temp;
    }

    else if (value <= root.val && root.left === null) {
        var temp = new TreeNode(value);
        root.left = temp;
    }
    else if (value <= root.val && root.left !== null) {
        insert(root.left, value);
    }
    else if (value > root.val && root.right === null) {
        var temp = new TreeNode(value);
        root.right = temp;
    }
    else if (value > root.val && root.right !== null) {
        insert(root.right, value);
    }
    
    return root;
}

function buildTree(root, nodes){

    if(nodes.length === 0){
        return root;
    }

    if (nodes.length % 2 === 0) {
        var middle = (nodes.length / 2) - 1;
    }
    else {
        var middle = (nodes.length - 1) / 2;
    }

    var leftNodes = nodes.slice(0, middle);
    var rightNodes = nodes.slice(middle + 1, nodes.length);
    root = insert(root, nodes[middle]);

    root.left = buildTree(root.left, leftNodes);
    root.right = buildTree(root.right, rightNodes);

    return root;
}

var balanceBST = function (root) {
    nodes = [];
    traverse(root);
    root = null;
    root = buildTree(root, nodes);
    return root;
};
