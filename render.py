import pygame
import requests
import time
import math

SERVER_URL = "http://127.0.0.1:5000/lidar-result"

WIDTH = 1280
HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True
maxVal = 5
minVal = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # draw grid lines
    pygame.draw.line(screen, "white", (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 1)
    pygame.draw.line(screen, "white", (0, HEIGHT / 2), (WIDTH, HEIGHT / 2), 1)

    try:
        response = requests.get(SERVER_URL, timeout=2)
        if response.status_code == 200:
            data = response.json()
            print("data recieved")
            for point in data['points']:
                if point['c'] >= 20:
                    coordinate = ((WIDTH/2) + (((math.cos(point['a']) * point['d']) - minVal) / (maxVal - minVal)),
                                  (HEIGHT/2) + (((math.sin(point['a']) * point['d']) - minVal) / (maxVal - minVal)))
                    pygame.draw.circle(screen, "red", coordinate, radius=3)

    except Exception as e:
        print(f"Waiting for response...{e}")

    pygame.display.flip()

    clock.tick(60)
    time.sleep(2)

'''
while True:
    try:
        response = requests.get(SERVER_URL, timeout=2)
        if response.status_code == 200:
            data = response.json()
            print("data recieved")
            print(data)
    except Exception as e:
        print(f"Waiting for response...{e}")

    # updates every 2 seconds 
    time.sleep(2)
'''