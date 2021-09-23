import tree

class KnightPathFinder:
    def __init__(self, position):
        self.position = position
        self._root = tree.Node(self.position)
        self._considered_positions = {self.position}
        self._board = self.create_board()

    def create_board(self, board = []):
        for i in range(8):
            for j in range(8):
                board.append((i, j))
        return board

    def get_valid_moves(self, position):
        (x, y) = position
        positions = []
        result = []
        positions.append((x-1, y+2))
        positions.append((x-1, y-2))
        positions.append((x+1, y+2))
        positions.append((x+1, y-2))
        positions.append((x+2, y+1))
        positions.append((x-2, y+1))
        positions.append((x+2, y-1))
        positions.append((x-2, y-1))
        for current_position in positions:
            if current_position in self._board:
                result.append(current_position)
        return result

    def new_move_positions(self, position):
        difference = set(self.get_valid_moves(position)).difference(self._considered_positions)
        for current_position in self.get_valid_moves(position):
            if(current_position not in self._considered_positions):
                self._considered_positions.add(current_position)
        return difference

    # def find_path(self, position):

# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}
