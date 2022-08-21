


let getAPI = () => {
    fetch("https://api.github.com/users/hillarychang")
.then(response => response.json() )
.then(coderData =>{ console.log(coderData) 
    document.getElementById('obj').innerHTML = `<h1> login = ${coderData.login} </h1>`
    document.getElementById('obj').innerHTML += `<img src = ${coderData.avatar_url}>`

}
)
.catch(err => console.log(err) )
}


// function getGithub() {
//     // The await keyword lets js know that it needs to wait until it gets a response back to continue.
//     var response =  fetch("https://api.github.com/users/hillarychang");
//     // We then need to convert the data into JSON format.
//     var coderData = response.json(); 
//         // wait for response to become json
//     return coderData;
// }

// user = getGithub()
// console.log(user)
// console.log("here",user["avatar_url"])
// console.log(getGithub());