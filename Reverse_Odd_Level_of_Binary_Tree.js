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

// var inorder = function (root) {
//     if (root === null) {
//         return
//     }

//     inorder(root.left);
//     console.log(root.val);
//     inorder(root.right);
// }

var reverse = function (tempValArr, tempObjArr) {

    for (var i = 0; i < tempValArr.length; i++) {
        tempObjArr[i].val = tempValArr[i];
    }

}

var tempValArr = [];
var tempObjArr = [];
var count = 0;
var power = 0;
var queue = [];
var initialCase = true;

var bfs = function (root) {

    if (queue.length === 0 && !initialCase) {
        tempValArr = [];
        tempObjArr = [];
        count = 0;
        power = 0;
        queue = [];
        initialCase = true;
        return;
    }

    if (initialCase) {
        initialCase = false;
        power++;

        if (root.left !== null) {
            queue.push(root.left);
        }

        if (root.right !== null) {
            queue.push(root.right);
        }

        bfs(null);
    }

    else {
        root = queue.shift();


        if (power % 2 === 1) {
            tempValArr.unshift(root.val);
            tempObjArr.push(root);
        }

        count++;

        if (count === 2 ** power) {

            if (power % 2 === 1) {
                reverse(tempValArr, tempObjArr);
                tempValArr = [];
                tempObjArr = [];
            }
            power++;
            count = 0;
        }

        if (root.left !== null) {
            queue.push(root.left);
        }

        if (root.right !== null) {
            queue.push(root.right);
        }
        bfs(null);
    }
}

var reverseOddLevels = function (root) {

    bfs(root);
    return root;
};

var root = new TreeNode(
    7,
    new TreeNode(
        13,
        null,
        null
    ),
    new TreeNode(
        11,
        null,
        null
    )
);


// inorder(root);
// bfs(root);
// console.log();
// inorder(root);

console.log(root);
var root = reverseOddLevels(root);
console.log(root);