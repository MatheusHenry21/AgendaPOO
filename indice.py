#indice
class IndiceContato:

    #Localizador do um contato específico
    @staticmethod
    def indice():
        while True:
            try:
                indice = int(input("\nDigite o índice do contato que deseja selecionar: "))
                return indice - 1
            except ValueError:
                print("\nErro! Digite apenas números")
    
    #Opções do menu
    @staticmethod
    def opcao():
        while True:
            try:
                opcao = int(input("\nDigite a opção na qual você deseja ultilizar: "))
                return opcao
            except ValueError:
                print("\nErro. Digite apenas números.")     