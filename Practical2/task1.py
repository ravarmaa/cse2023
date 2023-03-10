import pygame
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import time

pygame.init()
w, h = 1200, 1000
screen_size = (w, h)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("CSE's Very Sophisticated Partially ChatGPT-Based Simulator")
font = pygame.font.Font(None, 24)

# Define slider properties
slider_pos = (50, 50)
slider2_pos = (50, 100)
slider_length = 400
slider_height = 10
slider_color = (100, 100, 100)
slider_handle_size = (20, 20)
slider_handle_color = (255, 0, 0)

# Define minimum and maximum values for the slider
slider_min = 0.1
slider_max = 20.0
slider2_min = 0.0
slider2_max = 2.0

# Calculate the position of the slider handle based on its value
def handle_pos(value):
    value_range = slider_max - slider_min
    handle_range = slider_length - slider_handle_size[0]
    pos = ((value - slider_min) / value_range) * handle_range
    return pos + slider_pos[0], slider_pos[1] - slider_handle_size[1] / 2

# Calculate the position of the slider handle based on its value
def handle2_pos(value2):
    value2_range = slider2_max - slider2_min
    handle2_range = slider_length - slider_handle_size[0]
    pos = ((value2 - slider2_min) / value2_range) * handle2_range
    return pos + slider2_pos[0], slider2_pos[1] - slider_handle_size[1] / 2

# Define the initial value of the slider handle
slider_value = slider_min
slider2_value = slider2_min
slider_handle_rect = pygame.Rect(*handle_pos(slider_value), *slider_handle_size)
slider2_handle_rect = pygame.Rect(*handle2_pos(slider2_value), *slider_handle_size)

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
slider_dragging = False
slider2_dragging = False
running = True

time_data = []
displacement_datas = []
velocity_datas = []
#displacement_data_y = []

time_passing = False

last_p_time = 0

fig, ax = plt.subplots()
plt.xlim([0,30])
plt.ylim([-50,50])
plt.xlabel('time')
plt.ylabel('angle')

clean_time = np.array([dt*i for i in range(int(30/dt)+1)])
clean_displacement = np.array([np.nan]*(int(30/dt)+1))

latest_line = None

y_max = 50
y_min = -50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if math.hypot(mouse_x - x, mouse_y - y) < 10:
                dragging = True
            elif slider_handle_rect.collidepoint(event.pos):
                slider_dragging = True
            elif slider2_handle_rect.collidepoint(event.pos):
                slider2_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging == True:
                dragging = False
                displacement_datas.append([])
                velocity_datas.append([])
                latest_line = ax.plot(clean_time, clean_displacement)[0]
            elif slider_dragging == True:
                slider_dragging = False
            elif slider2_dragging == True:
                slider2_dragging = False
        elif event.type == pygame.MOUSEMOTION and slider_dragging:
            # Update the value of the slider based on the position of the mouse
            pos = max(slider_pos[0], min(event.pos[0], slider_pos[0] + slider_length - slider_handle_size[0]))
            slider_value = ((pos - slider_pos[0]) / (slider_length - slider_handle_size[0])) * (slider_max - slider_min) + slider_min
            slider_handle_rect.x, slider_handle_rect.y = handle_pos(slider_value)
        elif event.type == pygame.MOUSEMOTION and slider2_dragging:
            # Update the value of the slider based on the position of the mouse
            pos = max(slider2_pos[0], min(event.pos[0], slider2_pos[0] + slider_length - slider_handle_size[0]))
            slider2_value = ((pos - slider2_pos[0]) / (slider_length - slider_handle_size[0])) * (slider2_max - slider2_min) + slider2_min
            slider2_handle_rect.x, slider2_handle_rect.y = handle2_pos(slider2_value)
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        v_x -= keyboard_force
    if keys[pygame.K_RIGHT]:
        v_x += keyboard_force
    #if keys[pygame.K_UP]:
    #    v_y -= keyboard_force
    #if keys[pygame.K_DOWN]:
    #    v_y += keyboard_force

    if keys[pygame.K_SPACE] and time.time()-last_p_time > 0.1:
        time_passing = not time_passing
        last_p_time = time.time()
    if keys[pygame.K_ESCAPE]:
        displacement_datas = []
        velocity_datas = []
        v_x = 0
        v_y = 0
        t = 0

    if time_passing and not dragging:
        if len(displacement_datas) == 0:
            displacement_datas.append([])
            velocity_datas.append([])
            latest_line = ax.plot(clean_time, clean_displacement)[0]
        t += dt
        if t < 30:
            displacement_datas[-1].append(x - 250)
            velocity_datas[-1].append(v_x)
            if x-250 > y_max:
                y_max = x-250
            if x-250 < y_min:
                y_min = x-250
        #displacement_data_y.append(y - 250)

    if dragging:
        x, _ = pygame.mouse.get_pos()
        v_x = 0
        v_y = 0
        t = 0
    elif time_passing and not dragging:
        k = slider_value
        b = 2*k**0.5*slider2_value
        spring_force_x = -k * (x - 250)
        #spring_force_y = -k * (y - 250)
        dampening_force_x = -b * v_x
        #dampening_force_y = -b * v_y
        acceleration_x = (spring_force_x + dampening_force_x) / mass
        #acceleration_y = (spring_force_y + dampening_force_y) / mass
        v_x = v_x + acceleration_x * dt
        #v_y = v_y + acceleration_y * dt
        x = x + v_x * dt
        #y = y + v_y * dt

    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 10)

    # draw crosshair
    pygame.draw.line(screen, (255, 0, 0), (220, 250), (280, 250), 2)
    pygame.draw.line(screen, (255, 0, 0), (250, 220), (250, 280), 2)

    #pygame.draw.line(screen, (0, 255, 0), (int(x), int(y)), (int(x+v_x/5), int(y+v_y/5)), 2)
    #pygame.draw.line(screen, (0, 0, 255), (int(x), int(y)), (int(x+acceleration_x/10), int(y+acceleration_y/10)), 2)
    
    # Draw the slider and handle
    pygame.draw.rect(screen, slider_color, (*slider_pos, slider_length, slider_height))
    pygame.draw.rect(screen, slider_handle_color, slider_handle_rect)
    
    pygame.draw.rect(screen, slider_color, (*slider2_pos, slider_length, slider_height))
    pygame.draw.rect(screen, slider_handle_color, slider2_handle_rect)
    
    # Display the current value of the slider
    value_text = font.render("Spring stiffness: "+str(round(slider_value,2)), True, (0, 0, 0))
    value2_text = font.render("Damping ratio: "+str(round(slider2_value,2)), True, (0, 0, 0))
    screen.blit(value_text, (slider_pos[0], slider_pos[1] - value_text.get_height() - 10))
    screen.blit(value2_text, (slider2_pos[0], slider2_pos[1] - value2_text.get_height() - 10))
    
    # Draw spring
    spring_width = max(int(abs(x - 5)), 0)
    num_segments = 16
    segment_length = spring_width / num_segments
    for i in range(num_segments):
        if i % 2 == 0:
            start = (int(i * segment_length), y - 3)
            end = (int((i + 1) * segment_length), y + 3)
        else:
            start = (int(i * segment_length), y + 3)
            end = (int((i + 1) * segment_length), y - 3)
        pygame.draw.line(screen, (0, 0, 0), start, end, int(max(slider_value,1)))
    
    controls_text = "Controls:\nSpacebar to pause and resume\nESC to clear the plots\nMouse to drag sliders and the mass around"
    # Display control function text
    for i, function_line in enumerate(controls_text.split('\n')):
        function_text_display = font.render(function_line, True, (0, 0, 0))
        screen.blit(function_text_display, (50, 550+i*30))

    if len(displacement_datas) > 0:
        if not latest_line:
            latest_line = ax.plot(clean_time, clean_displacement)[0]
        if latest_line and len(displacement_datas[-1]) > 30/dt:
            latest_line.set_xdata(np.array(displacement_datas[-1][:(int(30/dt)+2)]))
            plt.ylim([y_min, y_max])
        elif latest_line:
            latest_line.set_ydata(np.array(displacement_datas[-1]+[np.nan]*(int(30/dt)+1-len(displacement_datas[-1]))))
            plt.ylim([y_min, y_max])
        # ~ plt.plot(time_data[:len(displacement_datas[-1])], np.array(displacement_datas[-1]), label="X offset")
    #plt.plot(time_data, displacement_data_y, label="Y offset")
    #
    #plt.legend(loc="upper left")
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    plot_surface = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(plot_surface, (500, 0))
    pygame.display.update()
    
    # ~ fig2 = plt.figure()
    # ~ for i, displacement_data_x in enumerate(displacement_datas):
        # ~ plt.plot(displacement_data_x, velocity_datas[i])
    
    # ~ #ax.quiver(X, Y, DX, DY, color='r')
    # ~ plt.xlabel('x')
    # ~ plt.ylabel('ẋ')
    # ~ #plt.xlim([-200, 200])
    # ~ #plt.ylim([-400, 400])
    # ~ plt.grid()
    
    #plt.legend(loc="upper left")
    # ~ canvas2 = FigureCanvasAgg(fig2)
    # ~ canvas2.draw()
    # ~ renderer2 = canvas2.get_renderer()
    # ~ raw_data2 = renderer2.tostring_rgb()
    # ~ size2 = canvas2.get_width_height()
    # ~ plot_surface2 = pygame.image.fromstring(raw_data2, size2, "RGB")
    # ~ screen.blit(plot_surface2, (500, 500))
    # ~ pygame.display.update()
    # ~ plt.close()


pygame.quit()
