import pygame
import sys
from descricao_jogo import DescricaoJogo
from informacoes_jogo import InformacoesJogo

# Inicialização do Pygame
pygame.init()

# Obtendo as dimensões da tela
largura_janela = pygame.display.Info().current_w
altura_janela = pygame.display.Info().current_h

cor_fundo = (255, 255, 255)  # Cor branca
titulo_janela = "Menu Pygame"

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20  # Espaço entre os botões

# Calcula as posições verticais dos botões para que fiquem centralizados
button_y_start = (altura_janela - (3 * BUTTON_HEIGHT + 2 * BUTTON_MARGIN)) // 2

BUTTON_START = pygame.Rect((largura_janela - BUTTON_WIDTH) // 2, button_y_start, BUTTON_WIDTH, BUTTON_HEIGHT)
BUTTON_DESCRIPTION = pygame.Rect((largura_janela - BUTTON_WIDTH) // 2, button_y_start + BUTTON_HEIGHT + BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)
BUTTON_INFO = pygame.Rect((largura_janela - BUTTON_WIDTH) // 2, button_y_start + 2 * (BUTTON_HEIGHT + BUTTON_MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT)

# Inicializando a janela em modo tela cheia
janela = pygame.display.set_mode((largura_janela, altura_janela), pygame.FULLSCREEN)
pygame.display.set_caption(titulo_janela)

# Carregando a imagem de fundo
imagem_fundo = pygame.image.load("/home/felipe/Documentos/jogoII/fundo2.jpg")  # Substitua pelo caminho real
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_janela, altura_janela))

# Carregando a música de fundo
pygame.mixer.music.load("/home/felipe/Documentos/jogoII/Caketown1.mp3")  # Substitua pelo caminho real
pygame.mixer.music.play(-1)  # -1 para reprodução contínua

# Cores dos botões
COR_PADRAO = (255, 0, 0)  # Vermelho
COR_DESTAQUE = (0, 255, 0)  # Verde quando o mouse está sobre o botão

# Função para exibir texto na tela
def exibir_texto(texto, tamanho, cor, posicao):
    fonte = pygame.font.SysFont(None, tamanho)
    texto_renderizado = fonte.render(texto, True, cor)
    janela.blit(texto_renderizado, posicao)

# Função para verificar se o mouse está sobre um botão
def mouse_sobre_botao(mouse_x, mouse_y, botao):
    return botao.collidepoint(mouse_x, mouse_y)

# Função para centralizar os botões na tela
def centralizar_botoes():
    # Calcula as posições verticais dos botões para que fiquem centralizados
    button_y_start = (altura_janela - (3 * BUTTON_HEIGHT + 2 * BUTTON_MARGIN)) // 2

    BUTTON_START.x = (largura_janela - BUTTON_WIDTH) // 2
    BUTTON_START.y = button_y_start

    BUTTON_DESCRIPTION.x = (largura_janela - BUTTON_WIDTH) // 2
    BUTTON_DESCRIPTION.y = button_y_start + BUTTON_HEIGHT + BUTTON_MARGIN

    BUTTON_INFO.x = (largura_janela - BUTTON_WIDTH) // 2
    BUTTON_INFO.y = button_y_start + 2 * (BUTTON_HEIGHT + BUTTON_MARGIN)

# Função para exibir a janela de jogos
def exibir_jogos():
    # Inicialização do Pygame
    pygame.init()

    # Obtendo as dimensões da tela
    largura_janela_jogos = pygame.display.Info().current_w
    altura_janela_jogos = pygame.display.Info().current_h

    cor_fundo_jogos = (255, 255, 255)  # Cor branca
    titulo_janela_jogos = "Jogos Pygame"

    # Inicializando a janela de jogos
    janela_jogos = pygame.display.set_mode((largura_janela_jogos, altura_janela_jogos), pygame.FULLSCREEN)
    pygame.display.set_caption(titulo_janela_jogos)

    # Carregando a imagem de fundo
    #imagem_fundo_jogos = pygame.image.load("/home/felipe/Documentos/jogoII/fundo2.jpg")  # Substitua pelo caminho real
    #imagem_fundo_jogos = pygame.transform.scale(imagem_fundo_jogos, (largura_janela_jogos, altura_janela_jogos))

    # Função para exibir texto na tela de jogos
    def exibir_texto_jogos(texto, tamanho, cor, posicao):
        fonte = pygame.font.SysFont(None, tamanho)
        texto_renderizado = fonte.render(texto, True, cor)
        janela_jogos.blit(texto_renderizado, posicao)

    # Loop principal da janela de jogos
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()

            # Verifica se a tecla ESC foi pressionada para sair do modo tela cheia
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
                pygame.quit()
                sys.exit()

            # Verifica se a janela foi redimensionada
            elif evento.type == pygame.VIDEORESIZE:
                largura_janela_jogos = evento.w
                altura_janela_jogos = evento.h
                janela_jogos = pygame.display.set_mode((largura_janela_jogos, altura_janela_jogos), pygame.RESIZABLE)

        # Desenhar a imagem de fundo
        #janela_jogos.blit(imagem_fundo_jogos, (0, 0))

        # Exibir texto centralizado
        exibir_texto_jogos("Lixeiras", 30, (0, 0, 0), ((largura_janela_jogos - 150) // 2, altura_janela_jogos // 3))
        exibir_texto_jogos("Jogo da Memória", 30, (0, 0, 0), ((largura_janela_jogos - 250) // 2, altura_janela_jogos // 2))
        exibir_texto_jogos("Perguntas e Respostas", 30, (0, 0, 0), ((largura_janela_jogos - 350) // 2, 2 * altura_janela_jogos // 3))

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de atualização da tela
        pygame.time.Clock().tick(30)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Verifica se um dos botões foi clicado
            if mouse_sobre_botao(mouse_x, mouse_y, BUTTON_START):
                # Chama a função para exibir os jogos
                exibir_jogos()
            elif mouse_sobre_botao(mouse_x, mouse_y, BUTTON_DESCRIPTION):
                # Chama a janela de descrição
                descricao = DescricaoJogo(largura_janela, altura_janela)
                descricao.exibir_descricao()
            elif mouse_sobre_botao(mouse_x, mouse_y, BUTTON_INFO):
                # Chama a janela de informações
                informacoes = InformacoesJogo(largura_janela, altura_janela)
                informacoes.exibir_informacoes()

        # Verifica se a tecla ESC foi pressionada para sair do modo tela cheia
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # Verifica se a janela foi redimensionada
        elif evento.type == pygame.VIDEORESIZE:
            largura_janela = evento.w
            altura_janela = evento.h
            janela = pygame.display.set_mode((largura_janela, altura_janela), pygame.RESIZABLE)
            centralizar_botoes()  # Recentraliza os botões após a redimensionamento

    # Desenhar a imagem de fundo
    janela.blit(imagem_fundo, (0, 0))

    # Desenhar os botões
    for botao in [BUTTON_START, BUTTON_DESCRIPTION, BUTTON_INFO]:
        cor_botao = COR_DESTAQUE if mouse_sobre_botao(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], botao) else COR_PADRAO
        pygame.draw.rect(janela, cor_botao, botao)

    # Exibir texto nos botões
    exibir_texto("Start", 20, (0, 0, 0), (BUTTON_START.x + 20, BUTTON_START.y + 15))
    exibir_texto("Descrição", 20, (0, 0, 0), (BUTTON_DESCRIPTION.x + 10, BUTTON_DESCRIPTION.y + 15))
    exibir_texto("Informações", 20, (0, 0, 0), (BUTTON_INFO.x + 5, BUTTON_INFO.y + 15))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização da tela
    pygame.time.Clock().tick(30)
