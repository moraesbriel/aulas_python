import random

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive=True
        self.ammo=5
        self.armor=60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)" % self.name

    def fire_at(self, enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

# Criando tanques
tanques = [Tank("Tanque " + str(i+1)) for i in range(5)]

# Simulação
while len(tanques) > 1:
    # Escolhendo o tanque que irá atirar
    tank_index = random.randint(0, len(tanques)-1)
    attacking_tank = tanques[tank_index]

    # Escolhendo o tanque que será atacado
    remaining_tanks = [tank for idx, tank in enumerate(tanques) if idx != tank_index]
    target_index = random.randint(0, len(remaining_tanks)-1)
    target_tank = remaining_tanks[target_index]

    # Realizando o ataque
    attacking_tank.fire_at(target_tank)

    # Removendo tanque se estiver morto
    if not target_tank.alive:
        tanques.remove(target_tank)

print("O tanque vencedor é:", tanques[0])
