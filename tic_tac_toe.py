class Game():
    def __init__(self, winner=None, player_turn='X', tie=False, 
                board={
                    'a1': None, 'b1': None, 'c1': None,
                    'a2': None, 'b2': None, 'c2': None,
                    'a3': None, 'b3': None, 'c3': None,
                }):
        self.player_turn = player_turn
        self.tie = tie
        self.winner = winner
        self.board = board

    def render(self):
        active_board = self.board
        print(f'''
                A   B   C
            1)  {active_board['a1'] or ' '} | {active_board['b1'] or ' '} | {active_board['c1'] or ' '}
                ----------
            2)  {active_board['a2'] or ' '} | {active_board['b2'] or ' '} | {active_board['c2'] or ' '}
                ----------
            3)  {active_board['a3'] or ' '} | {active_board['b3'] or ' '} | {active_board['c3'] or ' '}
            ''')

        if self.tie == True:
            print('Tie game! Play again?')
        elif self.winner:
            print(f'{self.winner} wins the game! Play again?')
        else:
            print(f'It\'s player {self.player_turn}\'s turn.')

    def play_game(self):
        print('It\'s time to duel!')
        self.render()
        self.execute_move()
        self.switch_turn()

    def switch_turn(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        else:
            self.player_turn = 'X'

    def execute_move(self):
        while True:
            move = input('Input coordinates to move(ie: A1) or type "exit" to quit:').strip().lower()
            
            if move == 'exit':
                print('See you later!')
                exit()
            elif move not in self.board:
                print('Invalid move. Try again with valid coordinates (ie: A1, C3, etc.)')
            elif self.board[move] != None:
                print('Invalid move. That position is taken. Try again.')
            else:
                self.board[move] = self.player_turn

    # def check_for_tie(self):
        
game_instance=Game()
game_instance.play_game()
# print(game_instance.board, game_instance.player_turn, game_instance.tie, game_instance.winner)