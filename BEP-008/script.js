// JavaScript simples para BEP-007

// Inicialização quando a página carrega
document.addEventListener('DOMContentLoaded', function() {
    createSimpleNavigation();
    addKeyboardNavigation();
    addCodeActions();
});

// Função para criar navegação simples
function createSimpleNavigation() {
    const nav = document.querySelector('.nav');
    if (!nav) return;
    
    // Extrair número do slide do ID da página
    const slideId = document.querySelector('.slide')?.id;
    const currentSlideNumber = slideId ? parseInt(slideId.replace('slide', '')) : 1;
    
    // Botão anterior
    const prevBtn = document.createElement('button');
    prevBtn.innerHTML = '← Anterior';
    prevBtn.onclick = () => {
        if (currentSlideNumber > 1) {
            window.location.href = `slide${String(currentSlideNumber - 1).padStart(2, '0')}.html`;
        }
    };
    if (currentSlideNumber <= 1) {
        prevBtn.disabled = true;
        prevBtn.style.opacity = '0.5';
    }
    nav.appendChild(prevBtn);
    
    // Indicador de slide atual
    const slideIndicator = document.createElement('span');
    slideIndicator.innerHTML = `${currentSlideNumber} / 15`;
    slideIndicator.style.color = 'white';
    slideIndicator.style.margin = '0 20px';
    slideIndicator.style.fontWeight = 'bold';
    nav.appendChild(slideIndicator);
    
    // Botão próximo
    const nextBtn = document.createElement('button');
    nextBtn.innerHTML = 'Próximo →';
    nextBtn.onclick = () => {
        if (currentSlideNumber < 15) {
            window.location.href = `slide${String(currentSlideNumber + 1).padStart(2, '0')}.html`;
        }
    };
    if (currentSlideNumber >= 15) {
        nextBtn.disabled = true;
        nextBtn.style.opacity = '0.5';
    }
    nav.appendChild(nextBtn);
    
    // Botão de índice
    const indexBtn = document.createElement('button');
    indexBtn.innerHTML = '📋 Índice';
    indexBtn.onclick = () => window.location.href = 'index.html';
    indexBtn.style.marginLeft = '20px';
    nav.appendChild(indexBtn);
}

// Função para adicionar navegação por teclado
function addKeyboardNavigation() {
    document.addEventListener('keydown', function(event) {
        const slideId = document.querySelector('.slide')?.id;
        const currentSlideNumber = slideId ? parseInt(slideId.replace('slide', '')) : 1;
        
        switch(event.key) {
            case 'ArrowRight':
            case ' ':
                event.preventDefault();
                if (currentSlideNumber < 15) {
                    window.location.href = `slide${String(currentSlideNumber + 1).padStart(2, '0')}.html`;
                }
                break;
            case 'ArrowLeft':
                event.preventDefault();
                if (currentSlideNumber > 1) {
                    window.location.href = `slide${String(currentSlideNumber - 1).padStart(2, '0')}.html`;
                }
                break;
            case 'Home':
                event.preventDefault();
                window.location.href = 'slide01.html';
                break;
            case 'End':
                event.preventDefault();
                window.location.href = 'slide15.html';
                break;
            case 'Escape':
                event.preventDefault();
                window.location.href = 'index.html';
                break;
        }
    });
}

// Função para copiar código
function copyCode(codeElement) {
    const text = codeElement.textContent;
    navigator.clipboard.writeText(text).then(function() {
        // Mostrar feedback visual
        const originalText = codeElement.textContent;
        codeElement.textContent = 'Código copiado!';
        codeElement.style.background = '#48BB78';
        
        setTimeout(function() {
            codeElement.textContent = originalText;
            codeElement.style.background = '#1A202C';
        }, 2000);
    });
}

// Adicionar botões de ação aos blocos de código
function addCodeActions() {
    const codeBlocks = document.querySelectorAll('.code-block');
    
    codeBlocks.forEach(block => {
        // Adicionar botões de ação
        const actions = document.createElement('div');
        actions.style.cssText = `
            position: absolute;
            top: 10px;
            right: 10px;
            display: flex;
            gap: 5px;
        `;
        
        const copyBtn = document.createElement('button');
        copyBtn.innerHTML = '📋';
        copyBtn.title = 'Copiar código';
        copyBtn.style.cssText = `
            background: #4B8BBE;
            color: white;
            border: none;
            padding: 5px 8px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 12px;
        `;
        copyBtn.onclick = () => copyCode(block);
        
        actions.appendChild(copyBtn);
        
        // Tornar o bloco de código relativo para posicionamento absoluto dos botões
        block.style.position = 'relative';
        block.appendChild(actions);
    });
}