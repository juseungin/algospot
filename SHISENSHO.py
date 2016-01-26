import sys

rl = lambda : sys.stdin.readline()
#---------------------------------------------
def make_tilemap(grid , h, w):
    map = dict()
    for i in range(h):
        for j in range(w):
            key = grid[i][j]
            if key != '.':
                value_list = map.get(key)
                if value_list == None:
                    value_list = [[i,j]]
                else:
                    value_list.append([i,j])
                map[key] = value_list
    return map

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

def make_empty_points(grid, src, h ,w):
    x = src[0]
    y = src[1]
    
    for i in range(x-1,-1,-1):
        if grid[i][y] == '.':
            yield [i,y]
        else : break
    for i in range(x+1,h):
        if grid[i][y] == '.':
            yield [i,y] 
        else : break
    for i in range(y-1,-1,-1):
        if grid[x][i] =='.':
            yield [x,i] 
        else : break    
    for i in range(y+1,w):
        if grid[x][i] == '.':
            yield [x,i] 
        else : break  

def can_link(grid, src, dst, h, w, n):
    if n == 4  : return False 
    link = False
    if src[0] == dst[0]:
        link =  is_empty_y(grid, src[0], src[1], dst[1])
    elif src[1] == dst[1]:
        link =  is_empty_x(grid, src[1], src[0], dst[0])
    
    if link == True: 
        return True
    else :
        for src_element in make_empty_points(grid, src, h, w):
            link = can_link(grid, src_element, dst, h , w,n+1)
            if link == True:
                break;
        return link

def map_to_list(tile_map):
    start = False
    start_index = 0
    end_index = 0
    for i in range(len(tile_map)):
        if tile_map[i] >='A' and tile_map[i] <= 'Z':
            pass
        else :
            if start == False :
                start = True 
                start_index = i
            else : 
                end_index = i
                yield tile_map[start_index:end_index]    

def count_link(grid, tile_map,h,w):
    cnt = 0
    for key in tile_map:
        tile_list = tile_map[key]
        for src in range(len(tile_list)):
            for dst in range(src+1, len(tile_list)):
                if can_link(grid, tile_list[src],tile_list[dst],h,w,1) == True:
                    cnt += 1
    return cnt  
#--------------------------------------------------------------------
if __name__ == '__main__':
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
    print(output)

