// nav bar section

document.getElementById('menu-icon').addEventListener('click', function() {
    document.getElementById('nav-links').classList.toggle('active');
});

document.getElementById('close-icon').addEventListener('click', function() {
    document.getElementById('nav-links').classList.remove('active');
});

// slider section

let slider = document.querySelector('.slider')
let sliderList = slider.querySelector('.slider .list')
let thumbnail = document.querySelector('.slider .thumbnail')
let thumbnailItems = thumbnail.querySelectorAll('.item')

thumbnail.appendChild(thumbnailItems[0])

function moveSlider(direction) {
    let sliderItems = sliderList.querySelectorAll('.item')
    let thumbnailItems = document.querySelectorAll('.thumbnail .item')
    
    if(direction === 'next'){
        sliderList.appendChild(sliderItems[0])
        thumbnail.appendChild(thumbnailItems[0])
        slider.classList.add('next')
    } else {
        sliderList.prepend(sliderItems[sliderItems.length - 1])
        thumbnail.prepend(thumbnailItems[thumbnailItems.length - 1])
        slider.classList.add('prev')
    }

    slider.addEventListener('animationend', function() {
        if(direction === 'next'){
            slider.classList.remove('next')
        } else {
            slider.classList.remove('prev')
        }
    }, {once: true}) // Remove the event listener after it's triggered once
}

// Automatic slider functionality
let autoSliderInterval = null;
let autoSliderDirection = 'next';

function startAutoSlider() {
    autoSliderInterval = setInterval(() => {
        moveSlider(autoSliderDirection);
        if (autoSliderDirection === 'next') {
            if (sliderList.children.length === 1) {
                autoSliderDirection = 'prev';
            }
        } else {
            if (sliderList.children.length === sliderList.children.length - 1) {
                autoSliderDirection = 'next';
            }
        }
    }, 4000); // Change the slider every 3 seconds
}

function stopAutoSlider() {
    clearInterval(autoSliderInterval);
}

// Start the automatic slider
startAutoSlider();

//historical section

let currentIndex = 0;

function showSlide(index) {
    const slides = document.querySelector('.tour-slides');
    const totalCards = document.querySelectorAll('.tour-card').length;

    // Ensure the index wraps around
    if (index >= totalCards) {
        currentIndex = 0; // Go back to the first card
    } else if (index < 0) {
        currentIndex = totalCards - 3; // Go to the last set of 3 cards
    } else {
        currentIndex = index;
    }

    // Calculate the transform value to shift the cards
    const offset = -currentIndex * (100 / 3); // Shift by 1/3 of the visible area
    slides.style.transform = `translateX(${offset}%)`;
}

function changeSlide(direction) {
    showSlide(currentIndex + direction);
}

// Initialize the slider
document.addEventListener('DOMContentLoaded', () => {
    showSlide(currentIndex);
});
