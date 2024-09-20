---

# Gerador-De-Regras-Mikrotik

Created on 2024/09/20, by Kauan Pollicarpo Pereira.

This project converts lists of domains found in tables within PDF files into static DNS filter rules for Mikrotik routers, which can be easily pasted into Mikrotik terminals. It uses regular expressions (REGEX) to identify the domains within the text of the PDFs and also analyzes table content if necessary, ensuring that all domains are correctly captured. The tool provides a simple graphical interface where the user can select the PDF file, generate the rules, and save them for later use.

## Descrição do Projeto (PT-BR)
O **Gerador de Regras Mikrotik** é uma aplicação desenvolvida em Python com uma interface gráfica (GUI) simples usando `tkinter`. O objetivo deste projeto é automatizar a extração de domínios de arquivos PDF e gerar regras de DNS estático para roteadores Mikrotik. As regras geradas permitem redirecionar domínios específicos para o endereço `127.0.0.1` (IPv4) e `::1` (IPv6), bloqueando o acesso a esses domínios.

### Funcionalidades
- **Escolher Arquivo PDF**: Seleciona um arquivo PDF que contém os domínios.
- **Gerar Lista**: Extrai os domínios do PDF e gera as regras de DNS para Mikrotik.
- **Exibir Regras**: Mostra as regras geradas na interface.
- **Salvar Regras**: Salva as regras geradas em um arquivo `.txt` para fácil importação no Mikrotik.

### Requisitos
- Python 3.6+
- Bibliotecas Python:
  - pdfplumber (`pip install pdfplumber`)
  - tkinter (normalmente incluída na instalação padrão do Python)
  - re (biblioteca padrão)

### Instalação e Execução
1. Clone o repositório ou baixe o código-fonte.
2. Instale as bibliotecas necessárias usando:
   ```bash
   pip install pdfplumber
   ```
3. Execute o script Python:
   ```bash
   python gerador_mikrotik.py
   ```
4. A interface gráfica será aberta, permitindo que você selecione um PDF e gere as regras.

### Como Usar
1. Clique no botão "Escolher PDF" para selecionar um arquivo PDF contendo os domínios.
2. Clique em "Gerar Lista" para extrair os domínios e gerar as regras de DNS.
3. As regras geradas serão exibidas na área de texto.
4. Clique em "Salvar Regras" para salvar as regras geradas em um arquivo de texto.

### Gerando Executável
Para gerar um executável `.exe` a partir do script Python usando `PyInstaller`:
1. Instale o PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Crie o executável:
   ```bash
   pyinstaller --onefile --windowed gerador_mikrotik.py
   ```
3. O executável será gerado na pasta `dist`.

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias ou correções.

---

## Project Description (EN)
The **Mikrotik Rules Generator** is an application developed in Python with a simple graphical interface (GUI) using `tkinter`. The goal of this project is to automate the extraction of domains from PDF files and generate static DNS rules for Mikrotik routers. The generated rules allow specific domains to be redirected to the `127.0.0.1` (IPv4) and `::1` (IPv6) addresses, blocking access to those domains.

### Features
- **Choose PDF File**: Selects a PDF file containing the domains.
- **Generate List**: Extracts the domains from the PDF and generates DNS rules for Mikrotik.
- **Display Rules**: Shows the generated rules in the interface.
- **Save Rules**: Saves the generated rules to a `.txt` file for easy import into Mikrotik.

### Requirements
- Python 3.6+
- Python Libraries:
  - pdfplumber (`pip install pdfplumber`)
  - tkinter (usually included in the standard Python installation)
  - re (standard library)

### Installation and Execution
1. Clone the repository or download the source code.
2. Install the required libraries using:
   ```bash
   pip install pdfplumber
   ```
3. Run the Python script:
   ```bash
   python gerador_mikrotik.py
   ```
4. The graphical interface will open, allowing you to select a PDF and generate the rules.

### How to Use
1. Click the "Choose PDF" button to select a PDF file containing the domains.
2. Click "Generate List" to extract the domains and generate the DNS rules.
3. The generated rules will be displayed in the text area.
4. Click "Save Rules" to save the generated rules to a text file.

### Generating an Executable
To generate an `.exe` executable from the Python script using `PyInstaller`:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Create the executable:
   ```bash
   pyinstaller --onefile --windowed gerador_mikrotik.py
   ```
3. The executable will be generated in the `dist` folder.

### Contributions
Contributions are welcome! Feel free to open issues or pull requests with improvements or fixes.
