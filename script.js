// JavaScript centralizado para todas as aulas BEP

// Inicialização quando a página carrega
document.addEventListener('DOMContentLoaded', function() {
    console.log('Script carregado!');
    createSimpleNavigation();
    addKeyboardNavigation();
    addCodeActions();
});

// Função para criar navegação simples
function createSimpleNavigation() {
    console.log('Criando navegação...');
    const nav = document.querySelector('.nav');
    console.log('Elemento .nav encontrado:', nav);
    
    if (!nav) {
        console.log('Elemento .nav não encontrado!');
        return;
    }
    
    // Limpar navegação existente
    nav.innerHTML = '';
    
    // Extrair número do slide do ID da página ou nome do arquivo
    const slideId = document.querySelector('.slide')?.id;
    const currentFile = window.location.pathname;
    let currentSlideNumber = 1;
    let isSlide05b = false;
    
    // Verificar se é o slide 05b
    if (slideId === 'slide05b' || currentFile.includes('slide05b.html')) {
        isSlide05b = true;
        currentSlideNumber = 5; // Tratar como slide 5 para lógica de navegação
    } else if (slideId) {
        const match = slideId.match(/slide(\d+)/);
        if (match) {
            currentSlideNumber = parseInt(match[1]);
        }
    } else {
        const fileMatch = currentFile.match(/slide(\d+)\.html/);
        if (fileMatch) {
            currentSlideNumber = parseInt(fileMatch[1]);
        }
    }
    
    console.log('Slide ID encontrado:', slideId);
    console.log('Número do slide atual:', currentSlideNumber);
    
    const totalSlides = getTotalSlides();
    console.log('Total de slides:', totalSlides);
    
    // Botão índice da aula (home) - primeiro
    const homeBtn = document.createElement('a');
    homeBtn.textContent = '🏠 Índice da aula';
    homeBtn.href = 'index.html';
    homeBtn.style.cssText = `
        background: #2D3748;
        color: white;
        text-decoration: none;
        padding: 10px 16px;
        border-radius: 5px;
        margin-right: 10px;
        font-size: 14px;
        display: inline-block;
    `;
    nav.appendChild(homeBtn);

    // Botão anterior - depois do índice
    const prevBtn = document.createElement('button');
    prevBtn.innerHTML = '← Anterior';
    prevBtn.style.cssText = `
        background: #4B8BBE;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        margin-right: 10px;
        font-size: 14px;
    `;
    
    prevBtn.onclick = () => {
        if (isSlide05b) {
            // Do 05b, voltar para 05
            window.location.href = 'slide05.html';
        } else if (currentSlideNumber > 1) {
            window.location.href = `slide${String(currentSlideNumber - 1).padStart(2, '0')}.html`;
        }
    };
    
    if (currentSlideNumber <= 1 && !isSlide05b) {
        prevBtn.disabled = true;
        prevBtn.style.opacity = '0.5';
        prevBtn.style.cursor = 'not-allowed';
    }
    nav.appendChild(prevBtn);

    
    // Indicador de slide atual
    const slideIndicator = document.createElement('span');
    const displayNumber = isSlide05b ? '05b' : String(currentSlideNumber).padStart(2, '0');
    const displayTotal = String(totalSlides).padStart(2, '0');
    slideIndicator.innerHTML = `${displayNumber} / ${displayTotal}`;
    slideIndicator.style.cssText = `
        color: white;
        margin: 0 20px;
        font-weight: bold;
        font-size: 16px;
    `;
    nav.appendChild(slideIndicator);
    
    // Botão próximo
    const nextBtn = document.createElement('button');
    nextBtn.innerHTML = 'Próximo →';
    nextBtn.style.cssText = `
        background: #4B8BBE;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        margin-left: 10px;
        font-size: 14px;
    `;
    
    nextBtn.onclick = () => {
        // Lógica especial para BEP-019
        const currentPath = window.location.pathname;
        const currentUrl = window.location.href;
        const isBEP019 = currentPath.includes('BEP-019') || currentUrl.includes('BEP-019');
        
        if (isBEP019) {
            if (currentSlideNumber === 5 && !isSlide05b) {
                // Do slide 05, ir para 05b
                window.location.href = 'slide05b.html';
            } else if (isSlide05b) {
                // Do 05b, ir para 06
                window.location.href = 'slide06.html';
            } else if (currentSlideNumber < 8) {
                // Do slide 01-07, ir para o próximo
                window.location.href = `slide${String(currentSlideNumber + 1).padStart(2, '0')}.html`;
            } else if (currentSlideNumber === 8) {
                // Slide 08 é o último, não há próximo
                return;
            }
        } else {
            // Lógica padrão para outras aulas
            if (currentSlideNumber < totalSlides) {
                window.location.href = `slide${String(currentSlideNumber + 1).padStart(2, '0')}.html`;
            }
        }
    };
    
    // Desabilitar botão próximo se estiver no último slide
    const currentPath = window.location.pathname;
    const currentUrl = window.location.href;
    const isBEP019 = currentPath.includes('BEP-019') || currentUrl.includes('BEP-019');
    const isLastSlide = isBEP019 
        ? (currentSlideNumber === 8)  // Slide 08 é o último do BEP-019
        : (currentSlideNumber >= totalSlides);
    
    if (isLastSlide) {
        nextBtn.disabled = true;
        nextBtn.style.opacity = '0.5';
        nextBtn.style.cursor = 'not-allowed';
    }
    nav.appendChild(nextBtn);
    
    console.log('Navegação criada com sucesso!');
}

// Função para adicionar navegação por teclado
function addKeyboardNavigation() {
    document.addEventListener('keydown', function(e) {
        const slideId = document.querySelector('.slide')?.id;
        const currentFile = window.location.pathname;
        let currentSlideNumber = 1;
        let isSlide05b = false;
        
        // Verificar se é o slide 05b
        if (slideId === 'slide05b' || currentFile.includes('slide05b.html')) {
            isSlide05b = true;
            currentSlideNumber = 5;
        } else if (slideId) {
            const match = slideId.match(/slide(\d+)/);
            if (match) {
                currentSlideNumber = parseInt(match[1]);
            }
        } else {
            const fileMatch = currentFile.match(/slide(\d+)\.html/);
            if (fileMatch) {
                currentSlideNumber = parseInt(fileMatch[1]);
            }
        }
        
        const totalSlides = getTotalSlides();
        const currentPath = window.location.pathname;
        const currentUrl = window.location.href;
        const isBEP019 = currentPath.includes('BEP-019') || currentUrl.includes('BEP-019');
        
        if (e.key === 'ArrowLeft') {
            if (isSlide05b) {
                window.location.href = 'slide05.html';
            } else if (currentSlideNumber > 1) {
                window.location.href = `slide${String(currentSlideNumber - 1).padStart(2, '0')}.html`;
            }
        } else if (e.key === 'ArrowRight') {
            if (isBEP019) {
                if (currentSlideNumber === 5 && !isSlide05b) {
                    window.location.href = 'slide05b.html';
                } else if (isSlide05b) {
                    window.location.href = 'slide06.html';
                } else if (currentSlideNumber < 8) {
                    window.location.href = `slide${String(currentSlideNumber + 1).padStart(2, '0')}.html`;
                }
                // Se estiver no slide 08, não faz nada (é o último)
            } else {
                // Lógica padrão para outras aulas
                if (currentSlideNumber < totalSlides) {
                    window.location.href = `slide${String(currentSlideNumber + 1).padStart(2, '0')}.html`;
                }
            }
        }
    });
}

// Função para adicionar ações aos códigos
function addCodeActions() {
    const codeBlocks = document.querySelectorAll('.code-block');
    console.log('Encontrados blocos de código:', codeBlocks.length);
    
    codeBlocks.forEach((block, index) => {
        // Criar container para ações
        const actions = document.createElement('div');
        actions.style.cssText = `
            position: absolute;
            top: 5px;
            right: 5px;
            display: flex;
            gap: 5px;
        `;
        
        // Botão de copiar
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

// Função para copiar código
function copyCode(block) {
    const text = block.textContent.replace('📋', '').trim();
    navigator.clipboard.writeText(text).then(() => {
        console.log('Código copiado!');
        // Feedback visual pode ser adicionado aqui
    }).catch(err => {
        console.error('Erro ao copiar:', err);
    });
}

// Função para determinar o número total de slides baseado na pasta atual
function getTotalSlides() {
    const currentPath = window.location.pathname;
    const currentUrl = window.location.href;
    
    console.log('=== DEBUG getTotalSlides ===');
    console.log('currentPath:', currentPath);
    console.log('currentUrl:', currentUrl);
    
    // Mapear cada aula para seu número de slides
    const slideCounts = {
        'BEP-001': 12,
        'BEP-002': 15,
        'BEP-003': 7,
        'BEP-004': 7,
        'BEP-005': 7,
        'BEP-006': 6,
        'BEP-007': 19,
        'BEP-008': 15,
        'BEP-009': 15,
        'BEP-010': 7,
        'BEP-011': 10,
        'BEP-012': 12,
        'BEP-013': 13,
        'BEP-014': 8,
        'BEP-015': 8,
        'BEP-016': 7,
        'BEP-017': 8,
        'BEP-018': 8,
        'BEP-019': 9,  // 01-08 + 05b
        'BEP-020': 12,
        'BEP-021': 12,
        'BEP-022': 12
    };
    
    // Detectar a pasta atual usando múltiplos métodos
    for (const [folder, count] of Object.entries(slideCounts)) {
        if (currentPath.includes(folder) || currentUrl.includes(folder)) {
            console.log(`Detectada pasta: ${folder}, slides: ${count}`);
            return count;
        }
    }
    
    // Tentar detectar pelo título da página
    const title = document.title;
    for (const [folder, count] of Object.entries(slideCounts)) {
        if (title.includes(folder)) {
            console.log(`Detectada pasta pelo título: ${folder}, slides: ${count}`);
            return count;
        }
    }
    
    // Tentar detectar pelo header da página
    const header = document.querySelector('.header h1');
    if (header) {
        const headerText = header.textContent;
        for (const [folder, count] of Object.entries(slideCounts)) {
            if (headerText.includes(folder)) {
                console.log(`Detectada pasta pelo header: ${folder}, slides: ${count}`);
                return count;
            }
        }
    }
    
    console.log('Não foi possível detectar a pasta, usando default: 15');
    // Default para 15 slides se não conseguir detectar
    return 15;
}