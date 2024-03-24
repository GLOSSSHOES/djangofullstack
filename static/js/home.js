const imageContainer = document.querySelector('.image-container');
const imageWrapper = imageContainer.querySelectorAll('.image-wrapper');

imageWrapper.forEach(img => {
    const clone = img.cloneNode(true); // Clone the image
    imageContainer.appendChild(clone); // Append the clone after the original image
});