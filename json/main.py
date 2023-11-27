import json
import time

f = open('luogu.txt', 'r')
res = f.read()
res = json.loads(res)['currentData']['contests']['result']
print(res)
f.close()
get_luogu = ""
cnt_luogu = 0
pos = 0
last = 0
for ress in res:
    if ress['endTime'] < time.time():
        break
    
    timestamp = int(res[pos:last])
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    today = time.strftime("%Y-%m-%d", time_local)
    if today == time_now:
        s = "比赛名称：" + name + "\n"
        s += "比赛时间：" + dt + "\n"
        s += "比赛链接：" + "https://codeforces.com/contest/" + contest_id
        if get_cf == "": get_cf = s
        else: get_cf = s + '\n' + get_cf
        cnt_cf += 1
        
        
