"""
TensorFlow Serving Starter (Q2)
Shows how to export a model for TF Serving.
"""
import tensorflow as tf
from tensorflow import keras
model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(5,), activation='relu'),
    keras.layers.Dense(1)
])
model.save('exported_model')
print("Model exported for TensorFlow Serving.")
# Human touch: Use docker/tensorflow/serving to serve this model.
