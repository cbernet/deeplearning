# Getting started with deep learning

## Software

### Centrally maintained on cmsgpu-Area-51-R4

- cuda 8.0.61-1 amd64 (version 9 does not work with tensorflow)
- Wing IDE

### Additional packages

#### Anaconda

Anaconda provides the majority of the scientific python packages. To install:

```
bash /opt/deeplearning/Anaconda2-5.0.1-Linux-x86_64.sh
```

An anaconda virtual environment will be used to install additional deep learning packages:

- tensorflow-gpu
- keras

Create your virtual environment:

```
conda create -n tf-gpu python=2.7
```

Activate it (everytime you want to use it):

```
source activate tf-gpu
```

To deactivate it, you can do the following, **but don't do it now**.

```
source deactivate
```

#### TensorFlow

**Make sure to first activate your virtual environment as explained above.**

```
pip install tensorflow-gpu==1.4
```

Test it by running this python script:

```python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

You get:

```
2017-12-04 15:55:52.967528: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 AVX512F FMA
2017-12-04 15:55:53.252195: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties:
name: GeForce GTX 1080 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.582
pciBusID: 0000:17:00.0
totalMemory: 10.91GiB freeMemory: 10.75GiB
2017-12-04 15:55:53.519858: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 1 with properties:
name: GeForce GTX 1080 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.582
pciBusID: 0000:65:00.0
totalMemory: 10.91GiB freeMemory: 10.24GiB
2017-12-04 15:55:53.520374: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Device peer to peer matrix
2017-12-04 15:55:53.520396: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1051] DMA: 0 1
2017-12-04 15:55:53.520400: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1061] 0:   Y Y
2017-12-04 15:55:53.520402: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1061] 1:   Y Y
2017-12-04 15:55:53.520409: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:17:00.0, compute capability: 6.1)
2017-12-04 15:55:53.520412: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:1) -> (device: 1, name: GeForce GTX 1080 Ti, pci bus id: 0000:65:00.0, compute capability: 6.1)
Hello, TensorFlow!
```

#### keras

**Make sure to first activate your virtual environment as explained above.**

```
pip install keras
```
Check your `~/.keras/keras.json` and make sure it looks like this:

```json
{
    "epsilon": 1e-07,
    "floatx": "float32",
    "image_data_format": "tf",
    "backend": "tensorflow"
}
```

In particular, "image_data_format" should be set to "tf" and "backend" to "tensorflow".

[Get started with Keras](https://keras.io/getting-started/sequential-model-guide/)

To save your Keras models you will need h5py:

```
pip install h5py
```

## Test CUDA

```
/usr/local/cuda-8.0/extras/demo_suite/nbody -benchmark -numbodies=256000 -device=0
```

Should print:

```
Run "nbody -benchmark [-numbodies=<numBodies>]" to measure performance.
	-fullscreen       (run n-body simulation in fullscreen mode)
	-fp64             (use double precision floating point values for simulation)
	-hostmem          (stores simulation data in host memory)
	-benchmark        (run benchmark to measure performance)
	-numbodies=<N>    (number of bodies (>= 1) to run in simulation)
	-device=<d>       (where d=0,1,2.... for the CUDA device to use)
	-numdevices=<i>   (where i=(number of CUDA devices > 0) to use for simulation)
	-compare          (compares simulation results running once on the default GPU and once on the CPU)
	-cpu              (run n-body simulation on the CPU)
	-tipsy=<file.bin> (load a tipsy model file for simulation)

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

> Windowed mode
> Simulation data stored in video memory
> Single precision floating point simulation
> 1 Devices used for simulation
gpuDeviceInit() CUDA Device [0]: "GeForce GTX 1080 Ti
> Compute 6.1 CUDA device: [GeForce GTX 1080 Ti]
number of bodies = 256000
256000 bodies, total time for 10 iterations: 1932.708 ms
= 339.089 billion interactions per second
= 6781.781 single-precision GFLOP/s at 20 flops per interaction

```
