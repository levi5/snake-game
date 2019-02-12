
# Jogo Snake feito em Python
# Autor: Levi Prudêncio De Araújo Neto

from tkinter import * # Modulo tkinter sendo importado 
import  random        

width_tl  = 500
heigth_tl = 400
Tam = 20


class Snake():
    def __init__(self,x, y, color):
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.vel_x = 0
        self.vel_y = 0
        self.Dimen   = [0,0, 0,Tam, Tam,Tam, Tam,0] #Dimensoes 


    def vel_Snake(self, x, y):
        self.vel_x = x
        self.vel_y = y

    def pos(self):
        return [self.Dimen[0] + self.pos_x,self.Dimen[1] + self.pos_y, self.Dimen[2] + self.pos_x, self.Dimen[3] + self.pos_y, self.Dimen[4] + self.pos_x, self.Dimen[5] + self.pos_y, self.Dimen[6] + self.pos_x, self.Dimen[7] + self.pos_y]
    
    # Método que atualiza a posição do quadrado
    def Atual_pos(self):
        if (self.pos_x > 0 and self.pos_x < width_tl - Tam ):
            self.pos_x += self.vel_x;

        if(self.pos_x == 0 and self.vel_x > 0):
            self.pos_x += self.vel_x 

        if(self.pos_x == width_tl - Tam and self.vel_x < 0):
            self.pos_x += self.vel_x 

        if (self.pos_y > 0 and self.pos_y < heigth_tl - Tam):
            self.pos_y += self.vel_y 

        if(self.pos_y == 0 and self.vel_y > 0):
             self.pos_y += self.vel_y

        if(self.pos_y == heigth_tl - Tam and self.vel_y < 0):
            self.pos_y += self.vel_y 

        

        


class tela():
    # Definição dos parâmetros da função construtora
    def __init__(self):
        #Snake.__init__(self)
        #self.Width      = width
        #self.Heigth     = heigth
        #self.background = color 
        self.window = Tk()  # Atribuindo objeto tipo Tk para atributo da classe
        self.canvas = Canvas(self.window, bg ='black', width = width_tl,  heigh = heigth_tl)
        self.canvas.pack()
        s0 = Snake(20, 20, 'white')
        s1 = Snake(20, 20, 'white')
        s2 = Snake(20, 20, 'white')
        s3 = Snake(20, 20, 'white')

        comd = Snake(random.randint(Tam, (width_tl / Tam)) * Tam - Tam,
                     random.randint(Tam, (heigth_tl / Tam)) * Tam - Tam, 'purple')

        self.snake  = [s0,s1,s2,s3]
        self.comida = [comd]
        self.vel    = [[20,0],[0,0],[0,0],[0,0]]

        self.window.bind("<Up>", self.move_up)
        self.window.bind("<Down>" , self.move_down)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<Left>", self.move_left)
     
    def move_up(self, event):
        if (self.vel[0] != [0,20]):
            self.vel[0] = [0,-20] 

    def move_down(self, event):
        if (self.vel[0] != [0, -20]):
            self.vel[0] = [0, 20]

    def move_right(self, event):
        if (self.vel[0] != [-20, 0]):
            self.vel[0] = [20, 0]

    def move_left(self, event):
        if (self.vel[0] != [20, 0]):
            self.vel[0] = [-20, 0]


    def criar_tela(self):
        cont = 0
        while True:
            self.canvas.delete('all')

            for l in range(len(self.vel)-1,0,-1):
                self.vel[l] = self.vel[l-1]

            for l in range(len(self.vel)):
                self.snake[l].vel_x = self.vel[l][0]
                self.snake[l].vel_y = self.vel[l][1]

            if (self.snake[0].pos() == self.comida[0].pos()):
                self.comida[0].pos_x = random.randint(0, (width_tl / Tam)) * Tam - Tam
                self.comida[0].pos_y = random.randint(0, (heigth_tl / Tam)) * Tam - Tam
                print("{} {} ".format(self.comida[0].pos_x, self.comida[0].pos_y))
                x = 0
                while x == 0:
                    if self.comida[0].pos_x < 20 or self.comida[0].pos_y < 20:
                        self.comida[0].pos_x = random.randint(0, width_tl / Tam - 1) * Tam - Tam
                        self.comida[0].pos_y = random.randint(0, heigth_tl / Tam) * Tam - Tam
                    else:
                        x = 1
                self.vel.append([0, 0])
                self.snake.append(Snake(self.snake[-1].pos_x, self.snake[-1].pos_y, self.snake[0].color))


            
            for s in self.snake:
                s.Atual_pos()
                self.canvas.create_polygon(s.pos(), fill = s.color)
            
            for comd in self.comida:
                comd.Atual_pos()
                self.canvas.create_polygon(comd.pos(), fill=comd.color)

            for i in range(2, len(self.snake)):
                if cont < 1:
                    cont += 1
                elif self.snake[0].pos() == self.snake[i].pos():
                    print("Game Over!!")
                    exit()
            

            self.canvas.after(180)
            self.window.update_idletasks()
            self.window.update()
    
       
game = tela()
game.criar_tela()
  
