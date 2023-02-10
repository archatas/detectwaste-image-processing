let userToken, resultsEndpointURL;

document.getElementById('login_form').addEventListener('submit', function(event) {
    event.preventDefault();
    let username = document.getElementById('id_username').value;
    let password = document.getElementById('id_password').value;

    fetch('http://127.0.0.1:8000/api/auth-token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "username": username,
            "password": password,
        })
    }).then( response => {
        return response.json();
    }).then(data => {
        document.getElementById('authentication_response').innerHTML = JSON.stringify(data, null, 2);
        userToken = data.token;
        console.log('Logged in. Got the token.');
    }).catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('image_upload_form').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('id_image');

    let data = new FormData();
    data.append('image', input.files[0]);

    fetch('http://127.0.0.1:8000/api/image-upload/', {
        method: 'POST',
        headers: {
            'Authorization': `Token ${userToken}`
        },
        body: data
    }).then(response => {
        return response.json();
    }).then(data => {
        document.getElementById('upload_response').innerHTML = JSON.stringify(data, null, 2);
        resultsEndpointURL = data.processed_image;
        console.log(data);
    }).catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('processing_form').addEventListener('submit', function(event) {
    event.preventDefault();

    fetch('http://127.0.0.1:8000' + resultsEndpointURL, {
        method: 'GET',
        headers: {
            'Authorization': `Token ${userToken}`
        }
    }).then(response => {
        return response.json();
    }).then(data => {
        document.getElementById('processing_response').innerHTML = JSON.stringify(data, null, 2);
        console.log(data);
    }).catch((error) => {
        console.error('Error:', error);
    });
})