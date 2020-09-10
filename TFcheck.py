import tensorflow as tf
#import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

print(tf.test.is_built_with_cuda())

print(tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None))
print(tf.__version__)

if tf.test.is_built_with_cuda() and tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None):
    print('You can use GPU')

else:
    print('TF can not use GPU')