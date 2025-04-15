
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


var calculateDepth = function (root) {

    if (root === null) {
        return 0;
    }

    var queue = [root];
    var depth = 0;

    while (queue.length !== 0) {
        var n = queue.length;
        for (var i = 0; i < n; i++) {

            var node = queue.shift();
            // console.log(node.val);

            if (node.left !== null) {
                queue.push(node.left);
            }

            if (node.right !== null) {
                queue.push(node.right);
            }
        }
        depth++;
        // console.log();
    }

    return depth - 1;
}

var calculateSum = function (root, d) {

    if (root === null) {
        return 0;
    }

    var queue = [root];
    var depth = 0;
    var sum = 0;

    while (queue.length !== 0) {

        var n = queue.length;
        for (var i = 0; i < n; i++) {

            var node = queue.shift();
            
            if(depth === d){
                sum += node.val;
            }

            if (node.left !== null) {
                queue.push(node.left);
            }

            if (node.right !== null) {
                queue.push(node.right);
            }
        }
        depth++;
    }

    return sum;
}

var deepestLeavesSum = function (root) {
    var depth = calculateDepth(root);

    var result = calculateSum(root, depth);
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

var result = deepestLeavesSum(root);
console.log(result);