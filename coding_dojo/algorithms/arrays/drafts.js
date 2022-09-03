
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

    //[15 0 5 10]



    
/*
// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!
function insertAt(arr, idx, value) {
    // [100,200,5 ]
    // [100,200,311 ]
    // [100,200,311,5 ]
    
    let length = arr.length;
    let temp = 0;
    arr.length = length+1;
    
    for (let i = idx; i < (arr.length-1); i++) {
    
        if (i==idx){
    
        temp=arr[i];
        temp2 = arr[i+1];
        arr[i]=value;
        continue;
        }
        else if (i == arr.length-1){
            arr[arr.length-1]=temp2;  
            break; 
        }
    
        arr[i]=temp //i=[3]
        temp = arr[i+1] //[4]
        arr[i+1]=temp2;  
        temp2 = arr[i+2]; //[5]
        console.log("arr", arr, " index", i)
    
    
    
        // temp = arr[2]; temp=2
        //     temp2 = arr[3]; temp2=3
        //     arr[2]=value; [5,7,8,3,6,0]
        //     arr[3]=temp  [5,7,8,2,6,0]
        //     temp = arr[4] temp = 6
        //     arr[4]=temp2  [5,7,8,2,3,0]
        //     temp2 = arr[5]; temp2=0
        //     arr[5]=temp; [5,7,8,2,3,6]
        //     arr[6]=temp2  [5,7,8,2,3,6 0]
    
    
    }


    return arr;
    }

console.log(insertAt([100,200,5], 2, 311)); //[100,200,311,5]
console.log(insertAt([5,7,2,3,6,0], 2, 8));
*/

/*
function removeAt(arr, idx) {

    for (let i = idx; i < arr.length; i++) {
        temp = arr[i+1]
        arr[i] = temp
    }

    let length = arr.length
    arr.length = length-1;
    
    return arr
    
    }

//console.log(removeAt([1000,3,204,77], 1)); // [1000,204,77]  





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
//console.log(swapPairs([1,2,3,4])); // [1000,204,77]  



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
*/
    /*
    [-2,-2,3.14,5,5,10]
    [_,-2,3.14,5,5,10]

    */