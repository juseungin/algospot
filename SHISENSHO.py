import sys
import cProfile

cache = {}

def make_tilemap_arr(grid, h, w):
    map = []
    for i in range(h):
        for j in range(w):
            tile_info = grid[i][j]
            if tile_info != '.':
                if not(tile_info in map) : 
                    map.append(tile_info)
                    map.append([i,j])
                else :
                    idx = map.index(tile_info)
                    map.insert(idx+1,[i,j])
    
    return map

def map_to_list(tile_map):
    start = False
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

def is_empty_x(grid, y, src_x,dst_x):
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

def make_empty_points(grid, x, y, h ,w):

    for i in range(x-1,-1,-1):
        if grid[i][y] == '.':
            yield i,y
        else : break
    for i in range(x+1,h):
        if grid[i][y] == '.':
            yield i,y 
        else : break
    for i in range(y-1,-1,-1):
        if grid[x][i] =='.':
            yield x,i
        else : break    
    for i in range(y+1,w):
        if grid[x][i] == '.':
            yield x,i
        else : break  

def can_link(grid, a_src_x, a_src_y, a_dst_x, a_dst_y, h, w, n):
    key = (a_src_x, a_src_y, a_dst_x, a_dst_y)
    if key in cache.keys() and cache[key] < n:
        return True
    if n == 0  : return False
    if n == 1 : 
        if not (a_src_x == a_dst_x or a_src_y == a_dst_y): return False
    link = False
    if a_src_x == a_dst_x:
        link =  is_empty_y(grid, a_src_x, a_src_y, a_dst_y)
    elif a_src_y == a_dst_y:
        link =  is_empty_x(grid, a_src_y, a_src_x, a_dst_x)   
    if link == True:
        cache[key] = 1
        return True

    for i in range(a_src_x+1,h): #right
        if grid[i][a_src_y] == '.':
            if can_link(grid, i, a_src_y,  a_dst_x, a_dst_y, h , w, n-1): 
                if key in cache.keys() and cache[key] > n-1:
                    cache[key] = n-1
                return True
        else : break   
    for i in range(a_src_y+1,w): #down
        if grid[a_src_x][i] == '.':
            if can_link(grid, a_src_x, i,  a_dst_x, a_dst_y, h , w, n-1): 
                if key in cache.keys() and cache[key] > n-1:
                    cache[key] = n-1
                return True
        else : break  
    for i in range(a_src_x-1,-1,-1): #left
        if grid[i][a_src_y] == '.':
            if can_link(grid, i, a_src_y,  a_dst_x, a_dst_y, h , w, n-1): 
                if key in cache.keys() and cache[key] > n-1:
                    cache[key] = n-1
                return True
        else : break
    for i in range(a_src_y-1,-1,-1): #up
        if grid[a_src_x][i] =='.':
            if can_link(grid, a_src_x, i,  a_dst_x, a_dst_y, h , w, n-1): 
                if key in cache.keys() and cache[key] > n-1:
                    cache[key] = n-1
                return True
        else : break 

    return False


def count_link(grid, tile_map,h,w):
    cnt = 0
    for tile_list in map_to_list(tile_map):
        for src in range(len(tile_list)):
            for dst in range(src+1, len(tile_list)):
                if can_link(grid, tile_list[src][0], tile_list[src][1], tile_list[dst][0], tile_list[dst][1], h, w, 3) == True:
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
        
        tile_map = make_tilemap_arr(grid, int(h), int(w))
        output.append(count_link(grid, tile_map, int(h), int(w)))
    for result in output:
        print(result)

if __name__ == '__main__':
    main()
