# Algorithms: Naive Bayes Classifier

[![Updates](https://pyup.io/repos/github/charlesgreen/naive_bayes_classifier/shield.svg)](https://pyup.io/repos/github/charlesgreen/naive_bayes_classifier/)
[![Python 3](https://pyup.io/repos/github/charlesgreen/naive_bayes_classifier/python-3-shield.svg)](https://pyup.io/repos/github/charlesgreen/naive_bayes_classifier/)


The purpose of this repository is to implement the great work done in the [Naive Bayes Tutorial for Machine Learning](https://machinelearningmastery.com/naive-bayes-tutorial-for-machine-learning/) by Jason Brownlee.
My goal with this repository is simply to practice and learn the topic more by implementing it in Python and sklearn.

## Overview

For an in-depth overview please read the tutorial. Assuming you've done that I'll keep this short.

To summarize, the tutorial demonstrates how to use the Naive Bayes classification algorithm to predict if someone will stay home or go out depending on two independent variables (weather, car status).

## Deviation from the Tutorial

Instead of using Naive Bayes the code uses the sklearn implementation of Gaussian Naive Bayes (Normal distribution).

## Setup (via conda or pip):

```ruby
# conda setup

# install anaconda
https://docs.continuum.io/anaconda/install

# list environments
$ conda env list

# create environment
$ conda create --name naive_bayes -y python=3

# install dependencies
conda env update -n naive_bayes --file requirements.txt

# active envionment
$ source activate naive_bayes

# deactivate environment
$ source deactivate

# remove envionrment
conda remove -n naive_bayes --all -y

```

```ruby

# pip setup

# install dependencies
$ pip install -r requirements.txt

# install
$ python setup.py install

```

### Usage
```ruby
$ python ./naive_bayes_classifier/gaussian_n_b.py
```


### Tutorial Dataset

```text
Weather	Car	Class
sunny	working	 go-out
rainy	broken	 go-out
sunny	working	 go-out
sunny	working	 go-out
sunny	working	 go-out
rainy	broken	 stay-home
rainy	broken	 stay-home
sunny	working	 stay-home
sunny	broken	 stay-home
rainy	broken	 stay-home

```

### Data Preparation
- The source dataset must be converted to numeric values using a technique "[one-hot](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/)" encoding.

```text
Variable: Weather
- sunny = 1
- rainy = 0

Variable: Car
- working = 1
- broken  = 0

Variable: Class
- go-out = 1
- stay-home = 0


Weather	Car	Class
1	1	1
0	0	1
1	1	1
1	1	1
1	1	1
0	0	0
0	0	0
1	1	0
1	0	0
0	0	0

```

### Calculations

#### Calculate Class Probabilities
```text
P(class=1) = count(class=1) / (count(class=0) + count(class=1))
P(class=0) = count(class=0) / (count(class=0) + count(class=1))

P(class=1) = 5 / (5 + 5)
P(class=0) = 5 / (5 + 5)
```

#### Calculate Conditional Probabilities
```text
# Weather Input Variable
P(weather=sunny|class=go-out) = count(weather=sunny and class=go-out) / count(class=go-out)
P(weather=rainy|class=go-out) = count(weather=rainy and class=go-out) / count(class=go-out)
P(weather=sunny|class=stay-home) = count(weather=sunny and class=stay-home) / count(class=stay-home)
P(weather=rainy|class=stay-home) = count(weather=rainy and class=stay-home) / count(class=stay-home)

P(weather=sunny|class=go-out) = 0.8
P(weather=rainy|class=go-out) = 0.2
P(weather=sunny|class=stay-home) = 0.4
P(weather=rainy|class=stay-home) = 0.6


# Car Input Variable
P(car=working|class=go-out) = count(car=working and class=go-out) / count(class=go-out)
P(car=broken|class=go-out) = count(car=brokenrainy and class=go-out) / count(class=go-out)
P(car=working|class=stay-home) = count(car=working and class=stay-home) / count(class=stay-home)
P(car=broken|class=stay-home) = count(car=brokenrainy and class=stay-home) / count(class=stay-home)

P(car=working|class=go-out) = 0.8
P(car=broken|class=go-out) = 0.2
P(car=working|class=stay-home) = 0.2
P(car=broken|class=stay-home) = 0.8
```


### Make Predictions with Naive Bayes
```text
P(h|d) = (P(d|h) * P(h)) / P(d)

Where:
P(h|d) is the probability of hypothesis h given the data d (posterior probability).
P(d|h) is the probability of data d given that the hypothesis h was true.
P(h) is the probability of hypothesis h being true (regardless of the data, prior probability of h)
P(d) is the probability of the data (regardless of the hypothesis).

# only numerator and the class is needed
MAP(h) = max(P(d|h) * P(h))
```

Example 1: `weather=sunny, car=working`
```text
go-out = P(weather=sunny|class=go-out) * P(car=working|class=go-out) * P(class=go-out)
go-out = 0.8 * 0.8 * 0.5
go-out = 0.32
```

#### Full Dataset Prediction
```text
Weather	Car	Class		out?	home?	Prediction
sunny	working	go-out		0.32	0.04	go-out
rainy	broken	go-out		0.02	0.24	stay-home
sunny	working	go-out		0.32	0.04	go-out
sunny	working	go-out		0.32	0.04	go-out
sunny	working	go-out		0.32	0.04	go-out
rainy	broken	stay-home	0.02	0.24	stay-home
rainy	broken	stay-home	0.02	0.24	stay-home
sunny	working	stay-home	0.32	0.04	go-out
sunny	broken	stay-home	0.08	0.16	stay-home
rainy	broken	stay-home	0.02	0.24	stay-home

# Accuracy of 80%
```

References:
- [Naive Bayes Tutorial for Machine Learning](https://machinelearningmastery.com/naive-bayes-tutorial-for-machine-learning/)
- [Naive Bayes, Gaussian Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html)
