/*
for (let i =0; i<arr.length; i++){
    if (arr[i]==number){
        return true;
    }
    return false;
}
*/
// Recursive Binary Search
// Given a sorted array and a value, recursively determine whether value is found within array. 


function rBinarySearch(arr, val) {

    console.log("num_times",arr);

    if (val === arr[0]) {
		return true;
    }

    if (arr.length == 1){
        return false
    }

    /*
[1,3,5,6]
[3,5,6]
[5,6]
[6]

    [1,3,5,6],4
*/


    return rBinarySearch(arr.slice(1, arr.length), val)

}



// function rBinarySearch(arr, val) {

//     if (val === arr[i]) {
// 		return true;
// 	} else if (arr == null) {
//         return false;
//     }
//     else {
//         rBinarySearch(arr++, val)
//     }
// 	// if (val === arr.length) {
// 	// 	return false;
// 	// }


//     // return (rBinarySearch(arr,val));
// }

// function loopArray(arr){

//         return arr[i];
//         return (loopArray(arr, i++));
// }

console.log("HERE",rBinarySearch([4,5,6,8,12],5)) //= false; 
console.log("HERE",rBinarySearch([1,3,5,6],4)) //= false; 

// rBinarySearch([4,5,6,8,12],5) = true.



// Greatest Common Factor
// Given two integers, create rGCF(num1,num2) to recursively determine Greatest Common Factor (the largest integer dividing evenly into both). Greek mathematician Euclid demonstrated these facts:

// gcf(a,b) == a, if a == b;
// gcf(a,b) == gcf(a-b,b), if a>b;
// gcf(a,b) == gcf(a,b-a), if b>a.
// Second: rework facts #2 and #3 to reduce stack consumption and expand rGCF’s reach. You should  be able to compute rGCF(123456,987654).
function rGCF(a, b) {

    if (a === b) {
		return a;
    }

    if (a > b){
        return rGCF(a-b, b);    
    }


    if (b > a){
        return rGCF(a, b-a);
    }


    if (a==1 || b ==1){
        return 1;
    }

}

/*
7,5
2,5
2,3
2,1
1,1
return 1

6,4
2,4
2,2
return 2

3,1
2,1
1,1
return 2
*/

console.log("rGCF",rGCF(40,15));
console.log("rGCF",rGCF(6,4));
console.log("rGCF",rGCF(123456,987654)); //answer is 4
/*
function GCF(a, b) {

a_arr = [];
b_arr = [];
both = [];
divisible_both =[];


for (let i=0 ; i< a; i++){ //factors of a
    if (a % i ==0){
        a_arr.push(i); 
    }
}


for (let i=0 ; i< b; i++){ //factors of b
    if (b % i ==0){
        b_arr.push(i);
    }
}

both = a_arr.concat(b_arr); 

for (let i=0 ; i< both; i++){ //if both are divisible by arr
    if (b % i ==0 && a % i ==0){
        divisible_both.push(i);
    }
}

ans = Math.max(divisible_both);

return ans;

}

*/



    /*
[1,3,5,6]
[3,5,6]
[5,6]
[6]

    [1,3,5,6],4
*/

