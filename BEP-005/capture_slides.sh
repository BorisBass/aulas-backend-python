#!/bin/bash

# Script para capturar screenshots dos slides HTML
# Requer: wkhtmltopdf ou wkhtmltoimage

echo "🚀 Iniciando captura dos slides HTML..."

# Diretório dos slides
SLIDES_DIR="/home/loc/Insync/liojes@gmail.com/OneDrive/Meus documentos/IFBA_2025/CEPEDI/aulas/Aula05"
OUTPUT_DIR="$SLIDES_DIR/screenshots"

# Cria diretório de saída
mkdir -p "$OUTPUT_DIR"

# Lista dos slides
slides=(
    "slide01.html"
    "slide02.html"
    "slide03.html"
    "slide04.html"
    "slide05.html"
    "slide06.html"
    "slide07.html"
    "slide08.html"
    "slide09.html"
    "slide10.html"
)

echo "📋 Verificando ferramentas disponíveis..."

# Verifica se wkhtmltoimage está disponível
if command -v wkhtmltoimage &> /dev/null; then
    echo "✅ wkhtmltoimage encontrado"
    TOOL="wkhtmltoimage"
elif command -v wkhtmltopdf &> /dev/null; then
    echo "✅ wkhtmltopdf encontrado"
    TOOL="wkhtmltopdf"
else
    echo "❌ wkhtmltopdf/wkhtmltoimage não encontrado"
    echo "📦 Instale com: sudo apt install wkhtmltopdf"
    echo "🔄 Usando método alternativo..."
    TOOL="browser"
fi

if [ "$TOOL" = "browser" ]; then
    echo "🌐 Abrindo slides no navegador para captura manual..."
    echo "📋 Instruções:"
    echo "1. Para cada slide:"
    echo "   - Pressione F12 para DevTools"
    echo "   - Clique no ícone de dispositivo móvel"
    echo "   - Defina resolução para 1920x1080"
    echo "   - Use Ctrl+Shift+P e digite 'screenshot'"
    echo "   - Escolha 'Capture full size screenshot'"
    echo "   - Salve como slide_01.png, slide_02.png, etc."
    echo ""
    
    for i in "${!slides[@]}"; do
        slide_num=$((i + 1))
        slide_file="${slides[$i]}"
        html_path="$SLIDES_DIR/$slide_file"
        
        if [ -f "$html_path" ]; then
            echo "📄 Abrindo Slide $slide_num: $slide_file"
            xdg-open "$html_path" 2>/dev/null || firefox "$html_path" 2>/dev/null || google-chrome "$html_path" 2>/dev/null
            read -p "Pressione Enter quando terminar de capturar o slide $slide_num..."
        else
            echo "⚠️ Arquivo não encontrado: $html_path"
        fi
    done
else
    echo "🖼️ Capturando screenshots automaticamente..."
    
    for i in "${!slides[@]}"; do
        slide_num=$((i + 1))
        slide_file="${slides[$i]}"
        html_path="$SLIDES_DIR/$slide_file"
        output_file="$OUTPUT_DIR/slide_$(printf "%02d" $slide_num).png"
        
        if [ -f "$html_path" ]; then
            echo "📄 Processando Slide $slide_num: $slide_file"
            
            if [ "$TOOL" = "wkhtmltoimage" ]; then
                wkhtmltoimage --width 1920 --height 1080 --quality 100 "$html_path" "$output_file"
            elif [ "$TOOL" = "wkhtmltopdf" ]; then
                wkhtmltopdf --page-size A4 --width 1920 --height 1080 "$html_path" "$output_file.pdf"
                # Converte PDF para PNG (requer imagemagick)
                if command -v convert &> /dev/null; then
                    convert "$output_file.pdf" "$output_file"
                    rm "$output_file.pdf"
                fi
            fi
            
            if [ -f "$output_file" ]; then
                echo "✅ Screenshot salvo: $output_file"
            else
                echo "❌ Erro ao capturar slide $slide_num"
            fi
        else
            echo "⚠️ Arquivo não encontrado: $html_path"
        fi
    done
fi

echo ""
echo "🎉 Processo concluído!"
echo "📁 Screenshots salvos em: $OUTPUT_DIR"
echo ""
echo "📋 Para usar no PowerPoint/Impress:"
echo "1. Abra PowerPoint ou LibreOffice Impress"
echo "2. Crie uma nova apresentação"
echo "3. Para cada slide, use 'Inserir > Imagens'"
echo "4. Selecione os arquivos PNG da pasta screenshots"
echo "5. Ajuste o tamanho das imagens conforme necessário"




