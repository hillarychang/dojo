// Reverse
    // // temp=arr[0]
    // // temp2=arr[arr.length-1]
    // // arr[arr.length-1]=temp
    // // arr[0]=temp2

    // // temp=arr[1]
    // // temp2=arr[arr.length-2]
    // // arr[arr.length-2]=temp
    // // arr[1]=temp2

    

    // [0,5,10,15]
    // [0,5,10,0]
    // [15,5,10,0]
    // [15,5,5,0]
    // [15,10,5,0]
    // [15,10,5,0]

// Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
// array – move values within the array that you are given. As always, do not use built-in array functions such as splice().copy
function reverse(arr) {

    for (let i = 0; i < arr.length/2; i++) {
        temp = arr[i]
        temp2=arr[arr.length-1-i]
        arr[arr.length-1-i]=temp
        arr[i]=temp2
        console.log("UGH",arr)
    }

    return arr
    
    }

console.log("ANS", reverse([0,5,10,15])); //[15,10,5,0] 




// Rotate
// Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), 
// change the array to [3,1,2]. Don't use built-in functions.
// Second: allow negative shiftBy (shift L, not R).
// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
// Fourth: minimize the touches of each element.copy

/*

temp = arr[arr.length-1]  //3
temp2 = arr[0] //1
arr[0]=temp //[3 2 3]
temp=arr[arr.length-1-1] //2
arr[1]=temp2 //[3 1 3]
arr[2]=temp //[3 1 2]



temp = arr[arr.length-1-0]  //3
temp2 = arr[i] //1
arr[i]=temp //[3 2 3]

temp=arr[arr.length-1-1] //2
arr[i]=temp2 //[3 1 3]
arr[2]=temp //[3 1 2]


temp=arr[0]  //1
arr[0] = arr[arr.length-1] //[6,2,3,4,5,6]

temp2 = arr[1] //2
arr[1] = temp //[6,1,3,4,5,6]
temp=arr[2] //3
arr[2] = temp2 //[6,1,2,4,5,6]

temp2 = arr[3] //4
arr[3] = temp //[6,1,2,3,5,6]
temp=arr[4] //5
arr[4] = temp2 //[6,1,2,3,4,6]

temp2 = arr[5] //6
arr[5] = temp //[6,1,2,3,4,5]


[1,2,3,4,5,6]
[6,2,3,4,5,6]
[6,1,3,4,5,6]
[6,1,2,4,5,6]
[6,1,2,3,5,6]
[6,1,2,3,4,6]
[6,1,2,3,4,5]


[1,2,3]
[3,2,3]
[3,1,3]
[3,1,2]
*/
// ([1,2,3],1) ->  [3,1,2]


/*
temp=arr[0]  //1
arr[0] = arr[arr.length-1] //[6,2,3,4,5,6]

temp2 = arr[1] //2
arr[1] = temp //[6,1,3,4,5,6]
temp=arr[2] //3
arr[2] = temp2 //[6,1,2,4,5,6]

temp2 = arr[3] //4
arr[3] = temp //[6,1,2,3,5,6]
temp=arr[4] //5
arr[4] = temp2 //[6,1,2,3,4,6]

temp2 = arr[5] //6
arr[5] = temp //[6,1,2,3,4,5]
*/


function rotate(arr, value) {

    for (let num = 0; num < value; num++) {

    for (let i = 0; i < arr.length; i+=2) {
        if (i==0){
            temp = arr[i];
            arr[0] = arr[arr.length-1];
            i--;
            console.log("HERE",arr, "idx ",i);
            continue;
        }
        else if (i == arr.length-1){
            temp2 = arr[i] //6
            arr[i] = temp //[6,1,2,3,4,5]
            break; 
        }
        temp2 = arr[i] //2
        arr[i] = temp //[6,1,3,4,5,6]
        temp=arr[i+1] //3
        arr[i+1] = temp2 //[6,1,2,4,5,6]
        console.log("ALRIGHT",arr, "idx ",i);
    }        
    
    }

    return arr
    
    }
    
    console.log("ROTATE",rotate([0,5,10,15],3)); //8 0 5 10 15
    // console.log("ROTATE",rotate([3,1,2])); //8 0 5 10 15
    // console.log("ROTATE",rotate([1, 2, 3, 4, 5, 6, 7, 8])); //8 0 5 10 15
    // console.log("ROTATE",rotate([8, 1, 2, 3, 4, 5, 6, 7])); //8 0 5 10 15
    



// Filter Range
// Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.copy
function filter(arr, min, max) {

    console.log("*arr",arr)
    console.log("*mi",min)
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max || arr[i]<min){
            console.log("max",max, "min", min, "arr[i]",arr[i]);
            console.log("P",arr, "i ", i, "element ",arr[i])
            removeAt(arr,i);
            i--;
            continue;            
        }
        else{
            console.log("N",arr, "i ", i, "element ",arr[i])
            continue;            
        }
    }

    return arr
    
    }

console.log("UIHKHB", filter([0,5,10,15],6,100)); //[15,10,5,0] 

function removeAt(arr, idx) {

    for (let i = idx; i < arr.length; i++) {
        temp = arr[i+1]
        arr[i] = temp
    }

    let length = arr.length
    arr.length = length-1;
    
    return arr
    
    }



// Concat
// Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].
function concat(arr, arr2) {

    let newarry = [];
    for (let i = 0; i < arr.length; i++) {
        newarry[i]=arr[i];
    }

    for (let j = 0; j < arr2.length; j++) {
        newarry[arr.length+j]=arr[j];
    }
    
    return newarry
    
    }
    console.log("concat", concat([0,5,10,15],[0,5,10,15]) ); //[15,10,5,0] 
