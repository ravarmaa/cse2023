import pygame
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

pygame.init()
w, h = 1200, 500
screen_size = (w, h)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mass-Spring System Simulation")

# Generated mostly by ChatGPT.
# A lot of hardcoded stuff.

# You can control the mass with KEYs. 
# Use SPACE to stop the mass (buggy atm)
# You can drag the mass around with the MOUSE

# Important parameters should be all here

mass = 1
spring_length = 10
k = 5
b = 0.1
x = 250
y = 250
v_x = 0
v_y = 0
dt = 0.1
t = 0

keyboard_force = 10

dragging = False
running = True

time_data = []
displacement_data_x = []
displacement_data_y = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if math.hypot(mouse_x - x, mouse_y - y) < 10:
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        v_x -= keyboard_force
    if keys[pygame.K_RIGHT]:
        v_x += keyboard_force
    if keys[pygame.K_UP]:
        v_y -= keyboard_force
    if keys[pygame.K_DOWN]:
        v_y += keyboard_force

    if keys[pygame.K_SPACE]:
        x, y = 250, 250
        vx, vy = 0, 0
        spring_force_x, spring_force_y = 0, 0

    if dragging:
        x, y = pygame.mouse.get_pos()
        v_x = 0
        v_y = 0
    else:
        spring_force_x = -k * (x - 250)
        spring_force_y = -k * (y - 250)
        dampening_force_x = -b * v_x
        dampening_force_y = -b * v_y
        acceleration_x = (spring_force_x + dampening_force_x) / mass
        acceleration_y = (spring_force_y + dampening_force_y) / mass
        v_x = v_x + acceleration_x * dt
        v_y = v_y + acceleration_y * dt
        x = x + v_x * dt
        y = y + v_y * dt

    t += dt

    time_data.append(t)
    displacement_data_x.append(x - 250)
    displacement_data_y.append(y - 250)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 10)

    # draw crosshair
    pygame.draw.line(screen, (255, 0, 0), (220, 250), (280, 250), 2)
    pygame.draw.line(screen, (255, 0, 0), (250, 220), (250, 280), 2)


    fig = plt.figure()
    plt.plot(time_data, displacement_data_x, label="X offset")
    plt.plot(time_data, displacement_data_y, label="Y offset")
    plt.legend(loc="upper left")
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    plot_surface = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(plot_surface, (500, 0))
    pygame.display.update()
    plt.close()


pygame.quit()