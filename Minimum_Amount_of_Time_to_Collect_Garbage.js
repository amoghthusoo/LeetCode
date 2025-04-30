/**
 * @param {string[]} garbage
 * @param {number[]} travel
 * @return {number}
 */
var garbageCollection = function (garbage, travel) {

    var infoDict = new Map();
    infoDict.set("M", 0);
    infoDict.set("P", 0);
    infoDict.set("G", 0);
    infoDict.set("MEnd", null);
    infoDict.set("PEnd", null);
    infoDict.set("GEnd", null);

    for (var i = 0; i < garbage.length; i++) {

        for (var j = 0; j < garbage[i].length; j++) {

            if (garbage[i][j] === "M") {
                infoDict.set("M", infoDict.get("M") + 1);
                infoDict.set("MEnd", i);
            }
            else if (garbage[i][j] === "P") {
                infoDict.set("P", infoDict.get("P") + 1);
                infoDict.set("PEnd", i);
            }
            else if (garbage[i][j] === "G") {
                infoDict.set("G", infoDict.get("G") + 1);
                infoDict.set("GEnd", i);
            }
        }
    }

    var totalPickingTime = infoDict.get("M") + infoDict.get("P") + infoDict.get("G"); 

    var totalTravalTime = 0;
    var tempSum = 0;
    for(var i = 0; i < travel.length; i++){
        tempSum += travel[i];

        if(infoDict.get("MEnd") === i + 1){
            totalTravalTime += tempSum;
        }
        
        if(infoDict.get("PEnd") === i + 1){
            totalTravalTime += tempSum;
        }
        
        if(infoDict.get("GEnd") === i + 1){
            totalTravalTime += tempSum;
        }
    }

    var totalTime = totalPickingTime + totalTravalTime;
    
    return totalTime;
};

var garbage = ["MMM","PGM","GP"];
var travel = [3,10];

var result = garbageCollection(garbage, travel);
console.log(result);

// M -> Metal
// P -> Plastic
// G -> Glass
