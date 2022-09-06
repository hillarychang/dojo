

// import math;
// Recursive Sigma
// Write a recursive function that given a number returns the sum of integers from 1 to that number. Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.

// count = num;
// for (let i =0 ; i<count; i++){

//     sum+=i;

// }

function rSigma(number) {

    number = Math.floor(number);


    if (number < 0) {
        return 0;
    }
    /* negative?? doesn't work
	if (number < 0) {
        if (number === 1) {
            return 1;
        }
    
    return (number+rSigma(number + 1))	    
    }
    */


	if (number === 0) {
		return 0;
	}
    return (number+rSigma(number - 1));
}




console.log("rSigma ",rSigma(5));
rSigma(2);
console.log("2.5 rSigma ",rSigma(2.5));
console.log("rSigma ",rSigma(-3)); //-3, -2,-1


// 
// Recursive Factorial
// Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).
function rFact(number) {

    number = Math.floor(number);



	if (number === 1) {
		return 1;
	}

    console.log("HERE",number);


    return (number*rFact(number - 1));
}




console.log("rFact ",rFact(3));



// //Flood Fill
// Replace a pixel’s color value only if it is the same color as the origin coordinate and is directly adjacent via X or Y to another pixel you will change.

function floodFill(canvas2D,startXY,newColor){

    number = Math.floor(number);



	if (number === 1) {
		return 1;
	}

    console.log("HERE",number);


    return (number*floodFill(number - 1));
}




console.log("floodFill ",floodFill([[3,2,3,4,3],[2,3,3,4,0],[7,3,3,5,3],[6,5,3,4,1],[1,2,3,3,3]], [2,2], 1));

