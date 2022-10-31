import axios from 'axios';

document.addEventListener('DOMContentLoaded', async () => {
    const inputSection = document.querySelector('.input-section');
    if (inputSection) {
        const inputForm = inputSection.querySelector('.input-section__form'); 
        const input = inputSection.querySelector('.input-section__input');
        const submitBtn = inputSection.querySelector('.input-section__submit-btn');

        submitBtn.disabled = true;

        input.addEventListener('input', () => {
            if (input.value === "Поделитесь своими мыслями" || input.value === "" ) {
                submitBtn.disabled = true;
                // console.log("disabled", input.value)
            } else {
                submitBtn.disabled = false;
                // console.log("enabled", input.value)
            }
        })

        inputForm.addEventListener('submit', async (e) => {
            
            e.preventDefault();
            const response = await axios.get('http://localhost:8000/profile');
            const userId = response.data.id
            
            const post = {
                id: Math.floor(Math.random() * 100),
                userId: userId,
                text: input.value
            }
            try {
                const postResponse = await axios.post('http://localhost:8000/posts', post);
                console.log(postResponse);
            } catch (err) {
                console.log(err)
            }
            
        })
        
    }
    
    

})