import random

class Carta:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo
    
    def __str__(self):
        nombres = ["J", "Q", "K", "A"]
        
        if self.valor <=10:
            return f"{self.valor} de {self.tipo}"
        else:
            return f"{nombres[self.valor-11]} de {self.tipo}"

class Grupo_cartas:
    def __init__(self, cartas=[]):
        self.cartas = cartas
        
    def mostar_carta(self):
        return self.cartas.pop(0)
    
    def verificar_si_hay_cartas(self):
        if len(self.cartas)>0:
            return True
        return False
    
    def verificar_cartas_restantes(self):
        return len(self.cartas)
    
    def barajar(self):
        random.shuffle(self.cartas)
    
    def añadir_carta(self, carta_añadida):
        self.cartas.append(carta_añadida)


class Baraja(Grupo_cartas):
    def __init__(self,cartas=[]):
        super().__init__(cartas)
        
        for tipo in ["Corazones", "Treboles", "Diamantes", "Espadas"]:
            for valor in range(2, 15):
                self.cartas.append(Carta(valor, tipo))


#Creamos nuestra baraja principal, de la cual se repartiran las cartas
baraja_principal=Baraja()

#Barajamos las cartas
baraja_principal.barajar()

#Creamos dos objetos de la clase grupo_cartas que seran las barajas de cada jugador
player1=Grupo_cartas([])
player2=Grupo_cartas([])


#Mostramos las cantidades de cartas iniciales en la baraja y las que poseen los jugadores
print(baraja_principal.verificar_cartas_restantes())
print(player1.verificar_cartas_restantes())
print(player2.verificar_cartas_restantes())
print("-----")

#Repartimos las cartas de la baraja principal


for i in range(52):
    var=baraja_principal.mostar_carta()
    if i%2==1:
        player1.añadir_carta(var)
    else:
        player2.añadir_carta(var)
    

#Mostramos las cantidades de cartas luego de repartir en la baraja y las que poseen los jugadores
print(baraja_principal.verificar_cartas_restantes())
print(player1.verificar_cartas_restantes())
print(player2.verificar_cartas_restantes())



print("El juego ha empezado!!!!")
contador=0
while player1.verificar_si_hay_cartas() and player2.verificar_si_hay_cartas():
    contador+=1
    input("Jugador 1, presione Enter para mostrar su carta")
    #Mostramos la carta del jugador 1
    carta_1=player1.mostar_carta()
    print("La carta del jugador 1 es: ",carta_1)

    input("Jugador 2, presione Enter para mostrar su carta")
    #Mostramos la carta del jugador 2
    carta_2=player2.mostar_carta()
    print("La carta del jugador 2 es: ",carta_2)

    if carta_1.valor>carta_2.valor:
        print("Jugador_1 se lleva las cartas")
        player1.añadir_carta(carta_1)
        player1.añadir_carta(carta_2)
    elif carta_1.valor<carta_2.valor:
        print("Jugador_2 se lleva las cartas")
        player2.añadir_carta(carta_1)
        player2.añadir_carta(carta_2)
    else:
        print("Se eliminan las cartas")

    print("--------")
    print(player1.verificar_cartas_restantes())
    print(player2.verificar_cartas_restantes())
    print("---------")

print("El juego ha finalizado")
print(contador)

