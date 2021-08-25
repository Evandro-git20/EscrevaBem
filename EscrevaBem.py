import random
from tkinter import *
import pygame
import cv2
from tkinter import messagebox

pygame.init()

# INTRODUÇÃO TOP TRENDS EDUCAÇÃO
intro = cv2.VideoCapture('videos/intro.mp4')

while intro.isOpened():
    ret, janela = intro.read()

    if ret:
        cv2.imshow('ESCREVA BEM', janela)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
intro.release()
cv2.destroyAllWindows()

# JANELA E SUAS VARIÁVEIS

janela = Tk()  # CRIAR JANELA

janela.title("ESCREVA BEM")  # TÍTULO DA JANELA

janela.iconbitmap('imagens/logojogo.ico') # ÍCONE DA JANELA

janela.geometry("800x600+275+50")  # TAMANHO E POSIÇÃO DA JANELA

janela.resizable(width=False, height=False)  # RECONFIGURAR TAMANHO DA JANELA

janela.configure(bg='white')  # COR DA JANELA

# MÚSICA DO JOGO
def musicaJogo():
    pygame.mixer.music.load('sons/musicajogo1.mp3')
    pygame.mixer.music.play(loops=10)

#SAIR DO JOGO
def quit():
    pygame.mixer.music.stop()
    janela.quit()

# BOTÕES DE MUTAR E DESMUTAR
muteimg = PhotoImage(file='imagens/desmute3.png')
label3 = Label(janela, image=muteimg)
label3.pack()
label3.place(x=5, y=6)

desmuteimg = PhotoImage(file='imagens/mute3.png')
label4 = Label(janela, image=desmuteimg)
label4.pack()
label4.place(x=5, y=6)

def mutar():
    pygame.mixer.music.pause()
    desmute = Button(janela, image=desmuteimg, bg='black', command=desmutar)
    desmute.place(x=5, y=6)

def desmutar():
    pygame.mixer.music.unpause()
    mute = Button(janela, image=muteimg, bg='black', command=mutar)
    mute.place(x=5, y=6)

# DEPÓSITO DE PERGUNTAS

questoes = [["IREI AO RESTAURANTE...", "ALMOSSAR", "AUMOÇAR", "AUMOSSAR", "ALMOÇAR"],
                ["IREI CONTATAR MEU...", "ADEVOGADO", "ADIVOGADO", "ADIVOGADU", "ADVOGADO"],
                ["COMPREI 200 GRAMAS DE...", "MORTADELLA", "MORTANDELA", "MOTADELA", "MORTADELA"],
                ["VOU DAR UM PASSEIO DE...", "BICECLETA", "BECICLETA", "BECECLETA", "BICICLETA"],
                ["É SEMPRE UM ... RECEBÊ-LO(A) EM MINHA CASA!", "PRASER", "PRAZÊ", "PRASÊ", "PRAZER"]]

# REMOVER ELEMENTOS DA JANELA
def limparElementos():
    elementos = janela.grid_slaves()
    for e in elementos:
        e.destroy()

# INICIAR JOGO
class IniciarJogo:
    def __init__(self, quest):
        limparElementos()
        pygame.mixer.music.pause()

        # BACKGROUND
        self.fundo = PhotoImage(file='imagens/bg.png')
        Label(janela, image=self.fundo).place(relwidth=1, relheight=1)

        # ACRESCENTAR PERGUNTAS
        self.Perguntar = []
        for n in quest:
            self.Perguntar.append(n)
        self.travar = False

        # CONTADOR DE RESPOSTAS CORRETAS
        self.correta = 0

        # CONTADOR DE RESPOSTAS ERRADAS
        self.errada = 0

        #------------------------------------- BOTÃO DE AVANÇAR ---------------------------------#

        self.avancar = Button(janela, width=7, height=1,
                      text="Próxima",
                      bg='blue',
                      fg='white',
                      font=("BigNoodleTitling", 22),
                      command=self.Questao)

        # TOTAL DE PERGUNTAS
        self.numero = 0
        self.totalPerg = 5
        self.Questao()

    # AVANÇAR QUESTÃO
    def Questao(self):
        self.avancar.place(x=352, y=1000)

        # RANDOMIZADOR DE PERGUNTAS
        if len(self.Perguntar) > 0 and self.numero < self.totalPerg:
            self.numero += 1
            self.travar = False
            NumAleatorio = random.randint(0, len(self.Perguntar) - 1)

            # FRASE AUXÍLIO
            PerguntarText = self.Perguntar[NumAleatorio][0]

            self.proxQuest = self.Perguntar[NumAleatorio][-1]
            respostas = []

            for i in range(1, 5):
                respostas.append(self.Perguntar[NumAleatorio][i])

            # ------------------------------ EMBARALHAR RESPOSTAS ------------------------------ #

            random.shuffle(respostas)

            self.alternativa1 = respostas[0]
            self.alternativa2 = respostas[1]
            self.alternativa3 = respostas[2]
            self.alternativa4 = respostas[3]

            # ------------------------ CONFIGURAÇÕES DA FRASE DE AUXÍLIO ----------------------- #

            Questao = Entry(janela,
                            font=('BigNoodleTitling', 30),
                            bg='white',
                            fg='black',
                            width=45,
                            justify='center',
                            highlightbackground="#37d3ff")
            Questao.insert(END, PerguntarText)
            Questao.grid(row=0,
                         column=0,
                         columnspan=4,
                         pady=4)
            Questao.place(x=60, y=90)

            # -------------------------- CONFIGURAÇÕES DOS BOTÕES DE RESPOSTA -------------------------- #
            self.opcao1 = Button(janela,
                                 text=self.alternativa1,
                                 font=("BigNoodleTitling", 26),
                                 width=24,  # BOTÃO 1
                                 height=2,
                                 command=self.fiscalizar1,
                                 bg='#e6ac00', fg='black')
            self.opcao1.place(x=60, y=200)

            # ---------------------------------------------------------------------------------------#

            self.opcao2 = Button(janela,
                                 text=self.alternativa2,
                                 font=("BigNoodleTitling", 26),
                                 width=24,  # BOTÃO 2
                                 height=2,
                                 command=self.fiscalizar2,
                                 bg='#e6ac00', fg='black')
            self.opcao2.place(x=415, y=200)

            # ---------------------------------------------------------------------------------------#

            self.opcao3 = Button(janela,
                                 text=self.alternativa3,
                                 font=("BigNoodleTitling", 26),
                                 width=24,  # BOTÃO 3
                                 height=2,
                                 command=self.fiscalizar3,
                                 bg='#e6ac00', fg='black')
            self.opcao3.place(x=60, y=330)

            # ---------------------------------------------------------------------------------------#

            self.opcao4 = Button(janela,
                                 text=self.alternativa4,
                                 font=("BigNoodleTitling", 26),
                                 width=24,  # BOTÃO 4
                                 height=2,
                                 command=self.fiscalizar4,
                                 bg='#e6ac00', fg='black')
            self.opcao4.place(x=415, y=330)

            # ---------------------------------------------------------------------------------------#

            if self.alternativa1 == self.proxQuest:
                self.BtProxQuestao = self.opcao1
            elif self.alternativa2 == self.proxQuest:
                self.BtProxQuestao = self.opcao2
            elif self.alternativa3 == self.proxQuest:
                self.BtProxQuestao = self.opcao3
            elif self.alternativa4 == self.proxQuest:
                self.BtProxQuestao = self.opcao4
                self.Perguntar.pop(NumAleatorio)
        else:
            limparElementos()

            self.white = PhotoImage(file='imagens/resultado.png')
            Label(janela, image=self.white).place(relwidth=1, relheight=1)

            # ----------------------------------- CONFIGURAÇÕES DO RESULTADO ------------------------------------- #

            lb = Label(janela, bg='white', fg='black',
                       text=f'{str(self.correta)}' + f'\n{str(self.errada)}',
                       font=('BigNoodleTitling', 55),
                       justify='center')
            lb.grid(column=0,
                    row=0,  # CONTADOR DE CORRETAS E INCORRETAS
                    padx=50,
                    pady=(188, 15))

            # --------------------------------------------------------------------------------------------------- #

            btmenu = Button(janela,
                            text="RETORNAR",
                            bg='#bfbfbf',
                            font=('BigNoodleTitling', 25),
                            command=criarMenu)  # BOTÃO DE VOLTAR AO MENU
            btmenu.grid(column=0,
                        row=1,
                        pady=150)
            btmenu.place(x=350, y=500)

            # --------------------------------------------------------------------------------------------------- #

    def fiscalizar1(self):
        if not self.travar:
            if self.proxQuest != self.alternativa1:
                self.opcao1.configure(bg='#b30000', fg='#f2f2f2')
                pygame.mixer.music.load('sons/errado.mp3')
                pygame.mixer.music.play()
                self.errada += 1
                self.avancar.place(x=352, y=510)
            else:
                self.opcao1.configure(bg='#006622', fg='#f2f2f2')
                pygame.mixer.music.load('sons/correto.mp3')
                pygame.mixer.music.play()
                self.correta += 1
                self.BtProxQuestao.configure(bg='#006622')
                self.travar = True
                self.avancar.place(x=352, y=510)

    def fiscalizar2(self):
        if not self.travar:
            if self.proxQuest != self.alternativa2:
                self.opcao2.configure(bg='#b30000', fg='#f2f2f2')
                pygame.mixer.music.load('sons/errado.mp3')
                pygame.mixer.music.play()
                self.errada += 1
                self.avancar.place(x=352, y=510)

            else:
                self.opcao2.configure(bg='#006622', fg='#f2f2f2')
                pygame.mixer.music.load('sons/correto.mp3')
                pygame.mixer.music.play()
                self.correta += 1
                self.BtProxQuestao.configure(bg='#006622')
                self.travar = True
                self.avancar.place(x=352, y=510)

    def fiscalizar3(self):
        if not self.travar:
            if self.proxQuest != self.alternativa3:
                self.opcao3.configure(bg='#b30000', fg='#f2f2f2')
                pygame.mixer.music.load('sons/errado.mp3')
                pygame.mixer.music.play()
                self.errada += 1
                self.avancar.place(x=352, y=510)

            else:
                self.opcao3.configure(bg='#006622', fg='#f2f2f2')
                pygame.mixer.music.load('sons/correto.mp3')
                pygame.mixer.music.play()
                self.correta += 1
                self.BtProxQuestao.configure(bg='#006622')
                self.travar = True
                self.avancar.place(x=352, y=510)

    def fiscalizar4(self):
        if not self.travar:
            if self.proxQuest != self.alternativa4:
                self.opcao4.configure(bg='#b30000', fg='#f2f2f2')
                pygame.mixer.music.load('sons/errado.mp3')
                pygame.mixer.music.play()
                self.errada += 1
                self.avancar.place(x=352, y=510)

            else:
                self.opcao4.configure(bg='#006622', fg='#f2f2f2')
                pygame.mixer.music.load('sons/correto.mp3')
                pygame.mixer.music.play()
                self.correta += 1
                self.BtProxQuestao.configure(bg='#006622')
                self.travar = True
                self.avancar.place(x=352, y=510)

# ADICIONAR PERGUNTAS

# MENU
class Menu:
    def __init__(self):
        limparElementos()
        self.fundo = PhotoImage(file='imagens/menu.png')
        Label(janela, image=self.fundo).place(relwidth=1, relheight=1)

        mutar()
        desmutar()

        # ------------------------------------ BOTÃO DE JOGADOR ------------------------------------ #

        self.Opcao1 = Button(janela, text="JOGADOR",
                              padx=17, pady=19, width=20,
                              font=('BigNoodleTitling', 26),
                              bg='#e6ac00', fg='black',
                              activebackground='#006622',
                              activeforeground='white', command=self.selecionarJogador)
        self.Opcao1.grid(column=0, row=0, padx=420, pady=170)

        # ------------------------------------- BOTÃO DE SAIR ------------------------------------- #

        self.Sair = Button(janela, text='SAIR', width=20,
                           padx=17, pady=19,
                           font=('BigNoodleTitling', 26),
                           bg='#e6ac00', fg='black',
                           activebackground='#b30000',
                           activeforeground='white',
                           command=janela.destroy)
        self.Sair.place(x=420, y=330)

        self.Sair.bind('<Enter>', self.hover)
        self.Sair.bind('<Leave>', self.hover_leave)

        self.Opcao1.bind('<Enter>', self.hover5)
        self.Opcao1.bind('<Leave>', self.hover_leave5)

    def hover(self, e):
        self.Sair.configure(bg='white')
    def hover_leave(self, e):
        self.Sair.configure(bg='#e6ac00')

    def hover5(self, e):
        self.Opcao1.configure(bg='white')
    def hover_leave5(self, e):
        self.Opcao1.configure(bg='#e6ac00')

    def selecionarJogador(self):

        self.janelao = Tk()
        self.janelao.iconbitmap('imagens/logojogo.ico')
        self.janelao.geometry('800x600+275+50')
        self.janelao.title('JOGADOR')
        self.janelao.resizable(width=False, height=False)

        labelPerg = Label(self.janelao, text='ESCOLHA A OPÇÃO DE JOGADOR',
                          font=('BigNoodleTitling', 40))
        labelPerg.place(x=170, y=15)

        # ------------------------------------  BOTÃO DE PROFESSOR  ----------------------------------- #

        self.Professor = Button(self.janelao, text="PROFESSOR",
                              padx=17, pady=19, width=20,
                              font=('BigNoodleTitling', 26),
                              bg='#e6ac00', fg='black',
                              activebackground='#006622',
                              activeforeground='white', command=self.login)
        self.Professor.place(x=250,y=120)

        # -------------------------------------   BOTÃO DE ALUNO   ------------------------------------ #

        self.Aluno= Button(self.janelao, text="ALUNO",
                              padx=17, pady=19, width=20,
                              font=('BigNoodleTitling', 26),
                              bg='#e6ac00', fg='black',
                              activebackground='#006622',
                              activeforeground='white', command=self.criarQuiz)
        self.Aluno.place(x=250,y=270)

        # ------------------------------------   BOTÃO DE VOLTAR   ------------------------------------- #

        self.Voltar = Button(self.janelao, text="VOLTAR",
                              padx=17, pady=19, width=20,
                              font=('BigNoodleTitling', 26),
                              bg='#e6ac00', fg='black',
                              activebackground='#006622',
                              activeforeground='white', command=self.janelao.destroy)
        self.Voltar.place(x=250,y=420)

        self.Professor.bind('<Enter>', self.hover7)
        self.Professor.bind('<Leave>', self.hover_leave7)

        self.Aluno.bind('<Enter>', self.hover8)
        self.Aluno.bind('<Leave>', self.hover_leave8)

        self.Voltar.bind('<Enter>', self.hover9)
        self.Voltar.bind('<Leave>', self.hover_leave9)

    def hover7(self, e):
        self.Professor.configure(bg='white')
    def hover_leave7(self, e):
        self.Professor.configure(bg='#e6ac00')

    def hover8(self, e):
        self.Aluno.configure(bg='white')
    def hover_leave8(self, e):
        self.Aluno.configure(bg='#e6ac00')

    def hover9(self, e):
        self.Voltar.configure(bg='white')
    def hover_leave9(self, e):
        self.Voltar.configure(bg='#e6ac00')

    def mestre(self):
        self.janelao.destroy()
        self.janela1 = Tk()
        self.janela1.iconbitmap('imagens/logojogo.ico')
        self.janela1.geometry('800x600+275+50')
        self.janela1.title('PROFESSOR')
        self.janela1.resizable(width=False, height=False)

        self.BotPersonalizar = Button(self.janela1, text="PERSONALIZAR",
                                      padx=17, pady=19, width=20,
                                      font=('BigNoodleTitling', 26),
                                      bg='#e6ac00', fg='black',
                                      activebackground='#660080',
                                      activeforeground='white', command=self.adicionarQuestoes)
        self.BotPersonalizar.place(x=420, y=100)

        # --------------------------------------- BOTÃO DE INCIAR ---------------------------------------- #

        self.Iniciar = Button(self.janela1, text="INICIAR",
                              padx=17, pady=19, width=20,
                              font=('BigNoodleTitling', 26),
                              bg='#e6ac00', fg='black',
                              activebackground='#006622',
                              activeforeground='white', command=self.criarQuiz2)
        self.Iniciar.place(x=420, y=250)

        # ----------------------------------------- BOTÃO DE SAIR ---------------------------------------- #

        self.Sair1 = Button(self.janela1, text='SAIR', width=20,
                            padx=17, pady=19,
                            font=('BigNoodleTitling', 26),
                            bg='#e6ac00', fg='black',
                            activebackground='#b30000',
                            activeforeground='white',
                            command=self.delete)
        self.Sair1.place(x=420, y=400)

        self.BotPersonalizar.bind('<Enter>', self.hover6)
        self.BotPersonalizar.bind('<Leave>', self.hover_leave6)

        self.Iniciar.bind('<Enter>', self.hover2)
        self.Iniciar.bind('<Leave>', self.hover_leave2)

        self.Sair1.bind('<Enter>', self.hover1)
        self.Sair1.bind('<Leave>', self.hover_leave1)

    def hover6(self, e):
        self.BotPersonalizar.configure(bg='white')

    def hover_leave6(self, e):
        self.BotPersonalizar.configure(bg='#e6ac00')

    def hover2(self, e):
        self.Iniciar.configure(bg='white')

    def hover_leave2(self, e):
        self.Iniciar.configure(bg='#e6ac00')

    def hover1(self, e):
        self.Sair1.configure(bg='white')

    def hover_leave1(self, e):
        self.Sair1.configure(bg='#e6ac00')

    def login(self):
        self.janela2 = Tk()
        self.janela2.iconbitmap('imagens/logojogo.ico')
        self.janela2.geometry('800x600+275+50')
        self.janela2.title('LOGIN')
        self.janela2.resizable(width=False, height=False)

        self.label_prof = Label(self.janela2, text='PROFESSOR', font=('BigNoodleTitling', 36))
        self.label_prof.place(x= 320, y=10)
        self.label_login = Label(self.janela2, text='Login:', font=('BigNoodleTitling', 26))
        self.label_login.place(x=160, y=100)
        self.entry_login = Entry(self.janela2, width=50)
        self.entry_login.place(x=250, y=115)
        self.label_senha = Label(self.janela2, text='Senha:', font=('BigNoodleTitling', 26))
        self.label_senha.place(x=160, y=150)
        self.entry_senha = Entry(self.janela2, width=50)
        self.entry_senha.place(x=250, y=165)

        # ----------------------------------------- BOTÃO DE LOGIN ---------------------------------------- #

        self.blogin = Button(self.janela2, text="LOGIN",
                                      padx=17, pady=19, width=20,
                                      font=('BigNoodleTitling', 26),
                                      bg='#e6ac00', fg='black',
                                      activebackground='#660080',
                                      activeforeground='white', command=self.mestre)
        self.blogin.place(x=250, y=230)

        # ----------------------------------------- BOTÃO DE CADASTRO ---------------------------------------- #

        self.bcadastro = Button(self.janela2, text="FAÇA SEU CADASTRO",
                                      padx=17, pady=19, width=20,
                                      font=('BigNoodleTitling', 26),
                                      bg='#e6ac00', fg='black',
                                      activebackground='#660080',
                                      activeforeground='white', command=self.cadastro)
        self.bcadastro.place(x=250, y=355)

        # ----------------------------------------- BOTÃO DE VOLTAR ---------------------------------------- #

        self.bvoltar = Button(self.janela2, text="VOLTAR",
                                      padx=17, pady=19, width=20,
                                      font=('BigNoodleTitling', 26),
                                      bg='#e6ac00', fg='black',
                                      activebackground='#660080',
                                      activeforeground='white', command=self.janela2.destroy)
        self.bvoltar.place(x=250, y=480)

    def cadastro(self):
        self.janela2.destroy()
        self.janela3 = Tk()
        self.janela3.iconbitmap('imagens/logojogo.ico')
        self.janela3.geometry('800x600+275+50')
        self.janela3.title('LOGIN')
        self.janela3.resizable(width=False, height=False)

        self.label_prof = Label(self.janela3, text='PROFESSOR', font=('BigNoodleTitling', 36))
        self.label_prof.place(x=320, y=10)
        self.label_login = Label(self.janela3, text='NOME:', font=('BigNoodleTitling', 26))
        self.label_login.place(x=160, y=100)
        self.entry_login = Entry(self.janela3, width=50)
        self.entry_login.place(x=250, y=115)
        self.label_senha = Label(self.janela3, text='CPF:', font=('BigNoodleTitling', 26))
        self.label_senha.place(x=160, y=150)
        self.entry_senha = Entry(self.janela3, width=50)
        self.entry_senha.place(x=250, y=165)
        self.label_login = Label(self.janela3, text='CFEP:', font=('BigNoodleTitling', 26))
        self.label_login.place(x=160, y=200)
        self.entry_login = Entry(self.janela3, width=50)
        self.entry_login.place(x=250, y=215)
        self.label_senha = Label(self.janela3, text='EMAIL:', font=('BigNoodleTitling', 26))
        self.label_senha.place(x=160, y=250)
        self.entry_senha = Entry(self.janela3, width=50)
        self.entry_senha.place(x=250, y=265)

        # ----------------------------------------- BOTÃO DE CADASTRAR ---------------------------------------- #

        self.bcadastrar = Button(self.janela3, text="CADASTRAR",
                             padx=17, pady=19, width=20,
                             font=('BigNoodleTitling', 26),
                             bg='#e6ac00', fg='black',
                             activebackground='#660080',
                             activeforeground='white')
        self.bcadastrar.place(x=250, y=320)

        # ----------------------------------------- BOTÃO DE VOLTAR ---------------------------------------- #

        self.bvolte = Button(self.janela3, text="VOLTAR",
                                padx=17, pady=19, width=20,
                                font=('BigNoodleTitling', 26),
                                bg='#e6ac00', fg='black',
                                activebackground='#660080',
                                activeforeground='white', command=self.janela3.destroy)
        self.bvolte.place(x=250, y=450)

        # ------------------------------------- BOTÃO DE PRSONALIZAR ------------------------------------- #

    def adicionarQuestoes(self):
        self.janelap = Tk()
        self.janelap.iconbitmap('imagens/logojogo.ico')
        self.janelap.geometry('800x600+275+50')
        self.janelap.title('ADICIONE NOVAS PERGUNTAS')
        self.janelap.resizable(width=False, height=False)

        labelPerg = Label(self.janelap, text='ESCREVA A FRASE DA QUESTÃO',
                          font=('BigNoodleTitling', 20))
        labelPerg.place(x=285, y=15)

        labelRespErrada = Label(self.janelap, text='ESCREVA AS ALTERNATIVAS INCORRETAS',
                                font=('BigNoodleTitling', 20))
        labelRespErrada.place(x=250, y=130)

        labelRespCorreta = Label(self.janelap, text='ESCREVA A ALTERNATIVA CORRETA',
                                 font=('BigNoodleTitling', 20))
        labelRespCorreta.place(x=275, y=350)

        self.box1 = Entry(self.janelap,
                          font=('BigNoodleTitling', 30),
                          bg='white',
                          fg='black',
                          width=45,
                          justify='center',
                          highlightbackground="#37d3ff")
        self.box1.place(x=60, y=65)

        self.box2 = Entry(self.janelap,
                          font=("BigNoodleTitling", 26),
                          width=24, justify='center',
                          bg='#cc0000', fg='white'
                          )

        self.box2.place(x=230, y=180)

        self.box3 = Entry(self.janelap,
                          font=("BigNoodleTitling", 26),
                          width=24, justify='center',
                          bg='#cc0000', fg='white'
                          )
        self.box3.place(x=230, y=230)

        self.box4 = Entry(self.janelap,
                          font=("BigNoodleTitling", 26),
                          width=24, justify='center',
                          bg='#cc0000', fg='white'
                          )
        self.box4.place(x=230, y=280)

        self.box5 = Entry(self.janelap,
                          font=("BigNoodleTitling", 26),
                          width=24, justify='center',
                          bg='#004d00', fg='white')

        self.box5 = Entry(self.janelap,
                          font=("BigNoodleTitling", 26),
                          width=24, justify='center',
                          bg='#004d00', fg='white'
                          )
        self.box5.place(x=230, y=390)

        #----------------------------------------- BOTÃO DE ADICIONAR ---------------------------------------- #


        self.BotAdicionar = Button(self.janelap, text="ADICIONAR", width=20, height=1,
                                   font=('BigNoodleTitling', 25),
                                   bg='#003300', fg='white',
                                   activebackground='#006622',
                                   activeforeground='white', command=self.adicionando)
        self.BotAdicionar.place(x=130, y=520)

        #----------------------------------------- BOTÃO DE FECHAR ---------------------------------------- #


        self.BotFechar = Button(self.janelap, text="FECHAR", width=20, height=1,
                                font=('BigNoodleTitling', 25),
                                bg='#990000', fg='white',
                                activebackground='#e60000',
                                activeforeground='white', command=self.janelap.destroy)
        self.BotFechar.place(x=420, y=520)

        self.BotAdicionar.bind('<Enter>', self.hover3)
        self.BotAdicionar.bind('<Leave>', self.hover_leave3)
        self.BotFechar.bind('<Enter>', self.hover4)
        self.BotFechar.bind('<Leave>', self.hover_leave4)

    def hover3(self, e):
        self.BotAdicionar.configure(bg='green')

    def hover_leave3(self, e):
        self.BotAdicionar.configure(bg='#003300')

    def hover4(self, e):
        self.BotFechar.configure(bg='red')

    def hover_leave4(self, e):
        self.BotFechar.configure(bg='#990000')

    def adicionando(self):

        b1 = self.box1.get()
        b2 = self.box2.get()
        b3 = self.box3.get()
        b4 = self.box4.get()
        b5 = self.box5.get()

        self.novas = [b1, b2, b3, b4, b5]

        if b1 == '':
            messagebox.showerror("ERRO", "VOCÊ NÃO PREENCHEU TODOS OS CAMPOS!", parent=self.janelap)

        elif b2 == '':
            messagebox.showerror("ERRO", "VOCÊ NÃO PREENCHEU TODOS OS CAMPOS!", parent=self.janelap)

        elif b3 == '':
            messagebox.showerror("ERRO", "VOCÊ NÃO PREENCHEU TODOS OS CAMPOS!", parent=self.janelap)

        elif b4 == '':
            messagebox.showerror("ERRO", "VOCÊ NÃO PREENCHEU TODOS OS CAMPOS!", parent=self.janelap)

        elif b5 == '':
            messagebox.showerror("ERRO", "VOCÊ NÃO PREENCHEU TODOS OS CAMPOS!", parent=self.janelap)

        else:
            questoes.append(self.novas)
            messagebox.showinfo("SUCESSO", "QUESTÃO ADICIONADA COM SUCESSO!", parent=self.janelap)
            self.box1.delete(0, END)
            self.box2.delete(0, END)
            self.box3.delete(0, END)
            self.box4.delete(0, END)
            self.box5.delete(0, END)

    def criarQuiz(self):
        self.janelao.destroy()
        q = IniciarJogo(questoes)

    def criarQuiz2(self):
        self.janela1.destroy()
        self.janela2.destroy()
        q = IniciarJogo(questoes)

    def delete(self):
        self.janela1.destroy()
        self.janela2.destroy()
        janela.destroy()

# FUNÇÃO PARA CRIAR O MENU
def criarMenu():
    musicaJogo()
    m = Menu()

criarMenu()

janela.mainloop()