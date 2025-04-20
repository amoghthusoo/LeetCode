
// Definition for a binary tree node.

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 */

var elements;

function recover(root){
    
    if(root === null){
        return;
    }

    if(root.left !== null){
        root.left.val = 2 * root.val + 1;
        elements.add(root.left.val);
    }
    if(root.right !== null){
        root.right.val = 2 * root.val + 2;
        elements.add(root.right.val);
    }

    recover(root.left);
    recover(root.right);
}

var FindElements = function(root) {
    elements = new Set();
    root.val = 0;
    elements.add(root.val);
    recover(root);
    this.root = root;
};

/** 
 * @param {number} target
 * @return {boolean}
 */

FindElements.prototype.find = function(target) {
    
    if(elements.has(target)){
        return true;
    }
    else{
        return false;
    }
};

/** 
 * Your FindElements object will be instantiated and called as such:
 * var obj = new FindElements(root)
 * var param_1 = obj.find(target)
 */