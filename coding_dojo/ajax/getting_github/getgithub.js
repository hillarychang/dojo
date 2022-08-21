

async function getGithub() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://api.github.com/users/hillarychang");
    // We then need to convert the data into JSON format.
    var coderData = await response.json();
    return coderData;
}
    
console.log(getCoderData());