
//remove
function hide(element) {
    console.log("remove");
    element.remove();
}


//drop down menu 
function changeTEMP() {
    var x = document.getElementById("select").value;
    console.log("HERE", x);

    var className = "";
    if (x=='C'){
        for (var i=1; i<5;i++){
            className = "high"+i;
            changeFtoC(className);
        }

        for (var i=1; i<5;i++){
            className = "low"+i;
            changeFtoC(className);
        }
    }
    else{
        for (var i=1; i<5;i++){
            className = "high"+i;
            changeCtoF(className);
        }

        for (var i=1; i<5;i++){
            className = "low"+i;
            changeCtoF(className);
        }
    }
    // console.log(document.getElementsByClassName("high1").innerHTML);
  }

  //document.getElementsByClassName("high1").innerHTML = "You selected: " + x;


function  changeFtoC(name){
    console.log("name",name);
    var val, newVal;
    val = document.querySelector("."+name).innerHTML;
    // val = document.getElementsByClassName(name).innerHTML;
    console.log("val",val);
    newVal = (val - 32 ) * (5/9);
    document.querySelector("."+name).innerHTML = Math.round(newVal);
}

function  changeCtoF(name){
    console.log("name",name);
    var val, newVal;
    val = document.querySelector("."+name).innerHTML;
    // val = document.getElementsByClassName(name).innerHTML;
    console.log("val",val);
    newVal = (val * 9/5 ) + 32;
    document.querySelector("."+name).innerHTML = Math.round(newVal);
}

// function changeTemp(element) {

//     var temp1 = document.querySelector('.high1').innerHTML;
//     var temp2 = document.querySelector('.low1').innerHTML;
//     console.log("temp",temp1);

//     console.log("element",element.innerHTML);
//     if (element.innerHTML == 'C'){
//         console.log("C");

//         temp1 = temp1 + 1;

//         // document.querySelector(id).innerHTML++;

//     }
//     else{

//     }
//     // document.querySelector(id).innerHTML = ;
// }



// changeTemp(.row1);


//dropdown menu

/*
function dropDown(id){
    const select = document.getElementById(id);
    select.addEventListener('change', function handleChange(event) {
    console.log();
    });
}

dropDown("script");
*/

/*const select = document.getElementById('select');
select.addEventListener('change', function handleChange(event) {
    alert("You are looking for a: "+select.options[select.selectedIndex].text);
});
*/
