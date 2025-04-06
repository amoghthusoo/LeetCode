/**
 * @param {string} pattern
 * @return {string}
 */

function getPermutation(s, sLen = null, pattern = null) {

    if (s.length === 1) {
        return s;
    }

    var permutations = [];

    for (var i = 0; i < s.length; i++) {

        var ch = s[i];
        var remainingStr = s.slice(0, i) + s.slice(i + 1, s.length);

        var interPermutations = getPermutation(remainingStr);
        for (var j = 0; j < interPermutations.length; j++) {
            var possibleResult = ch + interPermutations[j];
            permutations.push(possibleResult)

            if (possibleResult.length === sLen) {

                for (var k = 0; k < pattern.length; k++) {

                    if (pattern[k] === "I" && possibleResult[k + 1] < possibleResult[k]) {
                        break;
                    }
                    else if (pattern[k] === "D" && possibleResult[k + 1] > possibleResult[k]) {
                        break;
                    }

                    if (k == pattern.length - 1) {
                        return possibleResult;
                    }
                }
            }
        }
    }
    return permutations;
}

var smallestNumber = function (pattern) {

    var n = pattern.length;
    var digits = "123456789";
    var initialStr = digits.slice(0, n + 1);

    return getPermutation(initialStr, initialStr.length, pattern);
}

console.time();
var pattern = "IIIDIDDD";
var result = smallestNumber(pattern);
console.log(result);
console.timeEnd();