
//remove
function hide(element) {
    console.log("remove");
    element.remove();
}

//change number of pets when button is clicked
function changePet(id) {
    document.querySelector(id).innerHTML++;
}



//drop down menu alert
const select = document.getElementById('select');
select.addEventListener('change', function handleChange(event) {
    alert("You are looking for a: "+select.options[select.selectedIndex].text);
});



