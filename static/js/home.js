const imageContainer = document.querySelector('.image-container');
const images = imageContainer.querySelectorAll('img');

images.forEach(img => {
    const clone = img.cloneNode(true); // Clone the image
    imageContainer.appendChild(clone); // Append the clone after the original image
});