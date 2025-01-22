

function toggleLike() {

    const likeButton = document.getElementById('likeButton');
    likeButton.classList.toggle('liked');

}

function toggleComment() {

    const commentButtonButton = document.getElementById('commentButton');
    commentButton.classList.toggle('commented');

}

function toggleShare() {

    const shareButton = document.getElementById('shareButton');
    shareButton.classList.toggle('shared');

}


document.getElementById('likeButton').addEventListener('click', toggleLike);
document.getElementById('commentButton').addEventListener('click', toggleComment);
document.getElementById('shareButton').addEventListener('click', toggleShare);
