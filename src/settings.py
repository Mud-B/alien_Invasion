class Settings:
    """ store <<Alien Invasion>> settings """

    def __init__(self):
        """ initial game settings """
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship setting
        self.ship_speed = 0.5

        #Bullet setting
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
