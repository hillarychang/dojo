// Remove Blanks
// Create a function that, given a string, returns all of that string’s contents, but without blanks. 

function removeBlanks(str) {

    let newstr = "";

    for (let i = 0; i < str.length; i++) {
        if (str[i] == " "){
        continue;
        }
        newstr += str[i];

    }

    console.log("WHAT",newstr);
    return newstr;
    
    }

console.log("HERE ",removeBlanks(" Pl ayTha tF u nkyM usi c ")); // "PlayThatFunkyMusic"
removeBlanks("I can not BELIEVE it's not BUTTER") // "IcannotBELIEVEit'snotBUTTER"



// Get Digits
// Create a JavaScript function that given a string, returns the integer made from the string’s digits. You are allowed to use isNaN() and Number().

function getDigits(str) {

    let newstr = "";

    for (let i = 0; i < str.length; i++) {
        if (isNaN(Number(str[i]))){ //is Nan means str[i] is string
        continue;
        }
        newstr += str[i];

    }
    return Number(newstr);
    
    }

console.log(getDigits("abc8c0d1ngd0j0!8"))   //801008
getDigits("0s1a3y5w7h9a2t4?6!8?0") //1357924680





// Acronyms
// Create a function that, given a string, returns the string’s acronym (first letter of the word capitalized). You are allowed to use .split() and .toUpperCase().
function acronym(str) {

    let newstr = "";
    words = str.split(' ');
    console.log("words",words);
    console.log("?",words[0]);
    for (let i = 0; i < words.length; i++) {

        if (typeof words[i][0] == 'undefined') {

        // if (str[i] == "" || str[i] == undefined){
            console.log("undefined",words[i][0]);

            continue;
        }

        console.log("case ",words[i][0], "typeof", );
        // if (words[i][0]){
        // }
        // newword = toUpperCase();
        newstr+= words[i][0].toUpperCase();
        console.log("stringans ",newstr,"idx ",i);


    }

    // newstr.toUpperCase();

    console.log("newstr ",newstr);
    return newstr;
    
    }


console.log("*****",acronym("there's no free lunch - gotta pay yer way. ")); //=> "TNFL-GPYW". 
acronym("Live from New York, it's Saturday Night!") //=> "LFNYISN".


// Count Non-Spaces
// Create a function that, given a string, returns the number of non-space characters found in the string. 
function countNonSpaces(str) {
    let num = 0;

    for (let i = 0; i < str.length; i++) {
        if(str[i]!=" "){
            num++;
        }
    }

    console.log("CONSOLE",num);
    return num;
    
    }


console.log(countNonSpaces("Honey pie, you are driving me crazy"));
countNonSpaces("Hello world !");



// Remove Shorter Strings
// Create a function that, given an array of strings and a numerical value, returns an array that only contains strings longer than or equal to the given value.
function removeShorterStrings(arr, val) {

    let newstr = "";
    let count = 0;
    let newarr = [];

    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[i].length; j++) {
            count++
            console.log("count",count);

        }

        if (count >= val){
            newarr.push(arr[i]);
        }

        count=0;

    }

    console.log("WHAT",newarr);
    return newarr;
    
    }

console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)) //=> ['Good morning', 'sunshine', 'Earth', 'says', 'hello']
removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3) //=> ['There', 'bug', 'the', 'system']