from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = defaultdict(set)
        col_sets = defaultdict(set)
        sub_sets = defaultdict(set)
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item != '.':
                    if item in row_sets[i] or item in col_sets[j] or item in sub_sets[(j // 3) * 3 + (i // 3)]:
                        return False
                    row_sets[i].add(item)
                    col_sets[j].add(item)
                    sub_sets[(j // 3) * 3 + (i // 3)].add(item)
                
        return True