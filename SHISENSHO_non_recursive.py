import sys
import cProfile

def make_tileset(grid):
    tile_set = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tile_info = grid[i][j]
            if tile_info != '.':
                if not(tile_info in tile_set) : 
                    tile_set.append(tile_info)
                    tile_set.append([i,j])
                else :
                    idx = tile_set.index(tile_info)
                    tile_set.insert(idx+1,[i,j])
    
    return tile_set

def get_list_from_set(tile_map):
    start = False
    start_index, end_index = 0, 0
    for i in range(len(tile_map)):
        if type (tile_map[i]) == str:
            if start == True:
                start = False
                yield tile_map[start_index:end_index+1]                
        else :
            if start == False :
                start = True 
                start_index = i
            else : 
                end_index = i
    yield tile_map[start_index:end_index+1] 

def is_empty_x(grid, y, src_x, dst_x):
    if src_x > dst_x:
        src_x,dst_x = dst_x,src_x
        
    for i in range(src_x+1,dst_x):
        if grid[i][y] == '.': pass
        else: return False
    return True

def is_empty_y(grid, x, src_y,dst_y):
    if src_y > dst_y:
        src_y,dst_y = dst_y,src_y

    for i in range(src_y+1,dst_y):
        if grid[x][i] == '.': pass
        else: return False
    return True

def make_empty_points(grid, src_x, src_y,):  
    for i in range(src_x-1,-1,-1):
        if grid[i][src_y] == '.':
            yield i,src_y
        else : break
    for i in range(src_x+1,len(grid)):
        if grid[i][src_y] == '.':
            yield i,src_y 
        else : break
    for i in range(src_y-1,-1,-1):
        if grid[src_x][i] =='.':
            yield src_x,i
        else : break    
    for i in range(src_y+1,len(grid[0])):
        if grid[src_x][i] == '.':
            yield src_x,i 
        else : break  

def can_link_non_rec(grid, src_x, src_y, dst_x, dst_y, n):
    link = False
    if src_x == dst_x:
        link =  is_empty_y(grid, src_x, src_y, dst_y)
    elif src_y == dst_y:
        link =  is_empty_x(grid, src_y, src_x, dst_x)
    if link == True: 
        return True
    
    for src_x2,src_y2 in make_empty_points(grid, src_x, src_y):
        if src_x2 == dst_x:
            link =  is_empty_y(grid, src_x2, src_y2, dst_y)
        elif src_y2 == dst_y:
            link =  is_empty_x(grid, src_y2, src_x2, dst_x)
        if link == True: 
            return True
        for src_x3, src_y3 in make_empty_points(grid, src_x2, src_y2):
            if src_x3 == dst_x:
                link =  is_empty_y(grid, src_x3, src_y3, dst_y)
            elif src_y3 == dst_y:
                link =  is_empty_x(grid, src_y3, src_x3, dst_x)
            if link == True: 
                return True
    return False

def count_link(grid, tile_set):
    cnt = 0
    for tile_list in get_list_from_set(tile_set):
        for src in range(len(tile_list)):
            for dst in range(src+1, len(tile_list)):
                if can_link_non_rec(grid, tile_list[src][0], tile_list[src][1], tile_list[dst][0], tile_list[dst][1], 1) == True:
                    cnt += 1
    return cnt  

def main():
    rl = lambda : sys.stdin.readline()
    repeat = int(rl())
    output = []
    for n in range(repeat): 
        h,w = rl().split()
        grid = []

        for row in range(int(h)):
            row = rl().strip('\n')
            grid.append(row)
        
        tile_set = make_tileset(grid)
        output.append(count_link(grid, tile_set))

    for result in output:    
        print(result)

if __name__ == '__main__':
    cProfile.run('main()')
