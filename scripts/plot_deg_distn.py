import networkit as nk
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

graphReader = nk.graphio.EdgeListReader(separator=" ", firstNode = 0)
G = graphReader.read("/home/bk247056/Desktop/gap-mk/gapbs/inputs/GAP-web-clipped.wel")
print("****************************")
print("Input Graph: GAP-web-clipped")
nk.overview(G)
print("****************************")

degree_seq = sorted(nk.centrality.DegreeCentrality(G).run().scores(), reverse=True)
degree_cnt = Counter(degree_seq)
X_deg, Y_cnt = zip(*degree_cnt.items())
X_deg = [1 + int(x ** (np.log10(20) / (5*np.log10(10)))) for x in X_deg]

# X_deg = [1 + int(x ** (1 / (3 * np.log10(10)))) for x in X_deg]

print(max(X_deg))
print("Degrees")
print(X_deg)
print("Frequency")
print(Y_cnt)

plt.figure(1)
plt.title("Degree Distribution: GAP-web")

plt.xlabel("degree")
plt.xscale("log")
#plt.xlim(0, max(X_deg))
plt.ylabel("#Nodes")
plt.yscale("log")
#plt.ylim(0, max(Y_cnt))
#plt.axis([0, max(X_deg), 0, max(Y_cnt)])
plt.plot(X_deg, Y_cnt)
#plt.show()
plt.savefig("log-gap-web.png")


