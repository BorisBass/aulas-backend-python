# Conversão de Slides HTML para PowerPoint/Impress

Este diretório contém scripts para converter os slides HTML em imagens que podem ser importadas no PowerPoint ou LibreOffice Impress.

## 📁 Arquivos incluídos:

- `slide01.html` até `slide10.html` - Slides originais
- `html_to_slides.py` - Script Python com Selenium (requer instalação)
- `simple_screenshot.py` - Script Python simples para abrir no navegador
- `capture_slides.sh` - Script Bash para captura automática
- `README_CONVERSAO.md` - Este arquivo com instruções

## 🚀 Métodos de conversão:

### Método 1: Script Bash (Recomendado)
```bash
cd "/home/loc/Insync/liojes@gmail.com/OneDrive/Meus documentos/IFBA_2025/CEPEDI/aulas/Aula05"
./capture_slides.sh
```

### Método 2: Script Python simples
```bash
cd "/home/loc/Insync/liojes@gmail.com/OneDrive/Meus documentos/IFBA_2025/CEPEDI/aulas/Aula05"
python3 simple_screenshot.py
```

### Método 3: Captura manual
1. Abra cada slide HTML no navegador
2. Pressione F12 para abrir DevTools
3. Clique no ícone de dispositivo móvel (responsivo)
4. Defina resolução para 1920x1080
5. Use Ctrl+Shift+P e digite "screenshot"
6. Escolha "Capture full size screenshot"
7. Salve como slide_01.png, slide_02.png, etc.

## 📦 Instalação de dependências (opcional):

### Para captura automática:
```bash
# Ubuntu/Debian
sudo apt install wkhtmltopdf imagemagick

# Ou para melhor qualidade
sudo apt install wkhtmltopdf
```

### Para script Python com Selenium:
```bash
pip3 install selenium
# E baixar ChromeDriver
```

## 📋 Como usar as imagens no PowerPoint/Impress:

### PowerPoint:
1. Abra PowerPoint
2. Crie uma nova apresentação
3. Para cada slide: Inserir > Imagens > Este Dispositivo
4. Selecione os arquivos PNG da pasta screenshots
5. Ajuste o tamanho das imagens para preencher o slide

### LibreOffice Impress:
1. Abra LibreOffice Impress
2. Crie uma nova apresentação
3. Para cada slide: Inserir > Imagem > De arquivo
4. Selecione os arquivos PNG da pasta screenshots
5. Ajuste o tamanho das imagens para preencher o slide

## 🎯 Dicas importantes:

- As imagens serão salvas em alta resolução (1920x1080)
- Mantenha a proporção original para melhor qualidade
- Se necessário, ajuste o brilho/contraste das imagens
- Considere adicionar transições entre os slides
- Teste a apresentação antes de usar

## 🔧 Resolução de problemas:

### Se o script não funcionar:
1. Verifique se os arquivos HTML existem
2. Teste abrindo um slide manualmente no navegador
3. Use o método de captura manual
4. Verifique as permissões dos arquivos

### Se as imagens ficarem pequenas:
1. Use resolução maior (2560x1440)
2. Ajuste o zoom do navegador antes de capturar
3. Use ferramentas de edição para redimensionar

## 📞 Suporte:

Se tiver problemas, verifique:
- Permissões dos arquivos
- Instalação das dependências
- Caminhos dos arquivos
- Configurações do navegador




