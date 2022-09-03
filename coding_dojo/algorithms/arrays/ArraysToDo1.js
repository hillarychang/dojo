

// Push Front: Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!


//OTHER WAY
    // temp=arr[0] 0
    // temp2 = arr[1] 5
    // arr[1]=temp [0 0 10 15]   
    // temp=arr[2] 10
    // arr[2]=temp2 7 [0 0 5 15 ]
    // temp2 = arr[3] 15 
    // arr[3]=temp [0 0 5 10 ] 
    // arr[4]=temp2 [0 0 5 10 15]  


/*
i=1 [0,0,5,15 ]
i=2 [0,0,5,10 ]
i=3 [0,0,5,10 15]
*/
function pushFrontSimple(arr, value) {
    let length = arr.length;
    arr.length = length+1;

    for (let i = arr.length-1; i > 0; i--) {
        arr[i]=arr[i-1]
    }

    arr[0] = value;

    return arr

}
console.log(pushFrontSimple([0,5,10,15], 8)); //8 0 5 10 15


function pushFront(arr, value) {

let length = arr.length;
let temp = 0;
arr.length = length+1;


for (let i = 0; i < arr.length; i+=2) {

    if (i==0){
        temp = arr[i];
        temp2 = arr[i+1];
        arr[i+1]=temp;
        console.log("HERE",arr)
        continue;
    }
    else if (i == arr.length-1){
        console.log("this", arr)
        arr[i]=temp2;
        break; 
    }

    temp = arr[i];
    arr[i]=temp2;
    temp2 = arr[i+1];
    arr[i+1]=temp 
    console.log("arr", arr, " index", i)

}

    arr[0] = value

return arr

}

console.log(pushFront([0,5,10,15], 8)); //8 0 5 10 15
console.log(pushFront([5,7,2,3], 8)); 
console.log(pushFront([99], 7)); 




// Pop Front
// Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!
    // [0,5,10,15]
    // [5,5,10,15]
    // [5,10,15,15]
function popFront(arr) {

    for (let i = 0; i < arr.length; i++) {
        temp = arr[i+1]
        arr[i] = temp
    }

    let length = arr.length
    arr.length = length-1;
    
    return arr
    
    }

console.log(popFront([0,5,10,15])); //[5,10,15] 


// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!

function insertAt(arr, idx, value) {

    let length = arr.length;
    let temp = 0;
    arr.length = length+1;
    
    
    for (let i = idx; i < arr.length; i+=2) {
    
        if (i==idx){
            temp = arr[i];
            temp2 = arr[i+1];
            arr[i+1]=temp;
            console.log("HERE",arr)
            continue;
        }
        else if (i == arr.length-1){
            console.log("this", arr)
            arr[i]=temp2;
            break; 
        }
    
        temp = arr[i];
        arr[i]=temp2;
        temp2 = arr[i+1];
        arr[i+1]=temp 
        console.log("arr", arr, " index", i)
    
    }
    
        arr[idx] = value
    
    return arr
    
    }


    console.log(insertAt([5,7,2,3,6,0], 2, 8));
    console.log(insertAt([100,200,5], 2, 311));





    
// BONUS: Remove At
// Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).
function removeAt(arr, idx) {

    for (let i = idx; i < arr.length; i++) {
        temp = arr[i+1]
        arr[i] = temp
    }

    let length = arr.length
    arr.length = length-1;
    
    return arr
    
    }

console.log(removeAt([1000,3,204,77], 1)); // [1000,204,77]  


// // BONUS: Swap Pairs
// Swap positions of successive pairs of values of given array. If length is odd, do not change the final element.
function swapPairs(arr) {

    if (arr.length % 2 ==0){
        for (let i = 0; i < arr.length; i+=2) {
            temp = arr[i];
            temp2 = arr[i+1];
            arr[i] = temp2;
            arr[i+1]=temp;
        }
    }
    else{
        for (let i = 0; i < arr.length-1; i+=2) {
            temp = arr[i];
            temp2 = arr[i+1];
            arr[i] = temp2;
            arr[i+1]=temp;
        }    
    }

    return arr
    
    }

    console.log(swapPairs([1,2,3,4])) //[2,1,4,3]


// BONUS: Remove Duplicates
function removeDupes(arr) {

    for (let i = 0; i < arr.length; i++) {
        for (let j = i+1; j < arr.length; j++) {
        
            if (arr[i]==arr[j]){
                removeAt(arr,i);
            }

        }
    }
    
    return arr
    
    }

    console.log(removeDupes([-2,-2,3.14,5,5,10])) //[-2,3.14,5,10]
