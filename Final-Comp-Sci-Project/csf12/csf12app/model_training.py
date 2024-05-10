import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0



print("Shape of Training Dataset:", x_train.shape)
print("Shape of Training Dataset Labels:", y_train.shape)
print("Shape of Test Dataset:", x_test.shape)
print("Shape of Test Dataset Labels:", y_test.shape)



nb_images = 5
print(y_train[:nb_images])



train_images = np.hstack(x_train[:nb_images])
plt.imshow(train_images, cmap='Greys')



model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10),
  tf.keras.layers.Softmax()
])



print(model.summary())



loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)



model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])



hist = model.fit(x_train, y_train, epochs=10, shuffle=True, batch_size=256, validation_split=0.20)



plt.figure(0)
plt.plot(hist.history['loss'], 'g')
plt.plot(hist.history['val_loss'], 'b')
plt.plot(hist.history['accuracy'], 'r')
plt.plot(hist.history['val_accuracy'], 'black')
plt.show()



model.evaluate(x_test,  y_test, verbose=2)



model.save('my_mnist_model.keras')