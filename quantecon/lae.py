"""
Filename: lae.py

Authors: Thomas J. Sargent, John Stachurski,

Computes a sequence of marginal densities for a continuous state space
Markov chain X_t where the transition probabilities can be represented
as densities. The estimate of the marginal density of X_t is

.. math::

    (1/n) \sum_{i=0}^n p(X_{t-1}^i, y)

This is a density in y.

"""

import numpy as np

class LAE:
    """
    An instance is a representation of a look ahead estimator associated
    with a given stochastic kernel p and a vector of observations X.

    Parameters
    ----------
    p : function
        The stochastic kernel.  A function p(x, y) that is vectorized in
        both x and y
    X : array_like(float)
        A vector containing observations

    Attributes
    ----------
    p : function
        The stochastic kernel.  A function p(x, y) that is vectorized in
        both x and y
    X : array_like(float)
        A vector containing observations

    Example
    -------
    >>> psi = LAE(p, X)
    >>> y = np.linspace(0, 1, 100)
    >>> psi(y)  # Evaluate look ahead estimate at grid of points y

    """

    def __init__(self, p, X):
        X = X.flatten()  # So we know what we're dealing with
        n = len(X)
        self.p, self.X = p, X.reshape((n, 1))


    def __call__(self, y):
        """
        A vectorized function that returns the value of the look ahead
        estimate at the values in the array y.

        Parameters
        ----------
        y : array_like(float)
            A vector of points at which we wish to evaluate the look-
            ahead estimator

        Returns
        -------
        psi_vals : array_like(float)
            The values of the density estimate at the points in y

        """
        k = len(y)
        v = self.p(self.X, y.reshape((1, k)))
        psi_vals = np.mean(v, axis=0)    # Take mean along each row

        return psi_vals.flatten()


