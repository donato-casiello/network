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

