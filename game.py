import curses #cria interface terminal + captura teclas
import random #gera posicao aleatoria comida 

def main(stdsrc):
    #limpa tela
    curses.curs_set(0)  #escode cursos 
    stdsrc.nodelay(1)   #nao bloqueia execucao esperando entrada 
    stdsrc.timeout(100) #milessegundos p/ atualizar pagina

    #dimensoes tela
    altura,largura = stdsrc.getmaxyx()
    janela = curses.newwin(altura,largura,0,0)

    #posicao da cobra 
    cobra = [[4, 10], [4, 9], [4, 8]]

    #direcao inicial 
    direcao = curses.KEY_RIGHT

    def gerar_comida():
        while True:
            comida = [random.randint(1, altura-2), random.randint(1, largura-2)]
            if comida not in cobra:
                return comida
   
   
    #cria comida
    comida = gerar_comida()
    janela.addch (comida [0], comida [1], '*')

    while True:
        #captura tecla 
        nova_direcao = janela.getch()

        #tecla direciona cobrinha
        direcao = direcao if nova_direcao == -1 else nova_direcao

        #calcula movimento 
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
        
        # Se a cobra colidir com ela mesma ou com os limites da tela, o jogo termina
        if (nova_cabeca in cobra or 
            nova_cabeca[0] <= 0 or 
            nova_cabeca[0] >= altura -1 or
            nova_cabeca[1] <= 0 or
            nova_cabeca[1] >= largura -1):
            break 
            


        
        
        # Se a cobra comer a comida, ela cresce
        if nova_cabeca[0] in comida:
            cobra.insert(1,segment)
            # Nova comida
            comida = gerar_comida() 
            janela.addch(comida[0], comida[1], '*')
        else:
            cobra.insert(0, nova_cabeca)
            rabo = cobra.pop()
            janela.addch(rabo[0], rabo[1], ' ')            



        stdsrc.clear()
        
        #desenha a cobra 
        for segment in cobra:
            stdsrc.addstr(segment[0],segment[1] * 2, '0')

        stdsrc.addstr(comida[0], comida[1], '*')
        stdsrc.refresh()


curses.wrapper(main)


        
