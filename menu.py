#menu
from os import system
import gerenciador, indice
system('cls')

#menu principal        
def menu():

    agenda = gerenciador.GerenciadorDeContatos()
    while True:
        print("\n   --- MENU ---")
        print("1 - Adicionar contatos")
        print("2 - Listar contatos")
        print("3 - Atualizar contatos")
        print("4 - Remover contatos")
        print("5 - Favoritar Contatos")
        print("6 - Buscar pelo nome")
        print("7 - Sair")

        opcao = indice.IndiceContato.opcao()

        if opcao == 7:
            print("\nSaindo... até logo!")
            break

        elif opcao == 1:
            agenda.add_contato()

        elif opcao == 2:
            agenda.listar_contatos()

        elif opcao == 3:
            agenda.atualizar_contatos()

        elif opcao == 4:
            agenda.remover_contatos()

        elif opcao == 5:
            agenda.favoritar()
                
        elif opcao == 6:
            agenda.buscar_por_nome()

        else:
            print("Não há essa opção, tente novamente.")

menu()