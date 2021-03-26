# Linear_Regression

Predict the price of a car from its milage, using gradient descent coded from scratch.

#### Final Score 125/100

## Getting Started

First clone this repo.

```git clone https://github.com/anyashuka/Linear_Regression.git; cd Linear_Regression```

Download dependencies.

```pip install -r requirements.txt```

Then run run.sh to train a model and predict the price of a car.

```./run.sh```

<img src="https://github.com/anyashuka/Linear_Regression/blob/master/img/run.png" width="500">


## Train

train.py uses gradient descent to train a model using data.csv, 25 cars price and milage.

Below we see the linear function fit to the data over training iterations.

```python3 train.py```

![Example](https://github.com/anyashuka/Linear_Regression/blob/master/img/train.gif)

The loss function is mean squared error.

<img src="https://github.com/anyashuka/Linear_Regression/blob/master/img/error.png" width="610">

The model is saved to Theta.csv. Let's take a look at it's contents.

<img src="https://github.com/anyashuka/Linear_Regression/blob/master/img/theta.png" width="450">

### Flags

#### -a, --alpha

Set learning rate (alpha). Default 0.01.

#### -n, --num_iterations

Set number of training iterations. Default 1500.


## Predict

predict.py loads the model from Theta.csv, prompts user for milage, then prints the predicted price for a car of given milage.

```python3 predict.py```

<img src="https://github.com/anyashuka/Linear_Regression/blob/master/img/predict.png" width="500">


## Dependencies

Thankfully, running the following command should take care of dependencies for you.

```pip install -r requirements.txt```

Python 3.9.1

* matplotlib
* pandas
* numpy
<br />

I wrote this project in a team with the awesome [@dfinnis](https://github.com/dfinnis).
