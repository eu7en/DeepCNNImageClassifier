import os 

import tensorflow as tf

print("TensorFlow is using:", "GPU" if tf.config.list_physical_devices('GPU') else "CPU")
#the line above outputs what tensorflow currently uses


#print(os.listdir('trainingData'))
#os.path.join('trainingData', 'tiger')

### setting cpu memory usage growth to avoid OOM
cpus = tf.config.experimental.list_physical_devices('CPU')

for cpu in cpus:
    tf.config.experimental.set_memory_growth(cpu, True)