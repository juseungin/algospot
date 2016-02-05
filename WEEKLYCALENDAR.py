import sys

rl = lambda : sys.stdin.readline()
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = {'Sunday':0, 'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6}
 
def main():
    global month, date
    repeat = int(rl())
    output = []
    for n in range(repeat):
        m, d, s = rl().strip('\n').split(' ')
        i_m = int(m)-1
        i_d = int(d)
        
        sunday = i_d - date[s]
        week = []
        if sunday <= 0:
            i_m -= 1
            sunday = month[i_m] + sunday 
            if i_m < 0:
                i_m = 11
        
        day = sunday
        for i in range(7):
            if day > month[i_m]:
                i_m += 1
                if i_m > 11:
                    i_m = 1
                day = 1
            week.append(day)
            day += 1
        output.append(week)
    for week in output:
        print(week[0],week[1],week[2],week[3],week[4],week[5],week[6])

if __name__ == '__main__':
    main()
