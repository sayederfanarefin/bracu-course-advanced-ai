import numpy as np
from sklearn.naive_bayes import GaussianNB

default_training_data = np.array([[1, 1],
                                  [0, 0],
                                  [1, 1],
                                  [1, 1],
                                  [1, 1],
                                  [0, 0],
                                  [0, 0],
                                  [1, 1],
                                  [1, 0],
                                  [0, 0]])

default_training_labels = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
default_target = np.array([[0, 0], [1, 1], [1,0]])


class NaiveBayesClassifier:
    """ This class demonstrates the Gaussian Naive Bayes Classifier
        http://scikit-learn.org/stable/modules/naive_bayes.html
    """

    def __init__(self):
        self.y_pred = None
        self.clf = GaussianNB()
        print(default_training_data)

    def print_results(self):
        for item in range(len(self.y_pred)):
            print("Predict: {:d}".format(self.y_pred[item]))

    def fit(self, data=default_training_data, labels=default_training_labels):
        self.clf.fit(data, labels)
        return self

    def predict(self, target=default_target):
        self.y_pred = self.clf.predict(target)
        return self


if __name__ == "__main__":
    tc = NaiveBayesClassifier()
    tc.fit()
    tc.predict()
    tc.print_results()
