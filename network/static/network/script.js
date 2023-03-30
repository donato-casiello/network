document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#create').addEventListener('click', show_new);
});


// Show the new post form
function show_new() {
    document.querySelector('#new').style.display = 'block';
}