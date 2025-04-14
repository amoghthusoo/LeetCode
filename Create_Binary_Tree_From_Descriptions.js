
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */

function inorder(root){

    if(root === null){
        return;
    }

    inorder(root.left);
    console.log(root.val);
    inorder(root.right);
}

var createBinaryTree = function(descriptions) {

    var nodeMap = new Map();
    var childSet = new Set();

    for(var description of descriptions){

        if(nodeMap.has(description[0])){
            var parent = nodeMap.get(description[0]);
        }
        else{
            var parent = new TreeNode(description[0]);
            nodeMap.set(description[0], parent);
        }

        if(nodeMap.has(description[1])){
            var child = nodeMap.get(description[1]);  
            childSet.add(description[1]); 
        }
        else{
            var child = new TreeNode(description[1]);
            nodeMap.set(description[1], child);
            childSet.add(description[1]);
        }

        if(description[2] === 1){
            parent.left = child;
        }
        else{
            parent.right = child;
        }
    }

    for(var description of descriptions){
        if(!childSet.has(description[0])){
            return nodeMap.get(description[0]);
        }
    }

};

var descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]];
var root = createBinaryTree(descriptions);
inorder(root);
