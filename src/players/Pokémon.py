import pygame


# represents the Pokémons in the game
class Pokémon:
    def __init__(self, pos:tuple, value:float, type:int, wasTaken:bool, node:int, dest: int):
        self.pos = pos
        self.value = value
        # type -> going upward or downward
        self.type = type
        # has already been taken
        self.wasTaken = wasTaken
        self.srcnode = node
        self.destnode = dest

    def getpos(self):
        return self.pos

    def __str__(self):
        return self.value
