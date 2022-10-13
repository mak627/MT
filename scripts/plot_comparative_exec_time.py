import sys
import glob
import matplotlib.pyplot as plt
import numpy as np

#path = sys.argv[1]
#ifx = path.rfind("/")
#filename = path[ifx+1:]
file_path1 = sys.argv[1] + "/*"
file_path2 = sys.argv[2] + "/*"
files_list1 = glob.glob(file_path1)
files_list2 = glob.glob(file_path2)
files_list1.sort()
files_list2.sort()

labels = [1, 2, 4, 8, 16, 24, 32, 48]
thread_num_delta = []
exec_time_delta = []
thread_num_adap_delta = []
exec_time_adap_delta = []

for file_name in files_list1:
  print("\n")
  with open(file_name, "r") as f:
    for line in f:
        if('OMP_NUM_THREADS' in line):
          idx = line.find('=')
          OMP_NUM_THREADS = int(line[idx+1:].lstrip().rstrip().strip("'"))
          #print("OMP_NUM_THREADS = " + str(OMP_NUM_THREADS), end=', ')
          thread_num_delta.append(OMP_NUM_THREADS)        

        if('Average Time:' in line):
          idx = line.find(':')
          AVG_EXEC_TIME = float(line[idx+1:].lstrip().rstrip())
          AVG_EXEC_TIME = round(AVG_EXEC_TIME, 8)
          #print("AVG_EXEC_TIME = " + str(AVG_EXEC_TIME), end='')
          exec_time_delta.append(AVG_EXEC_TIME)

for file_name in files_list2:
  print("\n")
  with open(file_name, "r") as f:
    for line in f:
        if('OMP_NUM_THREADS' in line):
          idx = line.find('=')
          OMP_NUM_THREADS = int(line[idx+1:].lstrip().rstrip().strip("'"))
          #print("OMP_NUM_THREADS = " + str(OMP_NUM_THREADS), end=', ')
          thread_num_adap_delta.append(OMP_NUM_THREADS)

        if('Average Time:' in line):
          idx = line.find(':')
          AVG_EXEC_TIME = float(line[idx+1:].lstrip().rstrip())
          AVG_EXEC_TIME = round(AVG_EXEC_TIME, 8)
          #print("AVG_EXEC_TIME = " + str(AVG_EXEC_TIME), end='')
          exec_time_adap_delta.append(AVG_EXEC_TIME)

sorted_exec_time_delta = []
sorted_exec_time_adap_delta = []

for i in range(len(labels)):
  idx_delta = thread_num_delta.index(labels[i])
  sorted_exec_time_delta.append(exec_time_delta[idx_delta])
  idx_adap_delta = thread_num_adap_delta.index(labels[i])
  sorted_exec_time_adap_delta.append(exec_time_adap_delta[idx_adap_delta])

for i in range(len(sorted_exec_time_delta) - 1):
  sorted_exec_time_delta[i+1] = round((sorted_exec_time_delta[i+1] / sorted_exec_time_delta[0]), 4)
  print(sorted_exec_time_delta[i+1])
sorted_exec_time_delta[0] = 1

for i in range(len(sorted_exec_time_adap_delta) - 1):
  sorted_exec_time_adap_delta[i+1] = round((sorted_exec_time_adap_delta[i+1] / sorted_exec_time_adap_delta[0]), 4)
  print(sorted_exec_time_adap_delta[i+1])
sorted_exec_time_adap_delta[0] = 1

X = np.arange(len(labels))	# the label locations
width = 0.30

fig, ax = plt.subplots()
rects1 = ax.bar(X-width/2, sorted_exec_time_delta, width, label='Delta')
rects2 = ax.bar(X+width/2, sorted_exec_time_adap_delta, width, label='AdapDelta')
ax.set_xticks(X)
sorted_thread_labels = sorted(labels)
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)  

ax.set_title('THREADS v. EXEC_TIME (GAP-web)')
ax.set_ylabel('EXEC_TIME (in secs)')
ax.set_xlabel('#THREADS');
ax.set_xticklabels(sorted_thread_labels)
fig.tight_layout()

plt.show()
#plt.savefig(path + "/" + filename + '_plot.jpg')