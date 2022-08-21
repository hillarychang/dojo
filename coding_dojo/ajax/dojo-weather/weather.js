


let getWeather = () => {
    fetch("http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&APPID=97bd75684cc7cf194dc007851d337d78")
    // Make sure to put your unique API key in the URL (taking out the brackets).
    // &APPID={INSERTAPIKEY} will need to be at the end of each URL you access below and in the assignment.
    .then(response => response.json() )
    .then(coderData =>{ console.log(coderData) 
        document.getElementById('obj').innerHTML = `<h1> login = ${coderData} </h1>`
        // document.getElementById('obj').innerHTML += `<img src = ${coderData.}>`

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