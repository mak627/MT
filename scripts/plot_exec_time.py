import sys
import glob
import matplotlib.pyplot as plt
import numpy as np

path = sys.argv[1]
ifx = path.rfind("/")
filename = path[ifx+1:]
file_path = path + "/*"
list_files = glob.glob(file_path)
print(list_files)

thread_num = []
exec_time = []

list_files.sort()
for file_name in list_files:
    print("\n")

    with open(file_name, "r") as f:
        for line in f:
            if('OMP_NUM_THREADS' in line):
                idx = line.find('=')
                OMP_NUM_THREADS = int(line[idx+1:].lstrip().rstrip().strip("'"))
                print("OMP_NUM_THREADS = " + str(OMP_NUM_THREADS), end=', ')
                thread_num.append(OMP_NUM_THREADS)
            
            if('Average Time:' in line):
                
                idx = line.find(':')
                AVG_EXEC_TIME = float(line[idx+1:].lstrip().rstrip())
                AVG_EXEC_TIME = round(AVG_EXEC_TIME, 4)
                print("AVG_EXEC_TIME = " + str(AVG_EXEC_TIME), end='')
                exec_time.append(AVG_EXEC_TIME)


sorted_thread_num = thread_num[:]
sorted_exec_time = []
sorted_thread_num.sort()
for i in range(len(thread_num)):
	idx = thread_num.index(sorted_thread_num[i])
	sorted_exec_time.append(exec_time[idx])

print(thread_num)
print(exec_time)
print('*****************')
print(sorted_thread_num)
print(sorted_exec_time)
myDict = {"#THREADS": sorted_thread_num, "EXEC_TIME": sorted_exec_time}

fig, ax = plt.subplots(figsize = (7,5))
idx = np.asarray([i for i in range(len(myDict["#THREADS"]))])
ax.bar(idx, myDict["EXEC_TIME"], width=0.2, color='green')
xlabels = myDict["#THREADS"]
ax.set_xticks(idx)
ax.set_xticklabels(myDict["#THREADS"], rotation ='horizontal')
  
ax.set_title('THREADS v. EXEC_TIME (' + filename + ')')
ax.set_ylabel('EXEC_TIME (in secs)')
ax.set_xlabel('#THREADS');
fig.tight_layout()
plt.savefig(path + "/" + filename + '_plot.jpg')
