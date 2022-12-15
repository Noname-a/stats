from stats import MinStat, MaxStat, AverageStat

values = [1, 5, 4, 2]
 
mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
 
print(mins.result(), maxs.result(), '{:<09.3}'.format(average.result()))