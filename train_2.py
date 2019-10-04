import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plot
import statistics as stat

def feature_normalize(X):
    mu = stat.mean(X)
    sigma = stat.stdev(X)
    normalized_features = (X-mu)/sigma if sigma != 0 else X
    return normalized_features

def predict(X, theta):
    return theta[0] + (theta[1] * X)

def cost(X, y, theta):
    m = len(X)
    hypothesis = predict(X, theta)
    J = 1 / (2 * m) * np.sum(np.square(hypothesis - y))
    return (J)

def fit(X, y, theta, alpha, num_iters):
    m = len(X)
    J_history = []
    for i in range(num_iters):
        hypothesis = predict(X, theta)
        theta[0] -= alpha / m * np.sum(hypothesis - y)
        theta[1] -= alpha / m * np.dot((hypothesis - y), np.transpose(X))
        J_history.append(cost(X, y, theta))   
    return theta, J_history

def visualize_regression(theta, X_norm, X, y):
    fig = plot.figure()
    ax = plot.axes()
    
    plot.scatter(X, y, color='blue')

    x_max = np.max(X) + 10000
    x_min = np.min(X) - 10000
    ax.set_xlim([x_min, x_max])
    ax.set_ylim(np.min(y) - 1000, np.max(y) + 1000)
    ax.scatter(X, y, color='blue')
    
    reg_line = theta[0] + X_norm * theta[1]
    ax.plot(X, reg_line, 'r-', X, y, 'o')

    plot.title("Price over Distance Driven")
    plot.xlabel("kilometers")
    plot.ylabel("price")
    plot.show()

<<<<<<< HEAD
def visualize_cost(J_history):
    plot.figure()
    ax = plot.axes()
    plot.title("Error rate")
    plot.xlabel("Number of Iterations")
    plot.ylabel("Mean Squared Error")
    ax.plot(J_history)

=======
>>>>>>> 20af7a0b7e42e288f7d49895b6783e7232c23028
def save_theta(theta):
    if theta[0] == 0.0 and theta[1] == 0.0:
        print("Saving theta aborted as theta is zero")
    else:
        try:
            theta_file = open('Theta', 'w')
            theta_file.write('theta[0] = {}\ntheta[1] = {}' .format(theta[0], theta[1]))
            theta_file.close
        except Exception:
            print("Saving theta failed")


def main():
    data = pd.read_csv("data.csv")
    X = np.array(data['km'], dtype='float64')
    y = np.array(data['price'], dtype='float64')
    X_norm = feature_normalize(X)

    theta = np.array([0, 0], dtype='float64')
    # theta = fit(X_norm, y, theta, 0.01, 1500)
    
    theta = np.zeros(2)
    theta, J_history = fit(X_norm, y, theta, 0.01, 1500)

    visualize_cost(J_history)
    visualize_regression(theta, X_norm, X, y)
    plot.figure()
    ax = plot.axes()
    ax.plot(J_history)

    save_theta(theta)

    visualize(theta, X_norm, X, y)
    

if __name__ == '__main__':
    main()