import os 
import sys

import pygame 
from consts import WIDTH, HEIGHT, N_ROWS, N_COLS, BLOCK_SIZE
from consts import WHITE ,BLACK ,BLUE ,GREEN, RED
import heapq

pygame.init()

from enum import Enum

class Role:
    UNUSED = WHITE
    START = BLUE
    END = GREEN
    BLOCK = BLACK
    SERCHED = (247, 246, 242)
    PATH = RED

class Block:
    def __init__(self, row, col):
        self.x = col * BLOCK_SIZE  
        self.y = row * BLOCK_SIZE  
        self.row = row 
        self.col = col

        self.role = Role.UNUSED
        self.neighbors = []

    def set_role(self, role):
        self.role = role

    def get_position(self):
        return (self.x, self.y)

    def get_unused_neighbors(self, box_list):
        if not bool(self.neighbors):
            if 0 < self.row and self.row < N_ROWS:
                if (box_list[self.row - 1][self.col].role != Role.BLOCK):
                    self.neighbors.append(box_list[self.row - 1][self.col])

                if (box_list[self.row + 1][self.col].role != Role.BLOCK):
                    self.neighbors.append(box_list[self.row + 1][self.col])

            if 0 < self.col and self.row < N_COLS:
                if (box_list[self.row][self.col + 1].role != Role.BLOCK):
                    self.neighbors.append(box_list[self.row][self.col + 1])

                if (box_list[self.row][self.col - 1].role != Role.BLOCK):
                    self.neighbors.append(box_list[self.row][self.col - 1])

        return self.neighbors

    def __lt__(self, other):
        return True

    def is_closed(self, box_list):
        if (box_list[self.row - 1][self.col].role == Role.BLOCK) and (box_list[self.row][self.col + 1].role == Role.BLOCK) \
            and (box_list[self.row + 1][self.col].role == Role.BLOCK) and (box_list[self.row][self.col - 1].role == Role.BLOCK):
            return True

    def draw(self, window):
        pygame.draw.rect(window, self.role, (self.x + 2, self.y + 2, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, data): #priority, location
        heapq.heappush(self.elements, (data[0], data[1]))
        
    def get(self):
        return heapq.heappop(self.elements)

class Screen:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("Path finder")
        self.box_list = []
        self.path = {"START": None, "END": None}

        for row in range(N_ROWS):
            self.box_list.append([])
            for col in range(N_COLS):
                self.box_list[row].append(Block(row, col))

        self.done = False

    def reset(self):
        self.done = False 
        for row in range(N_ROWS):
            self.box_list.append([])
            for col in range(N_COLS):
                self.box_list[row][col].set_role(Role.UNUSED)
        self.path = {"START": None, "END": None}
        return self.done 

    def draw(self):
        self.window.fill(WHITE)

    def update(self):
        self.draw()
        for row in range(N_ROWS):
            pygame.draw.line(self.window, BLACK, (0, row * BLOCK_SIZE), (WIDTH, row * BLOCK_SIZE))
            for col in range(N_COLS):
                pygame.draw.line(self.window, BLACK, (col * BLOCK_SIZE, 0), (col * BLOCK_SIZE, WIDTH))
                self.box_list[row][col].draw(self.window)
        pygame.display.flip()

    def clicked_position(self, pos):
        x, y = pos 
        col = x//BLOCK_SIZE
        row = y // BLOCK_SIZE
        return (row, col)

    def create_path(self, came_from, current_block):
        while current_block in came_from:
            current_block = came_from[current_block]
            if self.path["START"] != current_block and self.path["END"] != current_block:
                current_block.set_role(Role.PATH)
            self.update()

    def run(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    break

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = self.clicked_position(pos)

                    if self.path["START"] is None:
                        if self.box_list[row][col].role != Role.END:
                            self.box_list[row][col].set_role(Role.START)
                            self.path["START"] = self.box_list[row][col]
                        
                    elif self.path["END"] is None:
                        if (self.box_list[row][col].role != Role.START):
                            self.box_list[row][col].set_role(Role.END)
                            self.path["END"] = self.box_list[row][col]

                    else:
                        if (self.box_list[row][col].role != Role.START) and (self.box_list[row][col].role != Role.END):
                            if not self.path["START"].is_closed(self.box_list) and not self.path["END"].is_closed(self.box_list):
                                self.box_list[row][col].set_role(Role.BLOCK)

                if pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    row, col = self.clicked_position(pos)
                    if self.box_list[row][col].role == Role.START:
                        self.path["START"] = None

                    if self.box_list[row][col].role == Role.END:
                        self.path["END"] = None

                    self.box_list[row][col].set_role(Role.UNUSED)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        path = self.dijkstras_search(self.box_list, self.path["START"], self.path["END"])
                        self.done = True
                        break
                        
                    if event.key == pygame.K_ESCAPE:
                        self.reset()
            self.update()

        pygame.quit()
        sys.exit(0)

    def dijkstras_search(self, blocks, start, goal):
        frontier = PriorityQueue()
        came_from = {}
        cost_so_far = {block: float("inf") for row in blocks for block in row}
        came_from[start] = None 
        cost_so_far[start] = 0 
        frontier.put((cost_so_far[start], start))
        
        while not frontier.empty(): 
            
            cost, current_block = frontier.get() 
            
            if current_block == goal:
                self.create_path(came_from, current_block)
                break

            for next in current_block.get_unused_neighbors(blocks):
                if next.role != Role.SERCHED:
                    new_cost = cost_so_far[current_block] + 1
                    if new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        frontier.put((new_cost, next))
                        came_from[next] = current_block
                        if self.path["START"] != current_block and self.path["END"] != current_block:
                            current_block.set_role(Role.SERCHED)

                next.draw(self.window)
                pygame.display.flip()

        return came_from





    
 