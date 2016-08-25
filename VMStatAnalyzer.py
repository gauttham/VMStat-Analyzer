
import numpy as np

import matplotlib.pyplot as plt

list_values=[]

for lines in open('vmstat_splunk_24_Aug.log'):
	if ("procs" not in lines) and ("swpd" not in lines): 
		curnum= int(lines.split()[12]) + int(lines.split()[13]);
		list_values.append(curnum)

plt.plot(list_values)
plt.ylabel('Time -->')
plt.xlabel('CPU Usage')
plt.show()