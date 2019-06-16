class State:
    '''
    grid_size: The number of dots on a side of the board (board must be square).
    '''
    def __init__(self, grid_size):
        self.grid_size = grid_size;
        self.p1_boxes = set()
        self.p2_boxes = set()
        self.edges = set()
        self.winner = 0
        self.boxes = []
        for col_idx in range(grid_size - 1):
            for row_idx in range(grid_size - 1):
                self.boxes.append(Box(grid_size, (row_idx, col_idx)))
    
    '''
    player: The player that played the move.
    edge: The edge that was played.
    return: The player who goes next.
    '''
    def play_move(self, player, edge):
        self.edges.add(edge)
        all_complete_boxes = set()
        for i in range(len(self.boxes)):
            if self.boxes[i].complete(self.edges):
                all_complete_boxes.add(i)
        newly_completed_boxes = all_complete_boxes - self.p1_boxes - self.p2_boxes

        if player == 1:
            self.p1_boxes = self.p1_boxes | newly_completed_boxes
        else:
            self.p2_boxes = self.p2_boxes | newly_completed_boxes
        if self.get_winner() != 0:
            return 0

        if len(newly_completed_boxes) > 0:
            return player
        if player == 1:
            return 2
        else:
            return 1
             

    def points_to_win(self):
        return (((self.grid_size - 1)**2) / 2) + 1

    def get_winner(self):
        if len(self.p1_boxes) >= self.points_to_win():
            winner = 1
            return 1
        elif len(self.p2_boxes) >= self.points_to_win():
            winner = 2
            return 2
        return 0

    def draw(self):
        print(self.edges)
        print('Player 1 score: {}'.format(len(self.p1_boxes)))
        print('Player 2 score: {}'.format(len(self.p2_boxes)))
        '''
        board_str = ''
        max_edge_idx = 2 * n**2 - 2 * n
        idx = 0
        row_idx = 0
        box_idx = 0
        while idx < max_edge_idx:
            if row_idx % 2 == 0:
                for i in range(self.grid_size - 1):
                    board_str += '.'
                    if idx in self.edges:
                        board_str += '---'
                    else:
                        board_str += '{:03d}'.format(idx)
                    idx += 1
                board_str += '.'
            else:
                for i in range(self.grid_size - 1):
                    if idx in self.edges:
                        board_str += '|'
                    else:
                        board_str += 
        '''
        pass






class Box:
    def __init__(self, grid_size, coordinate):
        self.x, self.y = coordinate[0], coordinate[1]
        top = self.y * (2 * grid_size - 1) + self.x
        left = top + grid_size - 1
        right = left + 1
        bottom = top + (2 * grid_size - 1)
        self.edges = set([top, left, right, bottom])

    '''
    Return whether this box is complete, given a set of all edges that have been taken
    game_edges: A set of all the edges that have been completed
    '''
    def complete(self, game_edges):
        return len(game_edges & self.edges) == 4

