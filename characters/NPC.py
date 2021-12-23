from characters.Character import Character

class NPC(Character):

    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__(pos_x=pos_x, pos_y=pos_y, picture_path= picture_path)
