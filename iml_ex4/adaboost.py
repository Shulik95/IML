"""
===================================================
     Introduction to Machine Learning (67577)
===================================================

Skeleton for the AdaBoost classifier.

"""
import numpy as np


class AdaBoost(object):

    def __init__(self, WL, T):
        """
        Parameters
        ----------
        WL : the class of the base weak learner
        T : the number of base learners to learn
        """
        self.WL = WL
        self.T = T
        self.h = [None] * T  # list of base learners
        self.w = np.zeros(T)  # weights

    def train(self, X, y):
        """
        Parameters
        ----------
        X : samples, shape=(num_samples, num_features)
        y : labels, shape=(num_samples)
        Train this classifier over the sample (X,y)
        After finish the training return the weights of the samples in the last iteration.
        """

        D = np.ones(y.shape) / y.shape[0]  # init parameters
        for i in range(0, self.T):
            self.h[i] = self.WL(D, X, y)  # construct a weak learner
            y_hat = (self.h[i]).predict(X)
            err_t = np.sum(D[y != y_hat])
            self.w[i] = 0.5 * np.log((1/err_t) - 1)
            D = np.multiply(D, np.exp(-y * self.w[i]*self.h[i]))  # update sample weights
            D = D / np.sum(D)
        return D


    def predict(self, X, max_t):
        """
        Parameters
        ----------
        X : samples, shape=(num_samples, num_features)
        :param max_t: integer < self.T: the number of classifiers to use for the classification
        :return: y_hat : a prediction vector for X. shape=(num_samples)
        Predict only with max_t weak learners,
        """

        predictions = [self.w[i] * self.h[i].predict(X) for i in range(max_t)]
        return np.sign(np.sum(predictions))

    def error(self, X, y, max_t):
        """
        Parameters
        ----------
        X : samples, shape=(num_samples, num_features)
        y : labels, shape=(num_samples)
        :param max_t: integer < self.T: the number of classifiers to use for the classification
        :return: error : the ratio of the wrong predictions when predict only with max_t weak learners (float)
        """
        # TODO complete this function
