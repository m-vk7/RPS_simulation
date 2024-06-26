import pygame
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text = self.font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

class InputField:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text = text
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

class Slider:
    def __init__(self, x, y, length, min_value, max_value, initial_value):
        self.rect = pygame.Rect(x, y, length, 20)
        self.color = GRAY
        self.slider_color = BLACK
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        slider_x = self.rect.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.rect.width
        pygame.draw.circle(screen, self.slider_color, (int(slider_x), self.rect.centery), 10)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                slider_x = event.pos[0] - self.rect.x
                slider_x = max(0, min(slider_x, self.rect.width))
                self.value = self.min_value + (slider_x / self.rect.width) * (self.max_value - self.min_value)

def quit_game():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Main Screen with Buttons, Input Fields, and Sliders")

    # Main screen area
    main_screen_rect = pygame.Rect(0, 0, 600, 500)

    # Buttons
    button1 = Button(650, 100, 100, 50, "Button 1", lambda: print("Button 1 clicked"))
    button2 = Button(650, 200, 100, 50, "Button 2", lambda: print("Button 2 clicked"))
    button3 = Button(650, 300, 100, 50, "Button 3", lambda: print("Button 3 clicked"))
    button_quit = Button(650, 500, 100, 50, "Quit", quit_game)

    # Input fields
    input_field1 = InputField(50, 50, 200, 40)
    input_field2 = InputField(300, 50, 200, 40)

    # Sliders
    slider1 = Slider(50, 150, 200, 0, 100, 50)
    slider2 = Slider(300, 150, 200, 0, 100, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button1.handle_event(event)
            button2.handle_event(event)
            button3.handle_event(event)
            button_quit.handle_event(event)
            input_field1.handle_event(event)
            input_field2.handle_event(event)
            slider1.handle_event(event)
            slider2.handle_event(event)

        # Fill the main screen area with white
        screen.fill(WHITE, main_screen_rect)

        # Draw buttons
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button_quit.draw(screen)

        # Draw input fields
        input_field1.draw(screen)
        input_field2.draw(screen)

        # Draw sliders
        slider1.draw(screen)
        slider2.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
