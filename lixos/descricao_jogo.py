import pygame
import sys

class DescricaoJogo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.cor_fundo = (255, 255, 255)  # Cor branca
        self.titulo_janela = "Descrição do Jogo"
        self.janela = pygame.display.set_mode((self.largura, self.altura), pygame.RESIZABLE)
        pygame.display.set_caption(self.titulo_janela)
        self.fonte = pygame.font.SysFont(None, 30)

    def exibir_descricao(self):
        descricao = [
            "Bem-vindo ao EcoGame!",
            "Este é um jogo educativo sobre ecologia.",
            "Use as setas para mover e a barra de espaço para pular.",
            "Colete os itens para ganhar pontos e avançar de fase.",
            "Divirta-se jogando e aprendendo sobre sustentabilidade!",
            "",
            "Pressione ESC para voltar ao menu principal."
        ]

        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    rodando = False

            self.janela.fill(self.cor_fundo)

            y_pos = 50
            for linha in descricao:
                texto_renderizado = self.fonte.render(linha, True, (0, 0, 0))
                self.janela.blit(texto_renderizado, (50, y_pos))
                y_pos += 30

            pygame.display.flip()
            pygame.time.Clock().tick(30)

        pygame.quit()
