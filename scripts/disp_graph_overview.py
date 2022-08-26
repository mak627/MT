import networkit as nk

graphReader = nk.graphio.EdgeListReader(separator=" ", firstNode = 0)
G = graphReader.read("/home/bk247056/Desktop/gap-mk/gapbs/inputs/cit-DBLP.wel")

print("************************************************")
print("******** Input Graph: cit-DBLP **********")
print("************************************************")
nk.overview(G)
print("************************************************")
