from state import State
from human_agent import Human

class Game:
    '''
    grid_size: The number of dots on a side of the board.
    p1: Agent for the player that will go first.
    p2: Agent for the player that will go second.
    '''
    def __init__(self, grid_size, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.s = State(grid_size)

    def play(self):
        turn = 1
        while turn != 0:
            self.s.draw()
            if turn == 1:
                print('Player 1')
                edge = self.p1.play_move(self.s)
            elif turn == 2:
                print('Player 2')
                edge = self.p2.play_move(self.s)
            turn = self.s.play_move(turn, edge)

            # TODO: Draw the state?
        print('Winner is player ' + self.s.get_winner())
        return self.s.get_winner()

if __name__ == '__main__':
    size = int(input('Grid size: '))
    g = Game(size, Human(), Human())
    g.play()
