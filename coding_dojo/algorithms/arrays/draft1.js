
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