#gerenciador

import contatoMolde, indice

class GerenciadorDeContatos:

    #Lista de contatos
    def __init__(self):
        self.__agenda = []

    def add_contato(self):
        nome = input("\nDigite o nome da pessoa: ").strip().title()
        celular = contatoMolde.Contato.numeroCelular()
        endereco = input("Digite o endereço dela(Opcional): ").capitalize().strip()
        novoContato = contatoMolde.Contato(nome, celular, endereco)
        self.__agenda.append(novoContato)
        print(f"\nO contato '{nome}' foi adicionado com sucesso!")

    def listar_contatos(self):
        if not self.__agenda:
            print("\nNão há nenhum contato nessa agenda!")
            return
        
        for i, contato in enumerate(self.__agenda, start=1):
            print(f"\n{i} - {contato}")

    def atualizar_contatos(self):

        if not self.__agenda:
            print("\nNão há contatos cadastrados nessa lista!")
            return
        
        self.listar_contatos()

        indiceLocal = indice.IndiceContato.indice()

        if 0 <= indiceLocal < len(self.__agenda):
            contato = self.__agenda[indiceLocal]

            novoNome = input(f"\nDeseja alterar o nome?(Enter para manter '{contato.nome}'): ").strip().title()
            if novoNome != "":
                contato.nome = novoNome
                
            novoCelular = input(f"Deseja alterar o celular?(Enter para manter '{contato.celular}'): ")
            if novoCelular != "":
                contato.celular = contatoMolde.Contato.numeroCelular()

            novoEndereco = input(f"Deseja alterar o endereço?(Enter para manter '{contato.endereco}'): ").strip().capitalize()
            if novoEndereco != "":
                contato.endereco = novoEndereco

            print("\nContato atualizado com sucesso")

        else:
            print("\nIndice inválido!")
        
    def remover_contatos(self):
        if not self.__agenda:
            print("\nNão há contatos cadastrados nessa lista!")
            return
        
        self.listar_contatos()
        local = indice.IndiceContato.indice()

        if 0 <= local < len(self.__agenda):
            contatoRemover = self.__agenda.pop(local)
            print(f"\nO contato '{contatoRemover.nome}' foi excluído com sucesso!")
        else: 
            print("\nÍndice inválido!")
            
    def favoritar(self):
        if not self.__agenda:
            print("\nNão há contatos cadastrados nessa lista!")
            return

        self.listar_contatos()
        local = indice.IndiceContato.indice()
        
        if 0 <= local < len(self.__agenda):
            contato = self.__agenda[local]
            contato.alterar_favorito()
            status = "adicionado aos" if contato.favoritoCtt else "removido dos"
            print(f"\nO contato '{contato.nome} foi {status} favoritos.")
        else:
            print("\nÍndice inválido!\n")

    def buscar_por_nome(self):
        if not self.__agenda:
            print("\nNão há contatos cadastrados nessa lista!")
            return

        escolhaNome = input("\nDigite o nome da pessoa: ").strip()

        encontrado = False
        for contato in self.__agenda:
            if escolhaNome.lower() in contato.nome.lower():
                print("\n              CONTATO ENCONTRADO!\n")
                print(f"{contato}")
                encontrado = True
        if not encontrado:
                print(f"\nO contato '{escolhaNome}' não está cadastrado nessa lista.")