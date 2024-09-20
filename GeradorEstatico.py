import pdfplumber
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext

# Expressão regular para capturar domínios
dominio_regex = re.compile(
    r'\b(?:[a-zA-Z0-9-]+\.)+(?:com|net|org|info|biz|gov|edu|me|io|co|tv|cc|xyz|club|site|online|live|top|vip|pro|blog|dev|shop|store|ink|art|app|fm|us|br|uk|eu|ca|au|ru|fr|de|jp|cn|[a-z]{2,})\b'
)

# Função definitiva para extrair domínios de qualquer PDF
def extrair_dominios(pdf_path):
    dominios = set()
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            # Extrair todo o texto da página
            page_text = page.extract_text() or ""
            
            # Extrair todas as tabelas da página e concatenar ao texto
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    # Adicionar cada célula de tabela ao texto da página
                    row_text = " ".join([cell.strip() for cell in row if cell])
                    page_text += " " + row_text
            
            # Procurar todos os domínios na página usando a expressão regular
            dominios_encontrados = dominio_regex.findall(page_text)
            dominios.update(dominios_encontrados)  # Adiciona domínios ao conjunto (elimina duplicatas automaticamente)
    
    return list(dominios)

# Função para gerar as regras de Mikrotik a partir dos domínios extraídos
def gerar_regras_mikrotik(dominios):
    template_ipv4 = 'add name="{domain}" address=127.0.0.1 ttl=1d'
    template_ipv6 = 'add name="{domain}" type=AAAA address="::1" ttl=1d'
    regras = []
    for dominio in dominios:
        regra_ipv4 = template_ipv4.format(domain=dominio)
        regra_ipv6 = template_ipv6.format(domain=dominio)
        regras.append(regra_ipv4)
        regras.append(regra_ipv6)
    return regras

# Função para selecionar o PDF
def escolher_pdf():
    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivo PDF", "*.pdf")],
        title="Escolha o arquivo PDF"
    )
    if arquivo:
        caminho_pdf.set(arquivo)

# Função para gerar e exibir as regras
def gerar_regras():
    caminho = caminho_pdf.get()
    if not caminho:
        messagebox.showwarning("Aviso", "Por favor, selecione um arquivo PDF primeiro.")
        return
    
    try:
        dominios_extraidos = extrair_dominios(caminho)
        regras = gerar_regras_mikrotik(dominios_extraidos)
        exibir_regras.delete(1.0, tk.END)
        for regra in regras:
            exibir_regras.insert(tk.END, regra + "\n")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível processar o arquivo.\nErro: {e}")

# Função para salvar as regras em um arquivo
def salvar_regras():
    if not exibir_regras.get(1.0, tk.END).strip():
        messagebox.showwarning("Aviso", "Nenhuma regra gerada para salvar.")
        return

    arquivo_salvar = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt")],
        title="Salvar Regras"
    )
    if arquivo_salvar:
        with open(arquivo_salvar, "w") as file:
            file.write(exibir_regras.get(1.0, tk.END))
        messagebox.showinfo("Sucesso", "Regras salvas com sucesso.")

# Interface Gráfica com tkinter
app = tk.Tk()
app.title("Gerador de Regras Mikrotik")
app.geometry("600x400")

# Caminho do PDF
caminho_pdf = tk.StringVar()

# Botão para escolher o arquivo PDF
botao_escolher = tk.Button(app, text="Escolher PDF", command=escolher_pdf)
botao_escolher.pack(pady=10)

# Campo de texto para exibir o caminho do PDF selecionado
campo_caminho_pdf = tk.Entry(app, textvariable=caminho_pdf, width=60)
campo_caminho_pdf.pack(pady=5)

# Botão para gerar as regras
botao_gerar = tk.Button(app, text="Gerar Lista", command=gerar_regras)
botao_gerar.pack(pady=10)

# Área de texto para exibir as regras geradas
exibir_regras = scrolledtext.ScrolledText(app, width=70, height=15)
exibir_regras.pack(pady=10)

# Botão para salvar as regras em um arquivo
botao_salvar = tk.Button(app, text="Salvar Regras", command=salvar_regras)
botao_salvar.pack(pady=10)

# Executa a interface
app.mainloop()
