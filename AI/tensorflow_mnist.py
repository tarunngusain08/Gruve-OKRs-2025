"""
A simple TensorFlow example: MNIST digit classification
Shows basic deep learning workflow with comments for clarity.
"""
import tensorflow as tf
from tensorflow.keras import layers, models, datasets

# 1. Data loading
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 2. Model definition
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 3. Training setup
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 4. Training
model.fit(x_train, y_train, epochs=2, batch_size=64, verbose=2)

# 5. Evaluation
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print(f'Accuracy: {acc:.2%}')

# Human touch: Try changing epochs, batch size, or model layers to see the effect!
