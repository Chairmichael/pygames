#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
import pygame as py

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
		return [raw_input('row:'), raw_input('col:')]
	

""" A class
"""
class Players(object):
	def __init__(self, roster = { 0: { 'name': 'PLAYER 1', 'score': 0, 'piece': 'O', 'turn': True}, 
								  1: { 'name': 'PLAYER 2', 'score': 0, 'piece': 'X', 'turn': False} }):
		self.roster = roster
	
	#gets a stat from the roster about a player
	def get_stat(self, player_num, stat_name):
		return self.roster.get(player_num).get(stat_name)
		
	#increases a player's score my one
	def increment_score(self, player_num):
		self.roster[player_num]['score'] = self.roster[player_num]['score'] + 1
		
	#gets the amount of players
	def num_of_players(self):
		return len(self.roster)
		
	#gives the turn to the next player
	def change_turn(self):
		for i in self.roster.keys():
			if (self.roster[i]['turn']):
				self.roster[i]['turn'] = False
				if(i == len(self.roster) - 1):
					self.roster[0]['turn'] = True
				else:
					self.roster[i + 1]['turn'] = True
				return
	
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
		
	#False if no winner, player's num if winner
	def is_winner(self):
		''' Better way:
				Collect pieces and put in dictionary with coords
				Sort with the x coord then look for 3 in a row
				Sort with the y coord then look for 3 in a row
		'''
		for i in range(3):
			r = self.board[i]
			if (r[0] != ' ' and r[0] == r[1] and r[1] == r[2]): return True
			
			c = []
			for j in range(3): c.append(self.board[j][i])
			print('--  c:%s' % c)
			if (c[0] != ' ' and c[0] == c[1] and c[1] == c[2]): return True #String index out of range!
		
		diag1 = []
		diag2 = []
		for i in range(3):
			diag1.append(self.board[i][i])
			diag2.append(self.board[i][abs(i-2)])
		if (diag2[0] != ' ' and diag1[0] == diag1[1] and diag1[1] == diag1[2]): return True
		if (diag2[0] != ' ' and diag2[0] == diag2[1] and diag2[1] == diag2[2]): return True
		
		#return false if nothing found
		return False
		
	
	#return a string resprentation of the board ready to be printed
	def get_board_str(self):
		board_str = ' 1 2 3 \n'
		i = 1
		for column in self.board:
			board_str += '[%s-%s-%s]%s\n' % tuple(column + [i])
			i += 1
		return board_str
		
	#true if the place is empty, otherwise false
	def place_empty(self, place):
		return self.board[place[0]][place[1]] == ' '
		
	#place a piece on the board
	def place(self, piece, place):
		if (self.board[place[0]][place[1]] == ' '): 
			self.board[place[0]][place[1]] = piece
	

""" A class
"""	
class Game(object):
	def __init__(self):
		self.board = Board()
		self.players = Players()
		self.display = Display()
	
	#contains the loop
	def start(self):
		done = False
		total_turns = 0
		self.dis_update()
		while (not done):
			move_place = self.get_valid_input()
			turn = self.get_turn()
			
			self.board.place(self.players.get_stat(turn, 'piece'), move_place)
			total_turns += 1
			self.players.change_turn()
			
			if (total_turns > 4):
				print('Total turns:%s' % total_turns)
				if (self.board.is_winner()):
					done = True
					print('Winner')
			if (total_turns >= 9):
				done = True
				print('No winner')
			self.dis_update()
		print('END OF START METHOD')
		
	#essentially a wrapper for Display.get_move() and subtracts 1
	def get_valid_input(self):
		#loop until valid input
		move_coords = []
		valid_input = False
		while (not valid_input):
			move_coords = self.display.get_move()
			try: 
				if (int(move_coords[0]) in range(1, 4) and int(move_coords[1]) in range(1, 4)): 
					move_coords[0] = int(move_coords[0]) - 1
					move_coords[1] = int(move_coords[1]) - 1
					if (self.board.place_empty(move_coords)):
						valid_input = True
					else: raise ValueError
				else: raise ValueError
			except ValueError: 
				terminal_clear()
				self.dis_update()
		return move_coords
				
	#finds whos turn it is, sort of a wrapper
	def get_turn(self):
		for i in range(self.players.num_of_players()):
			if (self.players.get_stat(i, 'turn')): return i
				
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
