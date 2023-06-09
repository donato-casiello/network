document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#create').addEventListener('click', showNew);
    })


// Show the new post form
function showNew() {
    document.querySelector('#new').style.display = 'block';
}

// Follow/Unfollow function
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
            console.log(result),
        )
        .then(() => {
            const followButton = document.querySelector('#follow');
            const followersCount = document.querySelector('#followers-count');
            console.log(followersCount);
            if (followButton.innerHTML === 'Follow') {
                followButton.innerHTML = "Unfollow"
                followButton.className = "btn btn-secondary";
                // Update the followers/following count
                followersCount.innerHTML = parseInt(followersCount.innerHTML) + 1; 
            } else {
                followButton.innerHTML = "Follow";
                followButton.className = "btn btn-primary";
                // Update the followers count
                followersCount.innerHTML = parseInt(followersCount.innerHTML) - 1;
            }
        })
    }

// Handle the cookies
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if(parts.length == 2) return parts.pop().split(';').shift(); 
    }

function editPost(id) {
    const textareaValue = document.getElementById(`new_content_${id}`).value;
    const content = document.getElementById(`content_${id}`);
    fetch(`/edit/${id}`, {
        method : "POST",
        headers : {"Content-type":"application/json", "X-CSRFToken":getCookie('csrftoken')},
        body : JSON.stringify({
            content : textareaValue,
        })
    })
    .then(response => response.json())
    .then(result => {
        // Change the value of the content
        content.innerHTML = result.data, 
        console.log(result)
    })
    }

function likeHandler(id) {
    const likes = document.getElementById(`like_${id}`).value;
    fetch(`/like/${id}`, {
        method : "POST",
        headers : {"Content-type":"application/json", "X-CSRFToken":getCookie('csrftoken')},
        body : JSON.stringify({
            content : id        
        })
    })
    .then(response => response.json())
    .then(result => 
        console.log(result))
    .then(() => {
        const likeButton = document.getElementById(`like_${id}`);
        let likeCount = document.getElementById(`like_count_${id}`)
        let likeValue = parseInt(likeCount.innerHTML.split("", 1)[0]);
        if (likeButton.className == "btn btn-outline-warning col-2") {
            likeButton.className = "btn btn-warning col-2";
            likeValue ++;
            likeCount.innerHTML = likeValue + ' Likes';
            console.log(likeValue)
        } else {
            likeButton.className = "btn btn-outline-warning col-2"
            if (likeValue == 0 ){
                // Not below 0
                likeValue = 0;
            } else {
                likeValue --;
            }
            likeCount.innerHTML = likeValue + ' Likes';
            console.log(likeCount)
        }
    })
}   