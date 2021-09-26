import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys,"frozen",False):
    os.chdir(sys._MEIPASS)


class Personagem:
    def __init__(self, nome, dormindo=True, infectado=False, machucado=False):
        self.nome = nome
        self.dormindo = dormindo
        self.infectado = infectado
        self.machucado = machucado
        self.vida = Vida()

    def __str__(self):
        
        if self.dormindo == False:
            dormindo = "acordado"
        else:
            dormindo = "dormindo"

        if self.vida.getVida() == True:
            vida = "vivo"
        else:
            vida = "morto"

        if self.machucado == False:
            machucado = "está bem"
        else:
            machucado = " machucado"

        if self.infectado == True:
            infectado = "está contaminado"
        else:
            infectado = "não está contaminado"

        if self.vida.getVida() == True:
            return f'\033[1;32m{self.nome} está {vida} e {dormindo} {infectado} {machucado} fisicamente.\033[m'
        else:
            return f'\033[1;91m{self.nome} está {vida} {infectado} e {machucado} fisicamente.\033[m'

class Relogio:
    def __init__(self):
        self.dias = 1
        self.horas = 5
        self.minutos = 0

    def __str__(self):
        return f"\033[;1m{self.horas:02d}:{self.minutos:02d} do dia {self.dias:02d}\033[m"

    def avancaTempo(self, horas):
        self.horas += horas
        if self.horas >= 24:
            self.dias += self.horas // 24
            self.horas = self.horas % 24
        

class Texto:
    def __init__(self):
        self.__texto = ''
        self.__estilo = "verde"
        self.__velocidade = 0.02

    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, novo_texto):
        raise ValueError("Impossível escrever texto diretamente, tente um outro método.")

    def escreverTexto(self, texto, estilo='vermelho', velocidade=0.02):
        self.__texto = texto
        self.__estilo = estilo
        self.__velocidade = velocidade
        if self.__estilo == "vermelho":
            for i in list(f'\033[1;91m{self.__texto}\033[m'):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(self.__velocidade)
        elif self.__estilo == 'verde':
            for i in list(f'\033[1;32m{self.__texto}\033[m'):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(self.__velocidade)
        elif self.__estilo == 'negrito':
            for i in list(f'\033[;1m{self.__texto}'):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(self.__velocidade)
        else:
            for i in list(self.__texto):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(self.__velocidade)
        print()

class Vida:
    def __init__(self,vida=True):
        self.__vida = vida

    def getVida(self):
        return self.__vida
    
    def setVida(self,vida):
        
        self.__vida = vida
    



class Morto:
    texto = Texto()
    print("Entrou na clase Morto")

    def __init__(self):
        super().__init__()

    def textoFim(self):
        frase = '''
            ███████████████████████████████████████████████████████████████████████████████████████████
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
            █░██╗░░░██╗░█████╗░░█████╗░███████╗░░███╗░░░███╗░█████╗░██████╗░██████╗░███████╗██╗░░░██╗██
            █░██║░░░██║██╔══██╗██╔══██╗██╔════╝░░████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║██
            █░╚██╗░██╔╝██║░░██║██║░░╚═╝█████╗░░░░██╔████╔██║██║░░██║██████╔╝██████╔╝█████╗░░██║░░░██║██
            █░░╚████╔╝░██║░░██║██║░░██╗██╔══╝░░░░██║╚██╔╝██║██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░░██║██
            █░░░╚██╔╝░░╚█████╔╝╚█████╔╝███████╗░░██║░╚═╝░██║╚█████╔╝██║░░██║██║░░██║███████╗╚██████╔╝██
            █░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝░░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚═════╝░██
            ███████████████████████████████████████████████████████████████████████████████████████████
            '''
            
        texto.escreverTexto(frase, 'vermelho', 0.01)

class Fim(Vida,Morto):
    relogio = Relogio()
    texto = Texto()
    

    
    def __init__(self):
        super().__init__()


    def textoFim(self):
        
        if self.getVida() == True:
            frase = f'''
Após 3 dias de muitas batalhas o exército conseguiu eliminar o os zumbis e aqueles que ainda tinham chance foram vacinados e se recuperaram. 
            '''
            texto.escreverTexto(frase,'verde')
            relogio.avancaTempo(72)
            print(relogio)
            print()
            frase = f' Parabéns!! você conseguiu vencer o Dia Apocalíptico'
            texto.escreverTexto (frase,'verde')
        else:
            Morto.textoFim(self)
            
            
            

import time
import pygame

texto = Texto()
vida1 = Vida()


os.system('cls')
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Projeto/audio.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.7)


opc = 0
print('''
                                        Loading…
                                        █▒▒▒▒▒▒▒▒▒▒▒
                                        █▒▒▒▒▒▒▒▒▒▒▒
''')

time.sleep(1)
os.system('cls')
print('''
                                        10%
                                        ███▒▒▒▒▒▒▒▒▒
                                        ███▒▒▒▒▒▒▒▒▒
''')

time.sleep(1)
os.system('cls')
print('''
                                        30%
                                        █████▒▒▒▒▒▒▒
                                        █████▒▒▒▒▒▒▒
''')

time.sleep(1.5)
os.system('cls')
print('''
                                        50%
                                        ███████▒▒▒▒▒
                                        ███████▒▒▒▒▒
                                
''')

time.sleep(2)
os.system('cls')
print('''
                                        100%
                                        ████████████
                                        ████████████
''')

os.system('cls')
# frase = "\033[;1mInicio do jogo!!\033[m"
frase = '''
                        ██╗███╗░░██╗██╗░█████╗░██╗░█████╗░  ██████╗░░█████╗░  ░░░░░██╗░█████╗░░██████╗░░█████╗░
                        ██║████╗░██║██║██╔══██╗██║██╔══██╗  ██╔══██╗██╔══██╗  ░░░░░██║██╔══██╗██╔════╝░██╔══██╗
                        ██║██╔██╗██║██║██║░░╚═╝██║██║░░██║  ██║░░██║██║░░██║  ░░░░░██║██║░░██║██║░░██╗░██║░░██║
                        ██║██║╚████║██║██║░░██╗██║██║░░██║  ██║░░██║██║░░██║  ██╗░░██║██║░░██║██║░░╚██╗██║░░██║
                        ██║██║░╚███║██║╚█████╔╝██║╚█████╔╝  ██████╔╝╚█████╔╝  ╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝
                        ╚═╝╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░╚════╝░  ╚═════╝░░╚════╝░  ░╚════╝░░╚════╝░░╚═════╝░░╚════╝░
'''
texto.escreverTexto(frase, 'negrito', 0.005)
print()

print()
nome = input("\033[;1mDigite o nome do seu personagem: \033[m")
#pygame.mixer.music.stop()
p1 = Personagem(nome)

relogio = Relogio()
morto = Morto()
fim = Fim()

os.system('cls')
frase = f"\033[;1m{p1.nome} acorda com uma grande explosão, olha no relógio e são {relogio}.\n\033[m"
p1.dormindo = False
pygame.mixer.init() 
pygame.mixer.pre_init() 
pygame.init()
sounds = [] 
sounds.append(pygame.mixer.Sound('Projeto/explosao.mp3'))
for sound in sounds: 
    sound.play()
texto.escreverTexto(frase, 'negrito', 0.03)

while opc == 0:

    print('''\033[;1m
O que você irá fazer?

1 - Vai até a porta para vê o que está acontecendo.
2 - Liga a TV para ver os noticiários.
3 - Fica apavorado e procura um lugar para se esconder.
        \033[m''')
    escolha = input("\033[;1mDigite uma das alternativas acima: \033[m")
    # Primeira opção
    if escolha == "1":
        os.system('cls')
        p1.infectado = True
        p1.machucado = True
        

        sounds = []
        sounds.append(pygame.mixer.Sound('Projeto/zombie-attack.wav'))
        for sound in sounds: 
            sound.play()
        time.sleep(2)
        frase = f"\nVocê se depara com um zumbi, e como não estava preparado ele conseguiu te atingir, você é contaminado e após 1h morre.\n"
        texto.escreverTexto(frase)
        relogio.avancaTempo(1)
        time.sleep(2)

        p1.vida.setVida(False)
        fim.setVida(False)

        print(relogio)
        print()
        print(p1)
        print()
        opc = 1
    #Segunda opção - Seguimento
    elif escolha == "2":
        os.system('cls')
        frase = f"{p1.nome} ligou a TV e os noticiários estão informando que houve uma explosão em um laboratório e um vírus muito perigoso foi disseminado e as pessoas infectadas estão virando zumbis."
        texto.escreverTexto(frase, 'verde', 0.03)

        while opc == 0:

            print(f'''\033[;1m
O que vc fará agora?
1 – Procurar uma arma para se defender e permanecer na sua residência.
2 - Fica com tanto medo e procura um lugar para se esconder.
3 - Procurar uma arma para se defender e ir em busca de mais pessoas que não estão infectadas.
\033[m
            ''')
            escolha = input("\033[;1mDigite uma das alternativas acima: \033[m")
            #Caminho 2->1
            if escolha == "1":
                os.system('cls')
                frase = f'{p1.nome} encontrou uma arma para se defender, os zumbis começaram a invadir sua casa após 1hrs de batalha, você fica cansado e como estava sozinho foi atingido e contaminado e morre após 1hr.'
                p1.infectado = True
                p1.machucado = True
                
                pygame.mixer.music.load("Projeto/zombie-attack.wav")
                pygame.mixer.music.play(2)
                texto.escreverTexto(frase)
                time.sleep(2)
                relogio.avancaTempo(2)
                p1.vida.setVida(False)
                fim.setVida(False)
                print()
                print(relogio)
                print()
                print(p1)
                print()   
                opc = 1

            #Caminho 2->2
            elif escolha == "2":
                os.system('cls')
                p1.infectado = True
                p1.machucado = True
                
                frase = f'{p1.nome} trancou a porta do seu quarto e ficou escondido embaixo da cama. O número de zumbis crescia a cada instantes. Após 2hrs de tentativa eles conseguiram arrombar a porta e você não teve como se defender, foi contaminado fica muito ferido e após 1hr morre.'

                pygame.mixer.init() 
                pygame.mixer.pre_init(44100, -16) 
                pygame.init()
                sounds = [] 
                sounds.append(pygame.mixer.Sound('Projeto/zombie-attack.wav')) 
                sounds.append(pygame.mixer.Sound('Projeto/arrombamento.wav'))               
                for sound in sounds: 
                    sound.play()

                texto.escreverTexto(frase)
                time.sleep(2)
                relogio.avancaTempo(3)
                p1.vida.setVida(False)
                fim.setVida(False)
                print()
                print(relogio)
                print()
                print(p1)
                print()
                opc = 1

            #Caminho 2->3 essa opção da seguimento ao jogo
            elif escolha == '3':
                os.system('cls')
                frase = f'{p1.nome} encontrou uma arma pegou alguns mantimentos e fugiu pela janela aproveitando que não tinha nenhum zumbi por perto. Depois de 5h de caminhada em busca de ajuda, ouvi pessoas gritando pedindo ajuda.'
                texto.escreverTexto(frase, 'verde')

                sounds = []
                sounds.append(pygame.mixer.Sound('Projeto/gritos.wav'))
                sounds.append(pygame.mixer.Sound('Projeto/gritos2.mp3')) 
                sounds.append(pygame.mixer.Sound('Projeto/zombie-attack.wav'))
                for sound in sounds: 
                    sound.play()

                relogio.avancaTempo(5)

                p1.vida.setVida(True)
                print()
                print(relogio)
                print()
                print(p1)
                print()
                #Esse while da inicio a terceira etapa do jogo.
                while opc == 0:
                    print(f'''\033[;1m{p1.nome} tem duas opções:

1 – Você irá até elas, para tentar ajudá-las?
2 – Ignora o pedido de ajuda e continua na sua jornada sozinho?
\033[m
                    ''')
                    escolha = input("\033[;1mDigite uma das alternativas acima: \033[m")
                    #Caminho 2->3->1
                    if escolha == "1":
                        os.system('cls')
                        p1.infectado = True
                        p1.machucado = True
                        sounds = []
                        sounds.append(pygame.mixer.Sound('Projeto/zombie-attack.wav'))
                        sounds.append(pygame.mixer.Sound('Projeto/zumbie.wav'))
                        for sound in sounds: 
                          sound.play()

                        frase = f'{p1.nome} encontra um grupo de 3 pessoas e se junta a elas em uma batalha contra um grupo de zumbis que não para de crescer, depois de 3hrs de batalha você e todos os seus amigos são infectados e não resistem a infecção morrendo após 1hr.'
                        texto.escreverTexto(frase)
                        time.sleep(2)
                        relogio.avancaTempo(4)
                        p1.vida.setVida(False)
                        fim.setVida(False)
                        print()
                        print(relogio)
                        print()
                        print(p1)
                        print()
                        opc = 1
                    #Caminho 2->3->2
                    elif escolha == '2':
                        os.system('cls')

                        frase = f"{p1.nome} ignorou os pedidos de ajuda, pq viu que fora do prédio havia um grupo muito grande de zumbis e que você não teria chance de entrar."
                        time.sleep(2)
                        texto.escreverTexto(frase, 'verde')

                        print(relogio)
                        print()
                        print(p1)
                        print()
                        time.sleep(5)
                        os.system("cls")

                        sounds = []
                        sounds.append(pygame.mixer.Sound('Projeto/zumbie.wav'))
                        for sound in sounds: 
                            sound.play()

                        frase = f'{p1.nome} continua caminhando após 2hrs um grupo de zumbis te cercam, como você estava sozinho não consegui resistir é atingido e infectado.'
                        texto.escreverTexto(frase)
                        print()                        
                        relogio.avancaTempo(2)
                        time.sleep(3)
                        pygame.mixer.music.set_volume(0.5) 
                        sounds.append(pygame.mixer.Sound('Projeto/helicoptero.mp3'))
                        sounds.append(pygame.mixer.Sound('Projeto/tiroteio.mp3')) 
                        sounds.append(pygame.mixer.Sound('Projeto/zombie-attack.wav'))
                        for sound in sounds: 
                            sound.play()

                        frase = f'Enquanto {p1.nome} se retorcia no chão com os efeitos do vírus, um grupo do exército te encontra e destrói o grupo de zumbis, passaram se 1hr.'
                        texto.escreverTexto(frase)
                        time.sleep(3)
                        pygame.mixer.music.load("Projeto/helicoptero.mp3")
                        pygame.mixer.music.play() 
                        relogio.avancaTempo(1)
                        p1.infectado = True
                        p1.machucado = True
                        p1.dormindo = True
                        print()
                        print(relogio)
                        print()
                        print(p1)
                        print()
                        time.sleep(5)
                        
                        pygame.mixer.music.load("Projeto/audio.mp3")
                        pygame.mixer.music.play() 
                        os.system('cls')
                        frase = f"Eles já possuíam a vacina, e aplicaram em você, após isso te levam para a base de resistência e você consegui se recuperar após 12hrs."
                        texto.escreverTexto(frase,'verde')
                        relogio.avancaTempo(12)
                        p1.infectado = False
                        p1.machucado = False
                        p1.dormindo = False
                        print()
                        print(relogio)
                        print()
                        print(p1)
                        print()
                        time.sleep(7)
                        #fim
                        opc = 1

    elif escolha == "3":
        os.system('cls')
        p1.infectado = True
        p1.machucado = True
        
        frase = f'{p1.nome} trancou a porta do seu quarto e ficou escondido embaixo da cama. O número de zumbis crescia a cada instantes. Após 2hrs de tentativa eles conseguiram arrombar a porta e você não teve como se defender, foi contaminado fica muito ferido e após 1hr morre.'

        sounds = []
        pygame.mixer.music.set_volume(0.5) 
        sounds.append(pygame.mixer.Sound('Projeto/arrombamento.wav'))
        sounds.append(pygame.mixer.Sound('Projeto/arrombamento.wav')) 
        sounds.append(pygame.mixer.Sound('Projeto/zombie-attack.wav')) 
        for sound in sounds: 
            sound.play()

        texto.escreverTexto(frase, 'vermelho', 0.06)
        p1.vida.setVida(False)
        fim.setVida(False)
        print()
        time.sleep(2)
        relogio.avancaTempo(3)
        print()
        print(relogio)
        print()
        print(p1)
        print()
        opc = 1
fim.textoFim()
print("\033[;1mPrograma Finalizado!!\033[m")
