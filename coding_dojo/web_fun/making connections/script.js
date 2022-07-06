function changeName(id)
{
    document.querySelector(id).innerText = "New Name";   
    console.log("edit profile");
}



function removeThing(id)
{    
    console.log("id", id);

    document.querySelector(id).style.display = "none";
    // var elem = document.getElementsByClassName(id);
    // console.log("elem", elem);
   //* document.getElementsByClassName(id).style.display = "none";
    // style.display = "none";
    
    
    // document.querySelector(id);
    // console.log("here", document.querySelector(id));
    console.log("remove");
}


    