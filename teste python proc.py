import tkinter as tk
from tkinter import ttk


class Produto:
    def __init__(self, nome, descricao, valor, disponivel):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.disponivel = disponivel


class CadastroProdutosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")

        self.produtos = []

        self.frame_cadastro = ttk.Frame(self.root, padding="10")
        self.frame_cadastro.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame_cadastro, text="Nome do produto:").grid(row=0, column=0, sticky=tk.W)
        self.entry_nome = ttk.Entry(self.frame_cadastro, width=40)
        self.entry_nome.grid(row=0, column=1, sticky=tk.W)

        ttk.Label(self.frame_cadastro, text="Descrição do produto:").grid(row=1, column=0, sticky=tk.W)
        self.entry_descricao = ttk.Entry(self.frame_cadastro, width=40)
        self.entry_descricao.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(self.frame_cadastro, text="Valor do produto:").grid(row=2, column=0, sticky=tk.W)
        self.entry_valor = ttk.Entry(self.frame_cadastro, width=20)
        self.entry_valor.grid(row=2, column=1, sticky=tk.W)

        ttk.Label(self.frame_cadastro, text="Disponível para venda:").grid(row=3, column=0, sticky=tk.W)
        self.combo_disponivel = ttk.Combobox(self.frame_cadastro, values=["Sim", "Não"], width=17)
        self.combo_disponivel.grid(row=3, column=1, sticky=tk.W)
        self.combo_disponivel.current(0)

        ttk.Button(self.frame_cadastro, text="Cadastrar", command=self.cadastrar_produto).grid(row=4, column=1,
                                                                                               sticky=tk.E)

        self.frame_listagem = ttk.Frame(self.root, padding="10")
        self.frame_listagem.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame_listagem, text="Lista de Produtos").grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.tree_produtos = ttk.Treeview(self.frame_listagem, columns=("Nome", "Valor"), show="headings")
        self.tree_produtos.heading("Nome", text="Nome")
        self.tree_produtos.heading("Valor", text="Valor")
        self.tree_produtos.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

        ttk.Button(self.frame_listagem, text="Novo Produto", command=self.abrir_formulario_cadastro).grid(row=2,
                                                                                                          column=0,
                                                                                                          columnspan=2,
                                                                                                          sticky=tk.E)

    def cadastrar_produto(self):
        nome = self.entry_nome.get()
        descricao = self.entry_descricao.get()
        valor = float(self.entry_valor.get())
        disponivel = True if self.combo_disponivel.get() == "Sim" else False

        produto = Produto(nome, descricao, valor, disponivel)
        self.produtos.append(produto)
        self.atualizar_listagem_produtos()
        self.limpar_campos_formulario()

    def abrir_formulario_cadastro(self):
        self.frame_cadastro.grid()
        self.frame_listagem.grid_remove()

    def atualizar_listagem_produtos(self):
        for item in self.tree_produtos.get_children():
            self.tree_produtos.delete(item)

        for produto in sorted(self.produtos, key=lambda x: x.valor):
            self.tree_produtos.insert("", "end", values=(produto.nome, produto.valor))

    def limpar_campos_formulario(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.combo_disponivel.current(0)


if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroProdutosApp(root)
    root.mainloop()