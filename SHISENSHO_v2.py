import sys
import cProfile
import copy

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
cnt = 0
H, W = 0, 0
grid = []
tile_grid = []
mychar = ''
line =0

def link(sx, sy, dx, dy, seg):
    global direction,cnt,H,W,grid,tile_grid,mychar, line
    line +=1
    print(line,': ', sx, sy," -> ", dx, dy,' seg=', seg)
    if line == 265:
        print("here")
    i_H, i_W = int(H), int(W)
    if seg >= 3 : return False
    if dx <0 or dx >= i_H or dy < 0 or dy >= i_W :
        return False
    
    if tile_grid[dx][dy] == mychar:
        cnt += 1
        print('find ',cnt)
        tile_grid[dx][dy] = '*'
        return True
    
    if tile_grid[dx][dy] != '.':
        return False
    
    tile_grid[dx][dy] = '*'
    
    for i in range(4):
        ni = dx + direction[i][0]
        nj = dy + direction[i][1]
        
        nseg = seg
        
        if sx != ni and sy != nj:
            nseg +=1
            
        link(dx, dy, ni, nj, nseg)
    
    tile_grid[dx][dy] = '.'
    return False

def main():
    global cnt,H,W,grid,tile_grid,mychar
    rl = lambda : sys.stdin.readline()
    repeat = int(rl())
#     output = []
    for n in range(repeat): 
        H,W = rl().split()

        for row in range(int(H)):
            row = rl().strip('\n')
            grid.append(list(row))
        
        for i in range(int(H)):
            for j in range(int(W)):
                if grid[i][j] >= 'A' and grid[i][j] <= 'Z':
                    coord = [i,j]                    
                    mychar = grid[i][j]
                    tile_grid = copy.deepcopy(grid)
                    tile_grid[i][j] = '.'
                    
                    link(coord[0], coord[1], coord[0], coord[1], 0)
                    grid[i][j] = '-'
#             print(tile_grid)
        print(cnt)
   
#     for result in output:
#         print(result)

if __name__ == '__main__':
    main()
