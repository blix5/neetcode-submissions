class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_sets = [set() for _ in range(9)]
        sub_sets = [set() for _ in range(9)]
        for i in range(len(board)):
            row = board[i]
            row_set = set()

            for j in range(len(row)):
                item = row[j]
                if item != '.':
                    if item in row_set or item in col_sets[j] or item in sub_sets[(j // 3) * 3 + (i // 3)]:
                        return False
                    row_set.add(item)
                    col_sets[j].add(item)
                    sub_sets[(j // 3) * 3 + (i // 3)].add(item)
                
        return True