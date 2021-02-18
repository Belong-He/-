from datetime import datetime

month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]

def tick():
    t = datetime.today()
    return t.year, t.month, t.day
def MonthLen(Tick,StartTime):
    month_31 = []
    month_30 = []
    month2 = ''
    for i in range(Tick, StartTime):  # 8-9
        if i in month31:
            month_31.append(i)
        elif i in month30:
            month_30.append(i)
        elif i == 2:
            month2 = 'True'
        else:
            month2 = ''
    return  month_31, month_30, month2
def getmonth(Tick,StartTime):  # 离开学有多少个月[2020,3,4]
    if StartTime[1] <= Tick[1] or Tick[0]>StartTime[0]:# 已经开学或是以前的课表
        if StartTime[1] <= Tick[1]:#一年内的月数
            monthlen1 = MonthLen(Tick[1] + 1, StartTime[1])
            month_31, month_30, month2 = monthlen1[0], monthlen1[1], monthlen1[2]
        elif StartTime[1] >= Tick[1]:#两年内的月数
            monthlen1 = MonthLen(StartTime[1], 13)
            month_31_front, month_30_front, month2_front = monthlen1[0], monthlen1[1], monthlen1[2]
            monthlen2 = MonthLen(1, Tick[1])
            month_31, month_30, month2 = monthlen2[0] + month_31_front, monthlen2[1] + month_30_front, monthlen2[
                2] + month2_front
        print('已经开学')
        print(len(month_31),len(month_30),month2)
        return len(month_31), len(month_30), month2
    else:  # 未开学
        if   Tick[1]<=StartTime[1]:  # 一年内的月数
            monthlen1 = MonthLen(Tick[1] + 1, StartTime[1])
            month_31, month_30, month2 = monthlen1[0], monthlen1[1], monthlen1[2]
        elif Tick[1] >= StartTime[1]:  # 两年内的月数
            monthlen1 = MonthLen(StartTime[1], 13)
            month_31_front, month_30_front, month2_front = monthlen1[0], monthlen1[1], monthlen1[2]
            monthlen2=MonthLen(1, Tick[1])
            month_31, month_30, month2=monthlen2[0]+month_31_front, monthlen2[1]+month_30_front, monthlen2[2]+month2_front
        print('未开学')
        # print(len(month_31), len(month_30), month2)
        print(month_31, month_30, month2)
        return -len(month_31), -len(month_30), month2


def get_front_day(StartTime):
    Tick = tick()
    getMonth = getmonth(Tick,StartTime)
    month_31 = getMonth[0]
    month_30 = getMonth[1]
    month2 = getMonth[2]
    print(month_31,month_30,month2)

    if StartTime[1] - Tick[1] <= 0 or Tick[0]>StartTime[0]:  # 已经开学或是以前的课表
        if month2:
            year = Tick[0]
            if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:  # 闰年
                month_day = month_31 * 31 + month_30 * 30 + Tick[2] + 29 - StartTime[2]
            else:
                month_day = month_31 * 31 + month_30 * 30 + Tick[2] + 28 - StartTime[2]
        else:
            month_day = month_31 * 31 + month_30 * 30 + Tick[2] - StartTime[2]
        print('已经开学或是以前的课表')
        print(month_day)
        return month_day
    else:  # 未开学
        if month2:
            # print('有2月')
            year = Tick[0]
            if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:  # 闰年
                month_day = -month_31 * 31 -month_30 * 30 - 29 - StartTime[2]#+ Tick[2]
            else:
                month_day = -month_31 * 31 - month_30 * 30  - 28 - StartTime[2]#+ Tick[2]
        else:
            month_day = -month_31 * 31 - month_30 * 30  - StartTime[2]# + Tick[2]
        print('未开学')
        print(month_day)
        return month_day


def ThisWeek(StartTime):
    month_day = get_front_day(StartTime)+1
    week = (month_day// 7)+1
    print('week:'+str(week))
    return week


if __name__ == "__main__":
    # StartTime = [3, 9]
    print(ThisWeek([2021, 3, 4]))