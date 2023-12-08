import pygame
import random

# inicio do jogo
pygame.init()

# Cores
WHITE = (255, 255, 255)

# Configurações da janela
WIDTH, HEIGHT = 800, 600
FPS = 60

# classe contendo as lixeiras
class Lixeira(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, tipo):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.tipo = tipo  

# Classe do Lixo
class Lixo(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, tipo):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        novo_largura = 40
        novo_altura = 40
        self.image = pygame.transform.scale(self.original_image, (novo_largura, novo_altura))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dragging = False
        self.tipo = tipo  #configuração do lixo

    def update(self):
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # da limite horizontal 
            if 0 <= mouse_x <= WIDTH - self.rect.width:
                self.rect.x = mouse_x
            elif mouse_x < 0:
                self.rect.x = 0
            elif mouse_x > WIDTH - self.rect.width:
                self.rect.x = WIDTH - self.rect.width

            # da limites verticais
            if 0 <= mouse_y <= HEIGHT - self.rect.height:
                self.rect.y = mouse_y
            elif mouse_y < 0:
                self.rect.y = 0
            elif mouse_y > HEIGHT - self.rect.height:
                self.rect.y = HEIGHT - self.rect.height

# Função principal
def main():
    global WIDTH, HEIGHT

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Jogo de Lixo")

    clock = pygame.time.Clock()
    running = True

    # sprites dos jogo
    all_sprites = pygame.sprite.Group()
    lixeiras = pygame.sprite.Group()
    lixos = pygame.sprite.Group()

    # codigo para ixibir img fundo
    background = pygame.image.load("/home/felipe/Documentos/jogoII/parqueFase1.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # lixeiras 
    lixeira_paths = ["/home/felipe/Documentos/jogoII/lixeiras/lixeiraMarrom1.png", "/home/felipe/Documentos/jogoII/lixeiras/lixeiraVerde1.png",
                     "/home/felipe/Documentos/jogoII/lixeiras/lixeiraVermelha1.png", "/home/felipe/Documentos/jogoII/lixeiras/lixeiraAzul1.png", 
                     "/home/felipe/Documentos/jogoII/lixeiras/lixeiraAmarela1.png",]
    tipos_lixeira = ["organico", "vidro", "plastico", "papel", "metal"]
    for i, path in enumerate(lixeira_paths):
        lixeira = Lixeira(i * 150 + 350, HEIGHT + 150, path, tipos_lixeira[i])
        lixeiras.add(lixeira)
        all_sprites.add(lixeira)

    # campo com tipos de  lixos
    lixo_paths_papel = ["/home/felipe/Documentos/jogoII/lixos/lixoPapel/caixaleite1.png", "/home/felipe/Documentos/jogoII/lixos/lixoPapel/caixaPapel1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixoPapel/copo1.png", "/home/felipe/Documentos/jogoII/lixos/lixoPapel/embalagem1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixoPapel/folha1.png", "/home/felipe/Documentos/jogoII/lixos/lixoPapel/papelamassado1.png"]
    
    lixo_paths_metal = ["/home/felipe/Documentos/jogoII/lixos/lixometal/lata1.png","/home/felipe/Documentos/jogoII/lixos/lixometal/latinha1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixometal/parafuso1.png","/home/felipe/Documentos/jogoII/lixos/lixometal/pregos1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixometal/sprey1.png"]
    
    lixo_paths_organico = ["/home/felipe/Documentos/jogoII/lixos/lixoOrganico/banana1.png","/home/felipe/Documentos/jogoII/lixos/lixoOrganico/carne1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixoOrganico/maca1.png","/home/felipe/Documentos/jogoII/lixos/lixoOrganico/melancia1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixoOrganico/ovo1.png", "/home/felipe/Documentos/jogoII/lixos/lixoOrganico/peixe1.png"]
    
    lixo_paths_plastico = ["/home/felipe/Documentos/jogoII/lixos/lixoplastico/cabide1.png","/home/felipe/Documentos/jogoII/lixos/lixoplastico/colher1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixoplastico/copo1.png","/home/felipe/Documentos/jogoII/lixos/lixoplastico/escova1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixoplastico/garrafaamassada1.png","/home/felipe/Documentos/jogoII/lixos/lixoplastico/sacola1.png"]
    
    lixo_paths_vidro = ["/home/felipe/Documentos/jogoII/lixos/lixoVidro/espelho1.png","/home/felipe/Documentos/jogoII/lixos/lixoVidro/garrafaV1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixoVidro/jarra1.png","/home/felipe/Documentos/jogoII/lixos/lixoVidro/oculos1.png",
                  "/home/felipe/Documentos/jogoII/lixos/lixoVidro/pote1.png","/home/felipe/Documentos/jogoII/lixos/lixoVidro/xicara1.png"]

    tipos_lixo = ["papel", "metal", "organico", "plastico", "vidro"]
    lixo_paths = [lixo_paths_papel, lixo_paths_metal, lixo_paths_organico, lixo_paths_plastico, lixo_paths_vidro]

    for i in range(25):
        novo_largura = 40
        novo_altura = 40
        x = random.randint(0, WIDTH - novo_largura)
        y = 920
        tipo_lixo = tipos_lixo[i % len(tipos_lixo)]
        lixo = Lixo(x, y, random.choice(lixo_paths[tipos_lixo.index(tipo_lixo)]), tipo_lixo)
        
        lixos.add(lixo)
        all_sprites.add(lixo)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for lixo in lixos:
                    if lixo.rect.collidepoint(event.pos):
                        lixo.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for lixo in lixos:
                    if lixo.dragging:
                        lixo.dragging = False
                        # Verificar se o lixo foi solto em cima de alguma lixeira
                        for lixeira in lixeiras:
                            if lixeira.rect.colliderect(lixo.rect) and lixo.tipo == lixeira.tipo:
                                lixos.remove(lixo)
                                all_sprites.remove(lixo)
            elif event.type == pygame.VIDEORESIZE:
                # Ajustar o tamanho da janela
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                background = pygame.transform.scale(background, (WIDTH, HEIGHT))

        # atualização das  sprites
        all_sprites.update()

        
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)

        # atualização das telas a tela
        pygame.display.flip()

        # quadros por segundo
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
