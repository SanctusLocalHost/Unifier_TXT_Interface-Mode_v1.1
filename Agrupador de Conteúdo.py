import os
import tkinter as tk
from tkinter import filedialog, messagebox

def concatenate_files(directory):
    output_filename = 'CONTEÚDO AGRUPADO!!!.txt'
    output_filepath = os.path.join(directory, output_filename)

    try:
        with open(output_filepath, 'w') as outfile:
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path) and file_name != "Concatenador_de_Arquivos_de_Texto.py":
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read())

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
root.title("Concatenador de Arquivos de Texto")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

label = tk.Label(frame, text="Selecione o Diretório com os Arquivos de Texto:")
label.pack(pady=(0, 10))

directory_entry = tk.Entry(frame, width=50)
directory_entry.pack(side=tk.TOP, padx=(0, 10))

browse_button = tk.Button(frame, text="Selecionar Diretório", command=select_directory)
browse_button.pack(side=tk.TOP, pady=(0, 5), fill=tk.X)

concatenate_button = tk.Button(frame, text="Concatenar", command=lambda: concatenate_files(directory_entry.get()), state=tk.DISABLED)
concatenate_button.pack(side=tk.BOTTOM, pady=(5, 0), fill=tk.X)

root.mainloop()
