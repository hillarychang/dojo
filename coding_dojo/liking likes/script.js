var count = 1
var numElement = document.querySelector(".num");

console.log(numElement);

function changeLike() {
    count++;
    numElement.innerText = count + " like(s)";
    console.log(count);
}

var title = document.querySelector("#title");