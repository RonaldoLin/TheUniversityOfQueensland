//Live Chat Support
let chatOpen = false;

let chatBox = document.querySelector('#chatBox');

document.querySelector('#chatIcon').addEventListener('click', function () {
    chatOpen = !chatOpen;
    chatBox.style.display = chatOpen ? 'block' : 'none';
});

document.querySelector('#chatInput').addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        let userText = this.value;
        this.value = '';
        addChatBubble('user', userText);
        getChatBotResponse(userText);
    }
});

function addChatBubble(userType, text) {
    let bubble = document.createElement('div');
    bubble.classList.add('chatBubble', userType);
    bubble.innerText = text;
    chatBox.appendChild(bubble);
}

function getChatBotResponse(userText) {
    let botText = 'Sorry, I did not understand that.';
    if (userText.toLowerCase().includes('hello')) {
        botText = 'Hello! How can I help you today?';
    } else if (userText.toLowerCase().includes('booking')) {
        botText = 'You can book a room through our online booking system.';
    } else if (userText.toLowerCase().includes('price')) {
        botText = 'Our room prices start from $100 per night.';
    }
    setTimeout(function () {
        addChatBubble('bot', botText);
    }, 1000);
}

//Mouse Event
let elements = document.getElementsByClassName("listhover");

for (let i = 0; i < elements.length; i++) {
    elements[i].addEventListener("mouseenter", function (e) {
        var object = elements[i];
        object.setAttribute('style', "height:600px")
        object.querySelector('#arrow').setAttribute("style", 'display:none')
    });
    elements[i].addEventListener("mouseleave", function (e) {
        var object = elements[i];
        object.setAttribute('style', "height:310px")
        object.querySelector('#arrow').setAttribute("style", 'display:inline;')
    });
}

//Carousel Gallary
let images = document.querySelectorAll('.carousel__image');
let currentIndex = 0;
let time = 3000; //Time in milliseconds to change to the next image

if (images.length > 0) {
    images[currentIndex].style.display = "block";

    setInterval(nextImage, time);

    function nextImage() {
        images[currentIndex].style.display = "none";
        currentIndex = ++currentIndex % images.length;
        images[currentIndex].style.display = "block";
    }
}

//Booking Date Validation
if (document.getElementById('arrival-date2') !== null) {
    document.getElementById('arrival-date2').setAttribute('min', new Date().toISOString().split('T')[0]);
}

//Booking Confirmation Detail Window
const galleryImages = document.querySelectorAll('.gallery-container img');
const modal = document.getElementById('booking-modal');
const modalContent = document.querySelector('.modal-content');
const closeModal = document.querySelector('.close');

galleryImages.forEach((img) => {
    img.addEventListener('click', () => {
        const modalImg = img.cloneNode(true);
        modalContent.appendChild(modalImg);
        modal.style.display = 'block';
    });
});

if (closeModal !== null) {
    closeModal.addEventListener('click', () => {
        modal.style.display = 'none';
        const modalImg = modalContent.querySelector('img');
        if (modalImg) {
            modalContent.removeChild(modalImg);
        }
    });
}

if (document.getElementById('booking-form') !== null) {
    document.getElementById('booking-form').addEventListener('submit', function (event) {
        event.preventDefault();

        //Get the input values from the form
        const name = document.getElementById('name2').value;
        const email = document.getElementById('email2').value;
        const arrivalDate = document.getElementById('arrival-date2').value;
        const nights = document.getElementById('nights2').value;

        //Check if all the required fields are filled in
        if (name && email && arrivalDate && nights) {
            //Show the booking confirmation window
            document.getElementById('booking-details').innerHTML = `
            <p>Name: ${name}</p>
            <p>Email: ${email}</p>
            <p>Arrival Date: ${arrivalDate}</p>
            <p>Nights: ${nights}</p>
          `;
            modal.style.display = 'block';
        } else {
            //Show the error message
            alert('Please fill in all the required fields.');
        }
    });
}

//Close the window when clicking outside of the window content
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = 'none';
        const modalImg = modalContent.querySelector('img');
        if (modalImg) {
            modalContent.removeChild(modalImg);
        }
    }
}

let thumbnails = document.querySelectorAll(".thumb");
let mainImage = document.getElementById("mainImage");

thumbnails.forEach(function (thumbnail) {
    thumbnail.addEventListener("click", function () {
        mainImage.src = thumbnail.src;
    });
});

let thumbnails1 = document.querySelectorAll(".thumb1");
let mainImage1 = document.getElementById("mainImage1");

thumbnails1.forEach(function (thumbnail) {
    thumbnail.addEventListener("click", function () {
        mainImage1.src = thumbnail.src;
    });
});

let thumbnails2 = document.querySelectorAll(".thumb2");
let mainImage2 = document.getElementById("mainImage2");

thumbnails2.forEach(function (thumbnail) {
    thumbnail.addEventListener("click", function () {
        mainImage2.src = thumbnail.src;
    });
});
