import os
import tkinter as tk
from tkinter import filedialog, messagebox

def concatenate_files(directory):
    output_filename = 'CONTEÚDO AGRUPADO!.txt'
    output_filepath = os.path.join(directory, output_filename)
    
    # Extensões a serem ignoradas
    ignore_extensions = {'.py', '.pyw', '.exe', '.xlsx', '.xls', '.csv', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}

    try:
        with open(output_filepath, 'w') as outfile:
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                # Verifica se é um arquivo e se não está na lista de extensões a serem ignoradas
                if os.path.isfile(file_path) and not file_name.endswith(tuple(ignore_extensions)):
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n\n')  # Adiciona uma linha vazia entre os textos concatenados

        messagebox.showinfo("Sucesso", f'Arquivos de texto concatenados em {output_filepath}')
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao concatenar os arquivos: {e}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)
        concatenate_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Unifier TXT Interface Mode")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

instructions = (
    "1. Clique em 'Selecionar Diretório' e escolha a pasta com os arquivos de texto.\n"
    "2. O caminho do diretório selecionado será exibido na caixa de texto.\n"
    "3. Clique em 'Concatenar' para unir os arquivos de texto em um único arquivo.\n"
    "4. Verifique o arquivo 'CONTEÚDO AGRUPADO!.txt' no diretório selecionado."
)

label_instructions = tk.Label(frame, text="PASSO A PASSO", font=('Helvetica', 12, 'bold'), justify=tk.CENTER)
label_instructions.pack(pady=(0, 10))

instructions_label = tk.Label(frame, text=instructions, justify=tk.LEFT)
instructions_label.pack(pady=(0, 10))

label = tk.Label(frame, text="Selecione o Diretório com os Arquivos de Texto:", font=('Helvetica', 10, 'bold'))
label.pack(pady=(0, 10))

directory_entry = tk.Entry(frame, width=50)
directory_entry.pack(side=tk.TOP, padx=(0, 10))

# Reduzir a largura dos botões
button_width = 20

browse_button = tk.Button(frame, text="Selecionar Diretório", command=select_directory, width=button_width)
browse_button.pack(side=tk.TOP, pady=(0, 5))

concatenate_button = tk.Button(frame, text="Concatenar", command=lambda: concatenate_files(directory_entry.get()), state=tk.DISABLED, width=button_width)
concatenate_button.pack(side=tk.BOTTOM, pady=(5, 0))

root.mainloop()
