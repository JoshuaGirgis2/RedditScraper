document.addEventListener("DOMContentLoaded", () => {
    fetch('http://127.0.0.1:5000/api/reddit_posts')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const postsContainer = document.getElementById('posts-container');
            data.forEach(post => {
                const postDiv = document.createElement('div');
                postDiv.className = 'post';
                postDiv.innerHTML = `
                    <h2>${post.title}</h2>
                    <p>Score: ${post.score}</p>
                    <p>Created At: ${new Date(post.created_utc * 1000).toLocaleString()}</p>
                    <a href="${post.url}" target="_blank">Read more</a>
                `;
                postsContainer.appendChild(postDiv);
            });
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
});
