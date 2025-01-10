import numpy as np


def trianglin(P1, P2, x1, x2):
    """
    :param P1: Projection matrix for image 1 with shape (3,4)
    :param P2: Projection matrix for image 2 with shape (3,4)
    :param x1: Image coordinates for a point in image 1
    :param x2: Image coordinates for a point in image 2
    :return X: Triangulated world coordinates
    """

    # Form A and get the least squares solution from the eigenvector 
    # corresponding to the smallest eigenvalue
    ##-your-code-starts-here-##

    # calculate [x1×]P1 and [x2×]P2
    # 3x3 matrix
    x1x = np.array([0, -x1[2], x1[1], x1[2], 0, -x1[0], -x1[1], x1[0], 0]).reshape((3, 3))
    x2x = np.array([0, -x2[2], x2[1], x2[2], 0, -x2[0], -x2[1], x2[0], 0]).reshape((3, 3))
    x1xP1 = x1x @ P1  # cross product
    x2xP2 = x2x @ P2  # cross product

    # and stack these vertically to acquire A
    A = np.vstack((x1xP1, x2xP2))

    temp_1, temp_2 = np.linalg.eig(A.T @ A)
    min_find = np.argmin(temp_1)
    ev = temp_2[:, min_find]
    ##-your-code-ends-here-##
    X = ev
    # X = np.array([0, 0, 0, 1])  # remove me

    return X
