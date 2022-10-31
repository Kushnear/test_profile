import axios from 'axios';

document.addEventListener('DOMContentLoaded', async () => {
    const profileSection = document.querySelector('.profile');
    const profilePicture = profileSection.querySelector('.profile__img');
    const profileFirstName = profileSection.querySelector('.profile__first-name');
    const profileLastName = profileSection.querySelector('.profile__last-name');

    // console.log(profilePictureSrc)

    if (profileSection) {
    try {
        const response = await axios.get('http://localhost:8000/profile');
        profilePicture.setAttribute('src', response.data.photo);
        profileFirstName.innerText = response.data.firstName;
        profileLastName.innerText = response.data.lastName;
    } catch (error) {
        console.log(error)
    }
    }
})