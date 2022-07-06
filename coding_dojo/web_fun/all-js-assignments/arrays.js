function alwaysHungry(arr) {
    var y=0;
    for (var i=0;i<arr.length;i++){
        if (arr[i]=="food") {
            y++;
            console.log("yummy");
       }
    }
    if (y==0){
        console.log("I'm hungry");
    }
}
   
alwaysHungry([3.14, "food", "pie", true, "food"]);
// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"




function highPass(arr, cutoff) {
    var filteredArr = [];
    for (var i=0;i<arr.length;i++){
        if (arr[i]>cutoff){
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // we expect back [6, 8, 10, 9]



function betterThanAverage(arr) {
    var sum = 0, avg = 0;
    // calculate the average
    for (var i=0;i<arr.length;i++){
        sum+=arr[i];
    }
    avg = (sum)/arr.length;
    var count = 0
    // count how many values are greated than the average
    for (var k=0;k<arr.length;k++){
        if (avg< arr[k]){
            count++;
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4




function reverse(arr) {
    // your code here
    var temp = [];
    for (var i=arr.length-1;i>=0;i--){
        temp.push(arr[i]);
    }
    return temp;
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]



function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    // your code here
    var fterm =0;
    var sterm =1;
    var newTerm = 0;


    while (n>0){


    newTerm = fibArr[fterm] + fibArr[sterm]
    fterm++;
    sterm++;

    fibArr.push(newTerm);
    n--;

}

    return fibArr;
}
   
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
