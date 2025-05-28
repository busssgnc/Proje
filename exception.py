class IncorrectSpellOrderError(Exception):
    def __init__(self):
        super().__init__("Incorrect spell order! Portal destabilizes, you take damage.")
