TFile f("/data/gtouquet/samples_root/QCD0.root");
TTree *t = (TTree*)f.Get("tree");
TTreeReader reader("tree", &f);
TTreeReaderValue<double> gen_pt(reader, "GenJet_pt");

void jetvarconv() {
  unsigned i=0;
  while(reader.Next()) {
    float pt = *gen_pt;
    if (i%10==0)
      std::cout<<i<<" "<<pt<<std::endl;
    i+=1;
  }
}
