class Card:
    def __init__(self, info):
        self.name = info["name"]
        self.attack = info["attack"]
        self.actions = info["actions"]
        self.draw = info["draw"]
        self.heal = info["heal"]
        self.shield = info["shield"]
        self.image = info["image"]

    # just for condsole output
    def __repr__(self):
        return f"{self.name} atk: {self.attack} act: {self.actions} draw: {self.draw} shield: {self.shield} heal: {self.heal}"
