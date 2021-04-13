class Card:
    def __init__(self, name, attack=0, actions=0, draw=0, heal=0):
        self.name = name
        self.attack = attack
        self.actions = actions
        self.draw = draw
        self.heal = heal

    # just for condsole output
    def __repr__(self):
        return f"{self.name} atk: {self.attack} act: {self.actions} draw: {self.draw}"
        