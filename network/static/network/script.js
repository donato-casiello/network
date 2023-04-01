document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#create').addEventListener('click', showNew);
    })


// Show the new post form
function showNew() {
    document.querySelector('#new').style.display = 'block';
}

function followUser(id) {
        console.log(id);
        fetch(`/follow/${id}`,{
            method : "POST",
            headers : {"Content-type":"application/json", "X-CSRFToken":getCookie('csrftoken')},
            body : JSON.stringify({
                // Content is mandatory
                content : id
            })
        })
        .then(response => response.json())
        .then(result =>
            console.log(result));
    
}

function unfollowUser(id) {
    console.log(id);
        fetch(`/unfollow/${id}`,{
            method : "POST",
            headers : {"Content-type":"application/json", "X-CSRFToken":getCookie('csrftoken')},
            body : JSON.stringify({
                // Content is mandatory
                content : id
            })
        })
        .then(response => response.json())
        .then(result =>
            console.log(result));
}

// Handle the cookies
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if(parts.length == 2) return parts.pop().split(';').shift(); 
    }

