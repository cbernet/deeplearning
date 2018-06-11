from ROOT import TFile, TTree

f = TFile('/data/gtouquet/samples_root/QCD0.root')
tree = f.Get('tree')

print 'starting to loop' 
for i,jet in enumerate(tree):
    print i
    # pt = jet.GenJet_pt
