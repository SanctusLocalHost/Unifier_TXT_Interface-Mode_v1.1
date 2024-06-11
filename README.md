# File_Unifier

# Agrupador de Arquivos de Texto

Este é um script em Python criado inicialmente para Agrupar Arquivos da Bipagem de um Scanner de Códigos de Barra. Permite Concatenar o conteúdo de todos os arquivos de texto em um diretório selecionado.

## Funcionalidades

- Concatena o conteúdo de todos os arquivos de texto em um único arquivo.
- Interface gráfica usando Tkinter para selecionar o diretório e iniciar a concatenação.

## Uso

1. Execute o Script usando alguma IDE Python.
2. Selecione o diretório contendo os arquivos de texto que você deseja concatenar.
3. Clique no botão "Selecionar Diretório" para escolher o diretório.
4. Após selecionar o diretório, o botão "Concatenar" será ativado.
5. Clique no botão "Concatenar" para iniciar o processo de concatenação.
6. O arquivo resultante será salvo no diretório selecionado com o nome "CONTEÚDO AGRUPADO!!!.txt".

## Requisitos

- Python 3.x
- Tkinter (normalmente incluído na distribuição padrão do Python)

```python
import os
import tkinter as tk
from tkinter import filedialog, messagebox

