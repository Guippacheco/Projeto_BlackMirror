opcaoEscolhida = -1


while(opcaoEscolhida != 0):
    opcaoEscolhida = input(f'''
===========BANCO AZUL================
    INFORME A PERGUNTA ESCOLHIDA:
  -  QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?
   -  QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE
TELEVISÃO?
    - QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA
A NETFLIX NO EPISÓDIO? 
   - COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?
    - QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE
ELA FAZ EM RESPOSTA?
    - QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE
BLACK MIRROR?   
   - O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.
                                                      
=====================================
 : ''')
    if(opcaoEscolhida == "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?"):
         print("Joan fonte")
    elif(opcaoEscolhida == "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?"):
        print("É a IA do computador quântico")
    elif(opcaoEscolhida == "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?"): 
        print("stremberry")
    elif(opcaoEscolhida ==  "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?"):
         print("Quando vai assistir uma série com o noivo")
    elif(opcaoEscolhida == "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?"):
        print("Ela fica chocada e incrédula e Depois tem um ataque de pânico")
    elif(opcaoEscolhida == "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?"):  
        print(f'''A série aborda aspectos cotidianos atuais, sobre aceitação de contrato virtual “termos e condições” sem que seja lido pelo usuário. Assim dando a liberdade para que seus dados sejam usados.
E também as novas tecnologias IA, que podem gerar imagem somente dando scripts textuais
''')
    elif(opcaoEscolhida == "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE."):
        print(f'Termina de forma que mostra o "lado bom" do que aconteceu, no final a personagem principal realizou seu sonho de vida que era ter um café ')
    else:
        print("!!! OPÇÃO INVALIDA !!!")
