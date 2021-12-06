"""
https://adventofcode.com/2021/day/6
"""
from itertools import repeat
from PIL import Image, ImageFilter,ImageChops,ImageDraw,ImageEnhance
import pygame
from random import random,randint

BLACK = (0,0,0)
GREEN = (0,255,0)

def load_data(filename: str) -> tuple:
    " Load fish data "
    items = [int(x) for x in open(filename, "r").read().split(',')]
    return items

def generate_dots_image(image, births, col):
    " Generate an image with given amount of random green dots"

    width, height = image.size
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), fill=BLACK)
    
    for n in range(births):
        x,y = randint(0,width),randint(0,height)
        draw.line([(x,y),(x,y-1)], fill=col)

    return image

def pilImageToSurface(pilImage):
    " Convert image from PIL image to Pygame Surface type "
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

def pygame_test():

    finished = False
    items  = load_data("input.txt")  
    days = 256
    day = 0
    births = []
    births = list(repeat(0, days+9))
    max_val = 1000
    black_image = Image.new('RGB', (max_val, max_val), BLACK)
    dots_image = Image.new('RGB', (max_val, max_val), BLACK)

    pygame.init()
    gameDisplay = pygame.display.set_mode((max_val,max_val))
    pygame.display.set_caption('AOC')
    clock = pygame.time.Clock()

    for item in items: 
        births[item] += 1

    fish = len(items)

    base_image = Image.new('RGB', (max_val, max_val), BLACK)

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        fish += births[day]
        births[day+9] += births[day] # set new fish to be born
        births[day+7] += births[day] # set today's parents to respawn again


        # shift existing canvas down 5px and black top 5px (as image tiles when offset)
        base_image_shifted = ImageChops.offset(base_image,0,5)
        base_image_shifted.paste(BLACK, (0, 0, max_val, 5))

        # darken existing image
        base_image = ImageChops.blend(black_image, base_image, 0.1)

        # add on shifted existing image onto darkened version
        base_image = ImageChops.add(base_image, base_image_shifted)

        # generate today's births as green dots
        dots_image = generate_dots_image(dots_image, births[day], GREEN)

        # add today's dots on
        base_image = ImageChops.add(base_image, dots_image)

        # add a two-level blur on top annd give it a bit of a random flicker
        blurred2 = base_image.filter(ImageFilter.GaussianBlur(20+randint(-2,2)))
        blurred1 = base_image.filter(ImageFilter.GaussianBlur(5))
        f_image = ImageChops.add(ImageChops.add(base_image,blurred1,0.5+random()*0.1),blurred2,0.6+random()*0.05)

        # push image to pygramee window
        img = pilImageToSurface(f_image)
        gameDisplay.blit(img, (0,0))
        pygame.display.update()

        # save image to disk
        pygame.image.save(gameDisplay,f"/Users/tombox/images/display{day:04}.png")

        print(day)
        clock.tick(60)    
        day+=1

        if day >= days:
            finished = True


pygame_test()