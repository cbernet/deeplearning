from ROOT import TTree, TBranch, TFile
import numpy as np

f = TFile('test.root','recreate')
tree = TTree("tree", "my tree")

p4s = np.zeros((10,4))
tree.Branch("ptcs",p4s,'ptcs[10][4]/D')

for i in range(20):
    for j in range(10):
        p4s[j,0]=j+i*10
    tree.Fill()
f.Write()
f.Close()
