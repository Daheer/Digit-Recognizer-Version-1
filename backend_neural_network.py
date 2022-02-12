import numpy as np # library import
import pandas as pd
import cv2
import matplotlib.pyplot as plt

np.random.seed(42)

def relu(Z):
    return np.maximum(0, Z)
def sigmoid(Z):
    return 1/(1+np.exp(-Z))
def relu_inv(Z):
    return Z > 0

class NeuralNetwork:
    def __init__(self, X, Y, n_h, learning_rate, iterations):
        self.X = X
        self.Y = Y
        self.n_x = X.shape[0]
        self.n_h = n_h
        self.n_y = Y.shape[0] 
        self.W1 = np.random.rand(self.n_h, self.n_x) - 0.5
        #Weights: Initalized with random numbers
        self.b1 = np.zeros((self.n_h, 1))
        #Biases: initialized with zeros
        self.W2 = np.random.rand(self.n_y, self.n_h) - 0.5
        self.b2 = np.zeros((self.n_y, 1))
        self.learning_rate = learning_rate
        self.iterations = iterations
    def forward_propagate(self):
        W1 = self.W1
        b1 = self.b1
        W2 = self.W2
        b2 = self.b2
        X = self.X
        Z1 = W1.dot(X) + b1
        A1 = relu(Z1)
        Z2 = W2.dot(A1) + b2
        A2 = sigmoid(Z2)
        self.Z1 = Z1
        self.A1 = A1
        self.Z2 = Z2
        self.A2 = A2
    def backward_propagate(self):
        m = self.Y.shape[1]
        X = self.X
        W1 = self.W1
        W2 = self.W2
        Z1 = self.Z1
        A1 = self.A1
        Z2 = self.Z2
        A2 = self.A2
        dZ2 = A2 - Y
        dW2 = dZ2.dot(A1.T) / m
        db2 = np.sum(dZ2) / m
        dA1 = W2.T.dot(dZ2)
        dZ1 = dA1 * relu_inv(Z1)
        dW1 = dZ1.dot(X.T) / m
        db1 = np.sum(dZ1) / m
        self.dW1 = dW1
        self.db1 = db1
        self.dW2 = dW2
        self.db2 = db2
    def compute_loss(self):
        m = self.Y.shape[1]
        Y = self.Y
        A2 = self.A2
        loss = np.multiply(Y, np.log(A2)) + np.multiply((1 - Y), np.log(1 - A2))
        loss = - np.sum(loss)
        loss /= m
        return loss
    def optimize(self):
        W1 = self.W1
        b1 = self.b1
        W2 = self.W2
        b2 = self.b2
        dW1 = self.dW1
        db1 = self.db1
        dW2 = self.dW2
        db2 = self.db2
        learning_rate = self.learning_rate
        W1 = W1 - (learning_rate * dW1)
        b1 = b1 - (learning_rate * db1)
        W2 = W2 - (learning_rate * dW2)
        b2 = b2 - (learning_rate * db2)
        self.W1 = W1
        self.b1 = b1
        self.W2 = W2
        self.b2 = b2
    def train(self):
        print("Training Network...")
        for i in range(self.iterations):
            self.forward_propagate()
            self.compute_loss()
            self.backward_propagate()
            self.optimize()
            if (i % 100 == 0):
                print("Loss at iteration", i, ":", self.compute_loss())
    def predict(self, X):
        W1 = self.W1
        b1 = self.b1
        W2 = self.W2
        b2 = self.b2
        Z1 = W1.dot(X) + b1
        A1 = relu(Z1)
        Z2 = W2.dot(A1) + b2
        A2 = sigmoid(Z2)
        prediction = A2 > 0.5
        prediction = prediction.astype(int)
        return prediction

train = np.array(pd.read_csv('mnist_train.csv'))
train = train[0:12664, :]

np.random.shuffle(train)

X_train = train[:, 1:785]
Y_train = train[:, 0]

X_train = X_train / 255.

X_train = X_train.T
Y_train = Y_train.T

Y_train = Y_train.reshape(1, 12664)

X = X_train
Y = Y_train

model = NeuralNetwork(X, Y, 24, 0.5, 3000)


def call():
    model.train()

def callpre(image="image.jpg"):
    # img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    #
    # scale_percent = 10  # percent of original size
    # width = int(img.shape[1] * scale_percent / 100)
    # height = int(img.shape[0] * scale_percent / 100)
    # dim = (width, height)
    #
    # # resize image
    # resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # resize = cv2.imwrite("image.jpg",resized)
    ######
    image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))
    image = image.reshape(784, 1)
    image = image / 255.
    return image

def callpredict():
    mod = model.predict(callpre())

    return mod

# # call()
def view(X_test):
    X_test = X_test.reshape(28, 28)
    plt.imshow(X_test)
    plt.show()
call()

###################################################################

# X_test = cv2.imread("test_digit.jpg", cv2.IMREAD_GRAYSCALE)
# view(X_test)
# X_test = X_test.reshape(784, 1)
# X_test = X_test / 255.
#
# model.predict(X_test)

#TO TEST THE MODEL
# image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
# image = image.reshape(784, 1)
#model.predict(image)
