#!/usr/bin/env python3
"""
Script simples para abrir slides HTML no navevador para captura manual
"""

import os
import webbrowser
import time

def main():
    """Abre cada slide HTML no navegador para captura manual"""
    
    # Diretório dos slides
    slides_dir = "/home/loc/Insync/liojes@gmail.com/OneDrive/Meus documentos/IFBA_2025/CEPEDI/aulas/Aula05"
    
    # Lista dos slides
    slides = [
        "slide01.html",
        "slide02.html", 
        "slide03.html",
        "slide04.html",
        "slide05.html",
        "slide06.html",
        "slide07.html",
        "slide08.html",
        "slide09.html",
        "slide10.html"
    ]
    
    print("🚀 Abrindo slides no navegador para captura manual...")
    print("📋 Instruções:")
    print("1. Para cada slide que abrir:")
    print("   - Pressione F11 para tela cheia")
    print("   - Use Ctrl+Shift+I para abrir DevTools")
    print("   - Clique no ícone de dispositivo móvel (responsivo)")
    print("   - Defina resolução para 1920x1080")
    print("   - Use Ctrl+Shift+P e digite 'screenshot'")
    print("   - Escolha 'Capture full size screenshot'")
    print("   - Salve como slide_01.png, slide_02.png, etc.")
    print("2. Pressione Enter para abrir o próximo slide")
    print("\n" + "="*60)
    
    for i, slide in enumerate(slides, 1):
        html_path = os.path.join(slides_dir, slide)
        
        if os.path.exists(html_path):
            print(f"\n📄 Abrindo Slide {i}: {slide}")
            print(f"📍 Caminho: {html_path}")
            
            # Abre no navegador padrão
            webbrowser.open(f"file://{html_path}")
            
            # Aguarda input do usuário
            input(f"Pressione Enter quando terminar de capturar o slide {i}...")
        else:
            print(f"⚠️ Arquivo não encontrado: {html_path}")
    
    print("\n🎉 Todos os slides foram processados!")
    print("📁 Agora você pode importar as imagens PNG no PowerPoint ou LibreOffice Impress")

if __name__ == "__main__":
    main()




