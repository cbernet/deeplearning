# QCD Aware Recursive Neural Network

## Software installation

```
pip install autograd
git clone git@github.com:GaelTouquet/recnn.git
cd recnn
ln -s /data/cbernet/DeepLearning/recnn/data
```

## Repeating the results of Gilles Louppe et al

[Original paper](https://arxiv.org/abs/1702.00748)

The goal of this section is to reproduce the results of the discrimination between boosted W jets and QCD jets.

## Training a model

The network model trained by Colin is available here:

    /data/cbernet/DeepLearning/recnn/models/model.pickle

If you want to train a model yourself (takes about 8 hours on lyovis10), do:

    nohup python train.py data/w-vs-qcd/final/antikt-kt-train.pickle model.pickle &
    
## Testing a model and reproducing the plots 

Not done yet!