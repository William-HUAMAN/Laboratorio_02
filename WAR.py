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
        
class Baraja(Grupo_cartas):
    def __init__(self,cartas=[]):
        super().__init__(cartas)
        
        for tipo in ["Corazones", "Treboles", "Diamantes", "Espadas"]:
            for valor in range(2, 15):
                self.cartas.append(Carta(valor, tipo))
                