import sys

rl = lambda : sys.stdin.readline()
#---------------------------------------------
def make_tilemap(grid):
    h = len(grid)
    w = len(grid[0])
#     print("h , w = ", h, w)
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

def is_empty_x(y, src_x,dst_x):
    if src_x > dst_x:
        temp = src_x
        src_x = dst_x
        dst_x = temp
        
    for i in range(src_x+1,dst_x):
        if grid[i][y] == '.':
            pass
        else:
            return False
    return True

def is_empty_y(x, src_y,dst_y):
    if src_y > dst_y:
        temp = src_y
        src_y = dst_y
        dst_y = temp
    for i in range(src_y+1,dst_y):
        if grid[x][i] == '.':
            pass
        else:
            return False
    return True

def make_empty_points(src, h ,w):
    empty_points = []
    x = src[0]
    y = src[1]
    
    for i in range(x-1,-1,-1):
        if grid[i][y] == '.':
            empty_points.append([i,y])
        else : break
    for i in range(x+1,h):
        if grid[i][y] == '.':
            empty_points.append([i,y])
        else : break
    for i in range(y-1,-1,-1):
        if grid[x][i] =='.':
            empty_points.append([x,i])
        else : break    
    for i in range(y+1,w):
        if grid[x][i] == '.':
            empty_points.append([x,i])
        else : break  
    return empty_points

def link(src, dst, h, w, n):
    if n == 4  : return False 
    can_go = False
    if src[0] == dst[0]:
        can_go =  is_empty_y(src[0], src[1], dst[1])
    elif src[1] == dst[1]:
        can_go =  is_empty_x(src[1], src[0], dst[0])
    
    if can_go == True: 
        return True
    else :
        points = make_empty_points(src, h, w)   
        for src_element in points:
            can_go = link(src_element, dst, h,w,n+1)
            if can_go == True:
                break;
        return can_go

def count_single_move(tile_map,h,w):
    single_move = 0
    for key in tile_map:
        tile_list = tile_map[key]
#         print(len(tile_list))
        for src in range(len(tile_list)):
            for dst in range(src+1, len(tile_list)):
                if link(tile_list[src],tile_list[dst],h,w,1) == True:
                    single_move += 1
    return single_move  
#--------------------------------------------------------------------

if __name__ == '__main__':
    repeat = int(rl())
    grids = []
    for n in range(repeat): 
        h_w = rl().split()
        h = int(h_w[0])
        w = int(h_w[1])
        
        grid = []
        for row in range(h):
            row = rl().strip('\n')
            grid.append(row)
    
        grids.append(grid)
        
    for grid in grids:
        h = len(grid)
        w = len(grid[0])
        tile_map = make_tilemap(grid)
        print(count_single_move(tile_map,h,w))
