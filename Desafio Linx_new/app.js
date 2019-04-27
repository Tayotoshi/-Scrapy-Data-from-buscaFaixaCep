const carouselSlide = document.querySelector('.lista');
const carouselImages = document.querySelectorAll('.lista img')
const carouselImages = document.querySelectorAll('.lista img')

//Buttons
const prevBtn = document.querySelector('#prevBtn');
const nextBtn = document.querySelector('#nextBtn');

//Counter
let counter = 1;
const size = carouselImages[0].clientWidth;

carouselSlide.style.transform = 'translateX(' +(-size *counter) + 'px)';