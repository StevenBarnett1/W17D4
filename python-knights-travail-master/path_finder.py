import tree

class KnightPathFinder:
    def __init__(self, position):
        self.position = position
        self._root = tree.Node(self.position)
        self._considered_positions = {self.position}
        self._board = self.create_board()

    def create_board(self, board = ()):
        for i in range(8):
            for j in range(8):
                board += (i, j)
        return board

    def get_valid_moves(self, position):
        (x, y) = position
        positions = []
        positions.append((x-1, y+2))
        positions.append((x-1, y-2))
        positions.append((x+1, y+2))
        positions.append((x+1, y-2))
        positions.append((x+2, y+1))
        positions.append((x-2, y+1))
        positions.append((x+2, y-1))
        positions.append((x-2, y-1))
        for current_position in positions:
            if current_position not in self._board or current_position in self._considered_positions:
                print(positions)
                print(current_position)
                positions.remove(current_position)
                # self._considered_positions.append(current_position)
        return positions

    def new_move_positions(self, position):
        for current_position in self.get_valid_moves(position):
            self._considered_positions.add(current_position)


    # def find_path(self, position):

# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}