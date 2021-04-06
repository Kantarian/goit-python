from datetime import *

users = {
    'Yehor':[1994,7,26],
    'Alex':[1995,4,13],
    'Max':[1991,4,12],
    'Maxim':[1992,4,10]
}

def weekday(dday):
    if dday == 1:
        return 'Monday'
    if dday == 2:
        return 'Tuesday'
    if dday == 3:
        return 'Wednesday'
    if dday == 4:
        return 'Thursday'        
    if dday == 5:
        return 'Friday'
    if dday == 6:
        return 'Saturday'
    if dday == 7:
        return 'Sunday'
    else:
        pass

def congratulate():
    today_is = date.today()
    today_is = today_is.strftime("%Y,%m,%d")
    today_is = today_is[0:4] + today_is[4:].replace('0','')
    today_is_list = []
    today_is_list.append(int(today_is[0:4]))
    today_is_list.append(int(today_is[5:6]))
    today_is_list.append(int(today_is[7:]))
    now_ywd = datetime(today_is_list[0],today_is_list[1],today_is_list[2]).isocalendar()
    now_y_w_d = []
    for n_ywd in now_ywd:
        now_y_w_d.append(n_ywd)

    for bd_name in users.keys():
        bd = users.get(bd_name)
        bd[0] = today_is_list[0]
        bd_ywd = datetime(bd[0],bd[1],bd[2]).isocalendar()
        bd_y_w_d = []
        for bd_ywd in bd_ywd:
            bd_y_w_d.append(bd_ywd)   
        if bd_y_w_d[1] == now_y_w_d[1] + 1:
            if bd_y_w_d[2] !=6 and bd_y_w_d[2] !=7:
                print(weekday(bd_y_w_d[2]) + ': ' + bd_name)
        if bd_y_w_d[1] == now_y_w_d[1]:
            if bd_y_w_d[2] == 6 or bd_y_w_d[2] == 7:
                print(weekday(1) + ': ' + bd_name)
        else:
            pass

def main():
    congratulate()
    

if __name__ == '__main__':
    main()
