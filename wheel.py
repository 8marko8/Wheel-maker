import math
import pygame
import time

pygame.init()
clock = pygame.time.Clock()
radius = 2
def f(x):
    return eval(graph, {"x": x, "math": math})
graph = input("f(x)=")
xStarting = input("starting x: ")
xEnding = input("ending x: ")
axleH = input("constant axle height from x=0: ")
interval = input("Interval in degrees=")
scale = int(input("Enter the scale factor of the drawing (it's too smol): "))
step = (eval(interval)/360) * (eval(xEnding)-eval(xStarting))
screen = pygame.display.set_mode((800, 800))
center = (400, 400)
xF = eval(xStarting)
while True:
    screen.fill((0, 0, 0))
    for angle in range(0, 360, eval(interval)):
        angle = math.radians(angle)
        interval_rad = math.radians(eval(interval))
        angle_next = angle + interval_rad
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        result = f(xF)
        dot_x = 400 + (math.cos(angle)*eval(axleH) - math.cos(angle)*result) * scale
        dot_y = 400 + (math.sin(angle)*eval(axleH) - math.sin(angle)*result) * scale
        dot_x_next = 400 + (math.cos(angle_next)*eval(axleH) - math.cos(angle_next)*(f(xF+step))) * scale
        dot_y_next = 400 + (math.sin(angle_next)*eval(axleH) - math.sin(angle_next)*(f(xF+step))) * scale
        pygame.draw.circle(screen, (255, 255, 255), (400, 400), 5)
        pygame.draw.circle(screen, (255, 0, 255), (dot_x, dot_y), radius)
        pygame.display.flip()
        clock.tick(144)
        time.sleep(0.05)
        xF += step
    time.sleep(0.05)
    continue