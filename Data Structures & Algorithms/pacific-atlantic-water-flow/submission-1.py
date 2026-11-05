class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def flow(starts):
            seen = set(starts)
            stack = list(starts)          
            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < R and 0 <= nc < C
                            and (nr, nc) not in seen
                            and heights[nr][nc] >= heights[r][c]):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            return seen

        pacific = flow([(r, 0) for r in range(R)] + [(0, c) for c in range(C)])
        atlantic = flow([(r, C - 1) for r in range(R)] + [(R - 1, c) for c in range(C)])

        return [list(cell) for cell in pacific & atlantic]