/**
 * @param {number} n
 * @return {number}
 */

function getPartitions(s) {

    if (s.length === 0) {
        return [[]];
    }
    else if (s.length === 1) {
        return [[s]];
    }

    var partitions = [];

    for (var i = 0; i < s.length; i++) {
        var prefix = s.slice(0, i + 1);
        var suffix = s.slice(i + 1, s.length);

        var tempPartitions = getPartitions(suffix);

        for (var part of tempPartitions) {
            part.unshift(prefix);
            partitions.push(part);
        }
    }

    return partitions;
}

function isValid(partitions, n) {

    var sum;
    for (var part of partitions) {
        sum = 0;
        for (var substring of part) {
            sum += Number.parseInt(substring);
        }
        if (sum === n) {
            return true;
        }
    }
    return false;
}

var punishmentNumber = function (n) {

    var count = 0;

    for (var i = 1; i <= n; i++) {

        var squared = i ** 2;
        var partitions = getPartitions(squared.toString());

        if (isValid(partitions, i)) {
            count += squared;
        }
    }

    return count;
};

n = 37;
var result = punishmentNumber(n);
console.log(result);

// console.log(getPartitions("100"));