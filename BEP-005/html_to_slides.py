#!/usr/bin/env python3
"""
Script para converter slides HTML para imagens para importação em PowerPoint/Impress
"""

import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    """Configura o driver do Chrome para captura de screenshots"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executa sem interface gráfica
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")  # Resolução alta
    chrome_options.add_argument("--force-device-scale-factor=2")  # DPI alto
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"Erro ao configurar o driver: {e}")
        print("Instale o ChromeDriver ou use: pip install selenium")
        return None

def capture_slide(driver, html_file, output_file):
    """Captura screenshot de um slide HTML"""
    try:
        # Converte caminho relativo para absoluto
        abs_path = os.path.abspath(html_file)
        file_url = f"file://{abs_path}"
        
        print(f"Processando: {html_file}")
        driver.get(file_url)
        
        # Aguarda o carregamento completo
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Aguarda um pouco mais para garantir que as imagens carregaram
        time.sleep(2)
        
        # Captura screenshot
        driver.save_screenshot(output_file)
        print(f"Screenshot salvo: {output_file}")
        return True
        
    except Exception as e:
        print(f"Erro ao processar {html_file}: {e}")
        return False

def main():
    """Função principal"""
    # Diretório dos slides
    slides_dir = "/home/loc/Insync/liojes@gmail.com/OneDrive/Meus documentos/IFBA_2025/CEPEDI/aulas/Aula05"
    output_dir = os.path.join(slides_dir, "screenshots")
    
    # Cria diretório de saída
    os.makedirs(output_dir, exist_ok=True)
    
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
    
    # Configura driver
    driver = setup_driver()
    if not driver:
        return
    
    try:
        print("Iniciando captura dos slides...")
        
        for i, slide in enumerate(slides, 1):
            html_path = os.path.join(slides_dir, slide)
            output_path = os.path.join(output_dir, f"slide_{i:02d}.png")
            
            if os.path.exists(html_path):
                success = capture_slide(driver, html_path, output_path)
                if success:
                    print(f"✅ Slide {i} capturado com sucesso")
                else:
                    print(f"❌ Erro ao capturar slide {i}")
            else:
                print(f"⚠️ Arquivo não encontrado: {html_path}")
        
        print(f"\n🎉 Processo concluído! Screenshots salvos em: {output_dir}")
        print("\nPara usar no PowerPoint/Impress:")
        print("1. Abra PowerPoint ou LibreOffice Impress")
        print("2. Crie uma nova apresentação")
        print("3. Para cada slide, use 'Inserir > Imagens' e selecione os arquivos PNG")
        print("4. Ajuste o tamanho das imagens conforme necessário")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()




