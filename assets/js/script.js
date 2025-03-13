let currentIndex = 0;
const carouselItems = document.querySelectorAll('.carousel-item');
const totalItems = carouselItems.length;

function showSlide(index) {
    const carousel = document.querySelector('.carousel');
    const offset = -index * 800; // Adjust based on image width
    carousel.style.transform = `translateX(${offset}px)`;
}

document.getElementById('next').addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % totalItems;
    showSlide(currentIndex);
});

document.getElementById('prev').addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + totalItems) % totalItems;
    showSlide(currentIndex);
});

// Optional: Automatic scrolling
setInterval(() => {
    currentIndex = (currentIndex + 1) % totalItems;
    showSlide(currentIndex);
}, 2000); // Change slide every 5 seconds