# Getting started with deep learning

## Software

The needed software is in a separate conda environment. 

Activate it (everytime you want to use it):

```
conda activate tf-gpu
```

To deactivate it, you can do the following, **but don't do it now**.

```
conda deactivate
```

#### TensorFlow

Test that TensorFlow is working properly: 

```
python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
```

You should get a printout like: 

```
2019-02-19 16:13:55.798638: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 AVX512F FMA
2019-02-19 16:13:56.000996: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1432] Found device 0 with properties: 
name: GeForce GTX 1080 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.582
pciBusID: 0000:17:00.0
totalMemory: 10.92GiB freeMemory: 10.76GiB
2019-02-19 16:13:56.148129: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1432] Found device 1 with properties: 
name: GeForce GTX 1080 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.582
pciBusID: 0000:65:00.0
totalMemory: 10.91GiB freeMemory: 10.71GiB
2019-02-19 16:13:56.148991: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1511] Adding visible gpu devices: 0, 1
2019-02-19 16:13:56.571692: I tensorflow/core/common_runtime/gpu/gpu_device.cc:982] Device interconnect StreamExecutor with strength 1 edge matrix:
2019-02-19 16:13:56.571724: I tensorflow/core/common_runtime/gpu/gpu_device.cc:988]      0 1 
2019-02-19 16:13:56.571730: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1001] 0:   N Y 
2019-02-19 16:13:56.571733: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1001] 1:   Y N 
2019-02-19 16:13:56.572306: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 10407 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:17:00.0, compute capability: 6.1)
2019-02-19 16:13:56.572660: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:1 with 10358 MB memory) -> physical GPU (device: 1, name: GeForce GTX 1080 Ti, pci bus id: 0000:65:00.0, compute capability: 6.1)
tf.Tensor(11.957642, shape=(), dtype=float32)
```

#### keras

Check your `~/.keras/keras.json` and make sure it looks like this:

```json
{
    "backend": "tensorflow",
    "floatx": "float32",
    "epsilon": 1e-07,
    "image_data_format": "channels_first"
}
```

In particular: 
 
* `image_data_format` should be set to "channels_first" and 
* "backend" to "tensorflow".

[Get started with Keras](https://keras.io/getting-started/sequential-model-guide/)

## Add a small deep learning test here