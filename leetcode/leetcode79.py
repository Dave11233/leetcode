class Solution:
    def exist(self, board, word: str) -> bool:
        if not word:
            return True
        if not board and len(word) > 0:
            return False

        def helper(location_x, location_y, word_location, visited):
            if word_location > len(word) - 1:
                return True
            if location_x < 0 or location_x >= len(board[0]) or location_y < 0 or location_y >= len(board):
                # 越界
                return False

            if word[word_location] != board[location_y][location_x] or visited[location_y][location_x]:
                return False
            visited[location_y][location_x] = True
            if word[word_location] == board[location_y][location_x]:

                if helper(location_x + 1, location_y, word_location + 1, visited) or \
                        helper(location_x - 1, location_y, word_location + 1, visited) or \
                        helper(location_x, location_y - 1, word_location + 1, visited) or \
                        helper(location_x, location_y + 1, word_location + 1, visited):
                    return True

            visited[location_y][location_x] = False
            return False

        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] == word[0]:
                    visited = [[False] * len(board[0]) for _ in range(len(board))]
                    if helper(i, j, 0, visited):
                        return True
        return False


if __name__ == '__main__':
    print(Solution().exist([["A"]]
                           , "A"))
