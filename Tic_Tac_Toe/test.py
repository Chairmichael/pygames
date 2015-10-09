#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
import os
#clears the terminal
def terminal_clear(): os.system('clear')

"""	A class that has methods to display the board, 
	whos turn, and the palyers name and score.
"""
class Display(object):
	#~ def __init__(self): #setup names and pieces from input from the user
		#~ pass
	
	#update the board
	def update(self, board_str, players_str):
		terminal_clear()
		#print player info
		print(players_str)
		#print board
		print('\n' + board_str)
	
	#get input from the user as to where to place a piece
	def get_move(self):
		return [raw_input('col:'), raw_input('row:')]
	

""" A class
"""
class Players(object):
	def __init__(self, roster = { 0: { 'name': 'PLAYER 1', 'score': 0, 'piece': 'O', 'turn': True}, 1: 
									 { 'name': 'PLAYER 2', 'score': 0, 'piece': 'X', 'turn': False} }):
		self.roster = roster
	
	#gets a stat from the roster about a player
	def get_stat(self, player_num, stat_name):
		return self.roster.get(player_num).get(stat_name)
	
	#get a string representation of the roster in a ready-to-print- format
	def get_roster_str(self):
		roster_str = ''
		for stats in self.roster.values():
			roster_str = roster_str + '%s(%s):%s%s\n' % tuple([stats.get('name'), stats.get('piece'), stats.get('score'), stats.get('turn')])
			roster_str = roster_str.replace('True', '  <----').replace('False', '')
		return roster_str
	

""" A class
"""	
class Board(object):
	def __init__(self, board = [ [ ' ', ' ', ' '] , [ ' ', ' ', ' '] , [ ' ', ' ', ' '] ]):
		self.board = board
	
	#return a string resprentation of the board ready to be printed
	def get_board_str(self):
		board_str = ' 1 2 3 \n'
		i = 1
		for column in self.board:
			board_str = board_str + '[' + '-'.join(column) + ']' + str(i) + '\n'
			i = i + 1
		return board_str
	
	#place a piece on the board
	def place(self, piece, col, row):
		if (self.board[col][row] == ' '): 
			self.board[col][row] = piece
	

""" A class
"""	
class Game(object):
	def __init__(self):
		self.board = Board()
		self.players = Players()
		self.display = Display()
	
	#determines if someone has won
	def is_winner(self):
		pass
	
	#contains the loop
	def start(self):
		done = False
		while (not done):
			self.dis_update()
			move = self.get_valid_input()
			
			
			
			done = True
		print('END OF START METHOD')
		
	#essentially a wrapper for Display.get_move()
	def get_valid_input(self):
		#loop until valid input
		move_coords = []
		valid_input = False
		while (not valid_input):
			move_coords = self.display.get_move()
			print(move_coords)
			try: 
				if (int(move_coords[0]) in range(1, 4) and int(move_coords[1]) in range(1, 4)): 
					move_coords[0] = int(move_coords[0])
					move_coords[1] = int(move_coords[1])
					valid_input = True
				else: raise ValueError
			except ValueError: 
				terminal_clear()
				self.dis_update()
				
	#starts a new game and updates the players' scores
	def new_game(self):
		pass
		
	#wrapper
	def dis_update(self):
		self.display.update(self.board.get_board_str(), self.players.get_roster_str())

""" The Main method
"""
def main():
	print("start")
	
	game = Game()
	game.start()
	
	print("quit")
	quit()
	return 0
	

#call the "main" function if running this script
if __name__ == '__main__': main()
