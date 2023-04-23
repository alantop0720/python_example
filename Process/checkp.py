import psutil
 
def judgeprocess(processname):
    pl = psutil.pids()
    print(pl)
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            print(pid)
            break
    else:
        print("not found")
        
if judgeprocess('alantop_tool.exe') == 0:
    print('success')
else:
    print('无')