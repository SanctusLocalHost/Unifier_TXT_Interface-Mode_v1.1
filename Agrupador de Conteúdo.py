# Importa os módulos necessários...
import os  # Módulo para interação com o sistema operacional
import tkinter as tk  # Biblioteca para criação de interfaces gráficas
from tkinter import filedialog, messagebox  # Componentes específicos do tkinter para diálogo de arquivos e mensagens

# Função para concatenar o conteúdo dos arquivos de texto
def concatenate_files(directory):
    """
    Concatena o conteúdo de todos os arquivos de texto em um único arquivo.

    :param directory: O diretório contendo os arquivos a serem concatenados.
    """
    # Define o nome e caminho do arquivo de saída
    output_filename = 'CONTEÚDO AGRUPADO!!!.txt'
    output_filepath = os.path.join(directory, output_filename)

    try:
        # Abre o arquivo de saída para escrita
        with open(output_filepath, 'w') as outfile:
            # Itera sobre os arquivos no diretório selecionado
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                # Verifica se o item é um arquivo e não o próprio script
                if os.path.isfile(file_path) and file_name != "Concatenador_de_Arquivos_de_Texto.py":
                    # Abre o arquivo de entrada e adiciona seu conteúdo ao arquivo de saída
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read())

        # Exibe uma mensagem de sucesso ao usuário
        messagebox.showinfo("Sucesso", f'Arquivos de texto concatenados em {output_filepath}')
    except Exception as e:
        # Em caso de erro, exibe uma mensagem de erro ao usuário
        messagebox.showerror("Erro", f"Ocorreu um erro ao concatenar os arquivos: {e}")

# Função para selecionar o diretório contendo os arquivos de texto
def select_directory():
    """
    Abre uma janela de diálogo para selecionar o diretório.
    Atualiza a entrada de diretório na interface gráfica com o diretório selecionado.
    Ativa o botão de concatenação.
    """
    # Abre uma janela de diálogo para seleção do diretório
    directory = filedialog.askdirectory()
    if directory:
        # Atualiza a entrada de diretório com o diretório selecionado
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)
        # Ativa o botão de concatenação
        concatenate_button.config(state=tk.NORMAL)

# Cria uma janela principal
root = tk.Tk()
# Define o título da janela
root.title("Concatenador de Arquivos de Texto")

# Cria um frame para organizar os widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Cria um rótulo para indicar a ação a ser realizada pelo usuário
label = tk.Label(frame, text="Selecione o Diretório com os Arquivos de Texto:")
label.pack(pady=(0, 10))

# Cria uma entrada de texto para exibir o diretório selecionado
directory_entry = tk.Entry(frame, width=50)
directory_entry.pack(side=tk.TOP, padx=(0, 10))

# Cria um botão para abrir o diálogo de seleção de diretório
browse_button = tk.Button(frame, text="Selecionar Diretório", command=select_directory)
browse_button.pack(side=tk.TOP, pady=(0, 5), fill=tk.X)

# Cria um botão para iniciar a concatenação dos arquivos
concatenate_button = tk.Button(frame, text="Concatenar", command=lambda: concatenate_files(directory_entry.get()), state=tk.DISABLED)
concatenate_button.pack(side=tk.BOTTOM, pady=(5, 0), fill=tk.X)

# Inicia o loop principal da interface gráfica
root.mainloop()
