import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of button
        self.width, self.height = 72, 48
        self.button_color = (255, 191, 0)
        self.text_color = (249, 246, 238)
        self.font = pygame.font.SysFont("Roboto", 40)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # this button message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into a rendered image and center text on the button"""
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        # self.screen.fill(self.button_color, self.rect)
        pygame.draw.rect(self.screen, self.button_color, self.rect, 3)
        self.screen.blit(self.msg_img, self.msg_img_rect)


