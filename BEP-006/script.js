// Navegação entre slides
let currentSlide = 1;
const totalSlides = 19;

function initNavigation() {
  // Criar botões de navegação
  const prevButton = document.createElement('button');
  prevButton.className = 'nav-button nav-prev';
  prevButton.innerHTML = '‹';
  prevButton.onclick = () => goToSlide(currentSlide - 1);
  
  const nextButton = document.createElement('button');
  nextButton.className = 'nav-button nav-next';
  nextButton.innerHTML = '›';
  nextButton.onclick = () => goToSlide(currentSlide + 1);
  
  // Criar contador de slides
  const counter = document.createElement('div');
  counter.className = 'slide-counter';
  counter.innerHTML = `${currentSlide} / ${totalSlides}`;
  
  // Adicionar elementos ao body
  document.body.appendChild(prevButton);
  document.body.appendChild(nextButton);
  document.body.appendChild(counter);
  
  // Atualizar estado inicial
  updateNavigation();
}

function goToSlide(slideNumber) {
  if (slideNumber < 1 || slideNumber > totalSlides) {
    console.log(`Slide ${slideNumber} fora do range (1-${totalSlides})`);
    return;
  }
  
  currentSlide = slideNumber;
  const slideFile = `slide${String(slideNumber).padStart(2, '0')}.html`;
  
  console.log(`Navegando para slide ${slideNumber}: ${slideFile}`);
  
  // Redirecionar para o slide
  window.location.href = slideFile;
}

function updateNavigation() {
  const prevButton = document.querySelector('.nav-prev');
  const nextButton = document.querySelector('.nav-next');
  const counter = document.querySelector('.slide-counter');
  
  if (prevButton) {
    prevButton.disabled = currentSlide === 1;
  }
  
  if (nextButton) {
    nextButton.disabled = currentSlide === totalSlides;
  }
  
  if (counter) {
    counter.innerHTML = `${currentSlide} / ${totalSlides}`;
  }
}

// Navegação por teclado
document.addEventListener('keydown', function(event) {
  switch(event.key) {
    case 'ArrowLeft':
      goToSlide(currentSlide - 1);
      break;
    case 'ArrowRight':
      goToSlide(currentSlide + 1);
      break;
    case 'Home':
      goToSlide(1);
      break;
    case 'End':
      goToSlide(totalSlides);
      break;
  }
});

// Inicializar quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
  // Extrair número do slide do nome do arquivo
  const fileName = window.location.pathname.split('/').pop();
  const slideMatch = fileName.match(/slide(\d+)\.html/);
  if (slideMatch) {
    currentSlide = parseInt(slideMatch[1]);
  }
  
  initNavigation();
});

// Função para destacar código (removida para evitar problemas de formatação)
// Os blocos de código já estão formatados corretamente no HTML
