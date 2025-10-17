#contatoMolde
class Contato:
    #Molde do contato
    def __init__(self, nome, celular, endereco=""):
        self.nome = nome
        self.celular = celular
        self.endereco = endereco
        self.favoritoCtt = False
    
    # Add/Del favoritos
    def alterar_favorito(self):
        self.favoritoCtt = not self.favoritoCtt

    #Condicionais para criação de celular
    @staticmethod
    def numeroCelular():
        while True:
            celular = input("Digite o número do celular: ").strip()
            if not celular.isdigit():
                print("Erro. Digite apenas números.")
            else:
                if len(celular) == 10:
                        celularFormatado = f"({celular[:2]})9{celular[2:6]}-{celular[6:]}"
                        return celularFormatado
                elif len(celular) == 11:
                        celularFormatado = f"({celular[:2]}){celular[2:7]}-{celular[7:]}"
                        return celularFormatado
                else:
                    print("Quantidade de números inválidos, Digite 10 ou 11 digitos.")

    #Retorno do novo contato
    def __str__(self):
        estrela = "⭐" if self.favoritoCtt else ""
        endereco = "NÃO INFORMADO" if self.endereco == "" else self.endereco
        return f"{self.nome} {self.celular} ENDEREÇO: {endereco} {estrela}"