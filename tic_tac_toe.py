class Game():
    def __init__(self):
        self.player_turn = 'X'
        self.tie = False
        self.winner = None
        self.board = { 
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.scoreboard = {
            'X': 0,
            'O': 0,
        }

    def play_game(self):
        print('It\'s time to duel!')
        while not self.tie and not self.winner:
            self.render()
            self.execute_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        if self.tie or self.winner:
            self.render()
            self.reset_game()

    def render(self):
        # Render Board
        active_board = self.board
        print(f'''
                 A   B   C
            1)   {active_board['a1'] or ' '} | {active_board['b1'] or ' '} | {active_board['c1'] or ' '}
                -----------
            2)   {active_board['a2'] or ' '} | {active_board['b2'] or ' '} | {active_board['c2'] or ' '}
                -----------
            3)   {active_board['a3'] or ' '} | {active_board['b3'] or ' '} | {active_board['c3'] or ' '}
            ''')
        # Render Message
        if self.tie == True:
            print('Tie game! No one wins.')
        elif self.winner:
            print(f'{self.winner} wins the game!')
            print(f"""
                Scoreboard:
                  X  |  O  
                -----------
                  {self.scoreboard.get('X')}  |  {self.scoreboard.get('O')} 
                """)
        else:
            print(f'It\'s {self.player_turn}\'s turn.')

    def switch_turn(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        else:
            self.player_turn = 'X'

    def execute_move(self):
        while True:
            move = input('Input coordinates to move(ie: A1) or type "exit" to exit: ').strip().lower()
            
            if move == 'exit':
                print('See you later!')
                exit()
            elif move not in self.board:
                print('Invalid move. Try again with valid coordinates (ie: A1, C3, etc.)')
            elif self.board[move] != None:
                print('Invalid move. That position is taken. Try again.')
            else:
                self.board[move] = self.player_turn
                return

    def check_for_winner(self):
        win_conditions = (
            ('a1', 'a2', 'a3'),
            ('b1', 'b2', 'b3'),
            ('c1', 'c2', 'c3'),
            ('a1', 'b1', 'c1'),
            ('a2', 'b2', 'c2'),
            ('a3', 'b3', 'c3'),
            ('a1', 'b2', 'c3'),
            ('a3', 'b2', 'c1'),
        )
        
        for condition in win_conditions:
            if self.board[condition[0]] and self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]]:
                self.winner = self.player_turn
                self.scoreboard[self.winner] += 1
                return

    def check_for_tie(self):
        if all(self.board[position] is not None for position in self.board) and not self.winner:
            self.tie = True
            return

    def reset_game(self):
        rematch = input('Rematch? (Y/N): ').strip().lower()
        
        if rematch == 'y':
            self.board = {  
                'a1': None, 'b1': None, 'c1': None,
                'a2': None, 'b2': None, 'c2': None,
                'a3': None, 'b3': None, 'c3': None,
            }
            self.winner = None
            self.tie = False
            self.player_turn = 'X'
            
            self.play_game()
            return
        else:
            print('See you later!')
            return

game_instance=Game()
game_instance.play_game()