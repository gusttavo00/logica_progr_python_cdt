class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        self.reservado = False

    def __str__(self):
        if self.reservado:
            status = "Reservado"
        elif not self.disponivel:
            status = "Emprestado"
        else:
            status = "Disponível"

        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {status}"

    def devolver(self):
        if not self.disponivel or self.reservado:
            self.disponivel = True
            self.reservado = False
            return f"O livro '{self.titulo}' foi devolvido."
        return f"O livro '{self.titulo}' já está disponível."

    def reservar(self):
        if self.disponivel:
            self.reservado = True
            self.disponivel = False
            return f"O livro '{self.titulo}' foi reservado."
        return f"O livro '{self.titulo}' não pode ser reservado."


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        return f"O livro '{livro.titulo}' foi adicionado à biblioteca."

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            return f"O livro '{livro.titulo}' foi removido da biblioteca."
        return f"O livro '{livro.titulo}' não está na biblioteca."

    def listar_livros(self):
        if not self.livros:
            return "Nenhum livro na biblioteca."
        return "\n".join(str(livro) for livro in self.livros)
