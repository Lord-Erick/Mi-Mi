import tkinter as tk
from PIL import Image, ImageTk
import random
import math

class Roleta:
    def __init__(self, root):
        self.root = root
        self.root.title("Roleta com Fotos")
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()
        self.angle = 0
        self.colors = ["red", "green", "blue", "yellow", "purple", "cyan"]
        
        # Carregar imagens
        self.imagens = []
        self.nomes_imagens = []  # Armazena os nomes das imagens
        for i in range(1, 7):
            try:
                caminho = f"/storage/emulated/0/meu_modulo/imagens/f{i}.jpg"
                print(f"Carregando imagem: {caminho}")
                img = Image.open(caminho)
                img = img.resize((80, 80), Image.ANTIALIAS)
                self.imagens.append(ImageTk.PhotoImage(img))
                self.nomes_imagens.append(f"f{i}.jpg") 
                print(f"Imagem f{i}.jpg carregada com sucesso!")
            except Exception as e:
                print(f"Erro ao carregar imagem f{i}.jpg: {e}")
                # Adiciona uma imagem padrão em caso de erro
                img = Image.new("RGB", (80, 80), color="gray")
                self.imagens.append(ImageTk.PhotoImage(img))
                self.nomes_imagens.append(f"f{i}.jpg")
        
        self.draw_roleta()
        self.button = tk.Button(root, text="Girar Roleta", command=self.iniciar_animacao)
        self.button.pack()

    def draw_roleta(self):
        self.canvas.delete("all")
        for i in range(6):
            start_angle = i * 60
            end_angle = (i + 1) * 60
            self.canvas.create_arc(50, 50, 450, 450, start=start_angle, extent=60, fill=self.colors[i], outline="black")
            text_angle = math.radians(start_angle + 30)
            x = 250 + 150 * math.cos(text_angle)
            y = 250 - 150 * math.sin(text_angle)
            self.canvas.create_image(x, y, image=self.imagens[i])
        
        #seta#
        self.canvas.create_polygon(250, 20, 240, 50, 260, 50, fill="black")

     #funcao girar#
    def iniciar_animacao(self):
        self.target_angle = self.angle + random.randint(360, 3600) 
        self.animar_roleta()

    def animar_roleta(self):
        if self.angle < self.target_angle:
            self.angle += 20
            self.canvas.delete("all")
            for i in range(6):
                start_angle = i * 60 + self.angle
                end_angle = (i + 1) * 60 + self.angle
                self.canvas.create_arc(50, 50, 450, 450, start=start_angle % 360, extent=60, fill=self.colors[i], outline="black")
                text_angle = math.radians(start_angle + 30)
                x = 250 + 150 * math.cos(text_angle)
                y = 250 - 150 * math.sin(text_angle)
                self.canvas.create_image(x, y, image=self.imagens[i])
           
            
            self.root.after(30, self.animar_roleta) 
        else:
            self.mostrar_imagem_sorteada()

    def mostrar_imagem_sorteada(self):
        # Calcular o índice da imagem sorteada
        angulo_final = self.angle % 360
        indice_sorteado = int(angulo_final // 60)  # Cada segmento tem 60 graus
        if indice_sorteado >= len(self.nomes_imagens):
            indice_sorteado = 0  # Caso o ângulo seja exatamente 360
        
        # Exibir o nome da imagem sorteada no console
        imagem_sorteada = self.nomes_imagens[indice_sorteado]
        print(f"Imagem sorteada: {imagem_sorteada}")
        
        # Exibir o nome da imagem na interface (opcional)
        self.canvas.create_text(250, 400, text=f"Imagem sorteada: {imagem_sorteada}", font=("Arial", 16), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    roleta = Roleta(root)
    root.mainloop()