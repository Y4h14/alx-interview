#!/usr/bin/node
const request = require('request');

function fetchEndpoint(url) {
  return new Promise(function (resolve, reject) {
    request(url, {json: true}, (err, res, body) => {
      if (err) {
        reject(err);
      } else if (res.statusCode !==  200){
          reject(new Error(`Request Failed. status code: ${res.statusCode}`));
      } else {
        resolve (body)
      }
    });
    });
}

const URL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`

fetchEndpoint(URL).then((data) => {
  const peopleLinks = data.characters
  return Promise.all(peopleLinks.map(url => fetchEndpoint(url)));
}).then ((peopleData)=>{
  peopleData.forEach(person => {
    console.log(person.name);
  });
}). catch((error)=> {
  console.error('Error', error)
});




