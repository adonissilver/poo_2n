import tkinter as tk



janela = tk.Tk() #criando a janela
janela.title("Meu programa em Python")
janela.geometry("300x200")
botao=tk.Button(janela, text="Clique aqui", command="mostrar_mensagem")
botao.pack(pady=10)
janela.mainloop()