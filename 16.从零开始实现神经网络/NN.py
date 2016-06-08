# coding=utf_8
__author__ = "http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/"

"""why implement a Neural Network from scratch at all? Even if you plan on using Neural Network libraries like
PyBrain in the future, implementing a network from scratch at least once is an extremely valuable exercise.
It helps you gain an understanding of how neural networks work, and that is essential for designing effective models."""

import matplotlib.pyplot as plt
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.linear_model
import matplotlib

# Gradient descent parameters (I picked these by hand)
epsilon = 0.01  # learning rate for gradient descent
reg_lambda = 0.01  # regularization strength

# Helper function to plot a decision boundary.
# If you don't fully understand this function don't worry, it just generates the contour plot below.
def plot_decision_boundary(pred_func):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)

# Helper function to evaluate the total loss on the dataset
def calculate_loss(model):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    # Forward propagation to calculate our predictions
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    # Calculating the loss
    corect_logprobs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(corect_logprobs)
    # Add regularization term to loss (optional)
    data_loss += reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
    return 1./num_examples * data_loss

# Helper function to predict an output (0 or 1)
def predict(model, x):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    # Forward propagation
    z1 = x.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return np.argmax(probs, axis=1)

# This function learns parameters for the neural network and returns the model.
# - nn_hdim: Number of nodes in the hidden layer
# - num_passes: Number of passes through the training data for gradient descent
# - print_loss: If True, print the loss every 1000 iterations
def build_model(nn_hdim, num_passes=20000, print_loss=False):

    # Initialize the parameters to random values. We need to learn these.
    np.random.seed(0)
    W1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
    b1 = np.zeros((1, nn_hdim))
    W2 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)
    b2 = np.zeros((1, nn_output_dim))

    # This is what we return at the end
    model = {}

    # Gradient descent. For each batch...
    for i in range(0, num_passes):

        # Forward propagation
        z1 = X.dot(W1) + b1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

        # Backpropagation
        delta3 = probs
        delta3[range(num_examples), y] -= 1
        dW2 = (a1.T).dot(delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)
        delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))
        dW1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)

        # Add regularization terms (b1 and b2 don't have regularization terms)
        dW2 += reg_lambda * W2
        dW1 += reg_lambda * W1

        # Gradient descent parameter update
        W1 += -epsilon * dW1
        b1 += -epsilon * db1
        W2 += -epsilon * dW2
        b2 += -epsilon * db2

        # Assign new parameters to the model
        model = { 'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}

        # Optionally print the loss.
        # This is expensive because it uses the whole dataset, so we don't want to do it too often.
        if print_loss and i % 1000 == 0:
          print("Loss after iteration %i: %f" % (i, calculate_loss(model)))

    return model

if __name__=="__main__":

    # Display plots inline and change default figure size
    matplotlib.rcParams['figure.figsize'] = (10.0, 8.0)

    #  Generating a dataset
    #  Let’s start by generating a dataset we can play with. Fortunately, scikit-learn has some useful
    #  dataset generators.so we don’t need to write the code ourselves. We will go with the make_moons function.

    # Generate a dataset and plot it
    np.random.seed(0)
    X, y = sklearn.datasets.make_moons(200, noise=0.20)
    # print("X:",X)
    # print("y:",y)
    plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)
    # plt.show()

    #  one of the major advantages of Neural Networks.  You don't need to worry about feature engineering.
    #  The hidden layer of a neural network will learn features for you.

    #  Logistic Regression
    #  To demonstrate the point let's train a Logistic Regression classifier.
    #  Its input will be the x- and y-values and the output the predicted class (0 or 1).
    #  To make our life easy we use the Logistic Regression class from scikit-learn.

    # Train the logistic regression classifier
    clf = sklearn.linear_model.LogisticRegressionCV()
    clf.fit(X, y)

    # Plot the decision boundary
    plot_decision_boundary(lambda x: clf.predict(x))
    plt.title("Logistic Regression")
    # plt.show()

    # The graph shows the decision boundary learned by our Logistic Regression classifier.It separates the data
    # as good as it can using a straight line,but it's unable to capture the "moon shape" of our data.

    # 建立一个三层神经网络，一个输入层，一个隐藏层，一个输出层 输入层的节点数由输入数据的维数决定，（这里是2），
    # 输出层的节点数由待分类的类别个数决定，这里也是2.（由于我们只有两类，所以我们可以只需要一个输出节点通过预测0或1来分类，
    # 但是 有2个节点便于我们将网络扩展到多分类的情况。）网络的输入是x和y坐标，输出分别是类0和类1的概率
    # 我们可以选择隐藏层的维数（结点个数）结点个数越多，我们需要拟合的函数越复杂，预测需要的计算越多，需要学习的网络参数越多
    # 也就更容易过拟合。选择合适的隐藏层节点数与其说是一项技术倒不如说是一项艺术。稍后我们会实验隐藏层的结点个数对输出结果的
    # 影响。

    # 我们也需要为隐藏层选择一个激活函数，激活函数将输入转换为输出，非线性激活函数允许我们拟合非线性假设，常规激活函数的选择
    # 是 tanh()、sigmod()和ReLUs().本次使用tanh()函数。这些函数有一个漂亮的特性就是他们的导数可以通过原函数计算出来。
    # 这个特性很重要，它允许我们计算原函数一次，然后在计算导数的时候重用它。
    #  Because we want our network to output probabilities the activation function for the output layer
    #  will be the softmax,which is simply a way to convert raw scores to probabilities. If you’re familiar with
    # the logistic function you can think of softmax as its generalization to multiple classes.

    # Some useful variables and parameters for gradient descent:
    num_examples = len(X)  # training set size
    nn_input_dim = 2  # input layer dimensionality
    nn_output_dim = 2  # output layer dimensionality

    # Build a model with a 3-dimensional hidden layer
    model = build_model(3, print_loss=True)

    # Plot the decision boundary
    plot_decision_boundary(lambda x: predict(model, x))
    plt.title("Decision Boundary for hidden layer size 3")

    # In the example above we picked a hidden layer size of 3. Let’s now get a sense of
    # how varying the hidden layer size affects the result.
    plt.figure(figsize=(16, 32))
    hidden_layer_dimensions = [1, 2, 3, 4, 5, 10]
    for i, nn_hdim in enumerate(hidden_layer_dimensions):
        plt.subplot(5, 2, i+1)
        plt.title('Hidden Layer size %d' % nn_hdim)
        model = build_model(nn_hdim)
        plot_decision_boundary(lambda x: predict(model, x))
    plt.show()