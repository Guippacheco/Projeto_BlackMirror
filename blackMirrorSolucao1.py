opcaoEscolhida = -1


while(opcaoEscolhida != 0):
    opcaoEscolhida = int(input(f'''
===========BANCO AZUL================
    INFORME A PERGUNTA ESCOLHIDA:
    [1] - QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?
    [2] - QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE
TELEVISÃO?
    [3] - QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA
A NETFLIX NO EPISÓDIO? 
    [4] - COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?
    [5] - QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE
ELA FAZ EM RESPOSTA?
    [6] - QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE
BLACK MIRROR?   
    [7] - O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK
MIRROR? EXPLIQUE.
                                                      
=====================================
 : '''))
    if(opcaoEscolhida == 1):
        print("Joan fonte")
    
    elif(opcaoEscolhida == 2):
        print("É a IA do computador quântico")
    elif(opcaoEscolhida == 3):
        print("stremberry")
    elif(opcaoEscolhida == 4):
        print("Quando vai assistir uma série com o noivo")
    elif(opcaoEscolhida == 5):
        print("Ela fica chocada e incrédula e Depois tem um ataque de pânico")
    elif(opcaoEscolhida == 6):
        print(f'''A série aborda aspectos cotidianos atuais, sobre aceitação de contrato virtual “termos e condições” sem que seja lido pelo usuário. Assim dando a liberdade para que seus dados sejam usados.
E também as novas tecnologias IA, que podem gerar imagem somente dando scripts textuais
''')
    elif(opcaoEscolhida == 7):
        print(f'Termina de forma que mostra o "lado bom" do que aconteceu, no final a personagem principal realizou seu sonho de vida que era ter um café ')    

    else:
        print("!!! OPÇÃO INVALIDA !!!")
