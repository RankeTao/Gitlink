
import matplotlib.pyplot as plt 
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train.shape
y_train.shape
type(x_train)

a = plt.imshow(x_train[0,:,:], cmap='gray')
plt.show(a)
for i in range(3):
    plt.imshow(x_train[i,:,:], cmap='gray')
    plt.title(y_train[i])
    plt.show()
    print(y_train[i])
