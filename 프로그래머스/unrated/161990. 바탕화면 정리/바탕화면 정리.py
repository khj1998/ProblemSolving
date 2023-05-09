def solution(wallpaper):
    answer = []
    paper_x = []
    paper_y = []
    rows = len(wallpaper)
    cols = len(wallpaper[0])
    
    for i in range(rows):
        for j in range(cols):
            if wallpaper[i][j] == "#":
                paper_x.append(i)
                paper_y.append(j)
    
    paper_x.sort()
    paper_y.sort()

    answer = [paper_x[0],paper_y[0],paper_x[-1]+1,paper_y[-1]+1]
    return answer