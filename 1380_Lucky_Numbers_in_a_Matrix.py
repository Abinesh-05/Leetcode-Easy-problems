class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROWS=len(matrix)
        COLS=len(matrix[0])

        min_rows=set()
        for r in range(ROWS):
            minn_ele=min(matrix[r])
            min_rows.add(minn_ele)

        max_col=set()
        maxx=0
        for c in range(COLS):
            curr_max=matrix[0][c]
            for r in range(ROWS):
                ele_max=matrix[r][c]
                curr_max=max(ele_max,curr_max)
            max_col.add(curr_max)

        for r in min_rows:
            if r in max_col:
                return [r]
        return []
