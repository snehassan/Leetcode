class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(tree, node, visited=None):
            r, c, k = node
            if visited is None:
                visited = set()

            if k == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r, c) in visited:
                return False
            if tree[r][c] != word[k]:
                return False

            visited.add((r, c))

            found = (
                dfs(tree, (r + 1, c, k + 1), visited) or
                dfs(tree, (r - 1, c, k + 1), visited) or
                dfs(tree, (r, c + 1, k + 1), visited) or
                dfs(tree, (r, c - 1, k + 1), visited)
            )

            visited.remove((r, c))
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(board, (r, c, 0)):
                        return True

        return False



        
        