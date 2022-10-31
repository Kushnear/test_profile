import axios from 'axios';

document.addEventListener('DOMContentLoaded', async () => {
    const postsSection = document.querySelector('.posts');
    const postsContainer = postsSection.querySelector('.posts__container');

    if (!!postsSection) {
        try {
            
            const response = await axios.get('http://localhost:8000/posts');
            const userResponse = await axios.get('http://localhost:8000/profile');
            console.log(response.data)

            response.data.forEach(element => {
                if (!!element.text) {
                    postsContainer.insertAdjacentHTML('beforeend', 
            `<div class="post">
                <div class="post__name"> 
                    <p class="post__first-name">${userResponse.data.firstName}</p>
                    <p class="post__last-name">${userResponse.data.lastName}</p>
                </div>
                <p class="post__text">${element.text}</p>
            </div>`)
                }
            });
            
            
            
        } catch (error) {
            console.log(error)
        }
    }
})