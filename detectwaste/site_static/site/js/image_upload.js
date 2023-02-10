let userToken;

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
        console.log(data);
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
        console.log(data);
    }).catch((error) => {
        console.error('Error:', error);
    });
});