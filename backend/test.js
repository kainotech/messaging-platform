// const params = {
//     "number": "0701613315",
//     "message": "Hi there" 
// };
// const options = {
//     method: 'POST',
//     body: JSON.stringify( params )  
// };
// fetch( 'http://127.0.0.1:8000/sendMessageDialog/', options )
//     .then( response => response.json() )
//     .then( response => {
//         // Do something with response.
//     } );

fetch('http://127.0.0.1:8000/sendMessageDialog/?number=0701613315&message=hi%20there', {
    method: 'POST',
    headers: {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }
});