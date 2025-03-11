import curses
import random

def main(stdsrc):

    # Função para exibir a tela de Game Over
    def game_over():
        stdsrc.clear()
        # Centraliza a mensagem "GAME OVER"
        stdsrc.addstr(altura // 2, largura // 2 - 5, "GAME OVER")
        # Opções de jogar novamente ou sair
        stdsrc.addstr(altura // 2 + 2, largura // 2 - 10, "1. Jogar Novamente")
        stdsrc.addstr(altura // 2 + 3, largura // 2 - 10, "2. Sair")
        #stdsrc.refresh()

        # Aguarda a escolha do jogador
        while True:
            escolha = stdsrc.getch()
            if escolha == ord('1'):
                curses.wrapper(main)
                
            elif escolha == ord('2'):
                break
                

    # Limpa a tela e configurações iniciais
    curses.curs_set(0)
    stdsrc.nodelay(1)
    stdsrc.timeout(100)

    # Dimensões da tela
    altura, largura = stdsrc.getmaxyx()
    janela = curses.newwin(altura, largura, 0, 0)

    # Posição inicial da cobra
    cobra = [[4, 10], [4, 9], [4, 8]]

    # Direção inicial
    direcao = curses.KEY_RIGHT

    # Função para gerar comida em posição aleatória
    def gerar_comida():
        while True:
            comida = [random.randint(1, altura - 2), random.randint(1, largura - 2)]
            if comida not in cobra:
                return comida
       
    # Cria a primeira comida
    comida = gerar_comida()
    janela.addch(comida[0], comida[1], '*')

    # Inicializa o score
    score = 0

    while True:
        # Captura a tecla pressionada
        nova_direcao = janela.getch()

        # Atualiza a direção da cobra
        direcao = direcao if nova_direcao == -1 else nova_direcao

        # Calcula o movimento da cobra
        if direcao == ord('d'):
            nova_cabeca = [cobra[0][0], cobra[0][1] + 1]
        elif direcao == ord('a'):
            nova_cabeca = [cobra[0][0], cobra[0][1] - 1]
        elif direcao == ord('w'):
            nova_cabeca = [cobra[0][0] - 1, cobra[0][1]]
        elif direcao == ord('s'):
            nova_cabeca = [cobra[0][0] + 1, cobra[0][1]]
        else:
            continue

        # Verifica colisão com as bordas ou com o próprio corpo
        if (nova_cabeca in cobra or 
            nova_cabeca[0] <= 0 or
            nova_cabeca[0] >= altura - 1 or
            nova_cabeca[1] <= 0 or
            nova_cabeca[1] >= largura - 1):
            game_over()
        


        # Verifica se a cobra comeu a comida
        if nova_cabeca[0] in comida:
            cobra.insert(1, segment)
            comida = gerar_comida()
            janela.addch(comida[0], comida[1], '*')
            score += 1  # Incrementa o score
        else:
            cobra.insert(0, nova_cabeca)
            rabo = cobra.pop()
            janela.addch(rabo[0], rabo[1], ' ')

        # Limpa a tela e desenha a cobra e a comida
        stdsrc.clear()
        for segment in cobra:
            stdsrc.addstr(segment[0], segment[1] * 2, '0')
        stdsrc.addstr(comida[0], comida[1], '*')

        # Exibe o score no canto superior direito
        stdsrc.addstr(1, largura - 10, f"Score: {score}")
        stdsrc.refresh()

curses.wrapper(main)