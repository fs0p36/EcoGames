import pygame
import sys

class InformacoesJogo:
    def __init__(self, largura_janela, altura_janela):
        self.janela_informacoes = pygame.display.set_mode((largura_janela, altura_janela), pygame.FULLSCREEN)
        self.cor_fundo = (255, 255, 255)  # Cor branca
        pygame.display.set_caption("Informações do Jogo")

    def exibir_informacoes(self):
        informacoes_ativas = True
        while informacoes_ativas:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    informacoes_ativas = False

            # Desenhar as informações
            self.janela_informacoes.fill(self.cor_fundo)
            pygame.display.flip()
