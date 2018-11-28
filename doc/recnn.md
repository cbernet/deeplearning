# QCD Aware Recursive Neural Network

## Software installation

```
git clone git@github.com:GaelTouquet/recnn.git -b refactoring
cd recnn
ln -s /data/conda/recnn/data
ln -s /data/conda/recnn/data_gilles_louppe
ln -s /data/conda/recnn/models
```

Pour executer certain script de plotting il vous faudra aussi recuperer le package cpyroot:
```
git clone git@github.com:cbernet/cpyroot.git
cd cpyroot
source init.sh
```

## Repeating the results of Gilles Louppe et al

[Original paper](https://arxiv.org/abs/1702.00748)

The goal of this section is to reproduce the results of the discrimination between boosted W jets and QCD jets.

## Preprocessing, Training, Testing

Those three steps can be done in a single cfg file that can be used like :

    nohup ipython Hadronic_taus_cfg.py <path to the working directory that will be created> > Hadronic_taus_cfg.out &
    
The rootfiles with the input and the test results are in <workdir>/rawBackground.root and <workdir>/rawSignal.root for background (QCD jets) and signal (hadronic taus) respectively.
    
## Plot ROC curves

    python ROC.py <path to working directory>
    
The produced ROC curves will be in <workdir>/ROCs.root .
