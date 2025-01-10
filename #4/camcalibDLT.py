import numpy as np


def camcalibDLT(x_world, x_im):
    """
    :param x_world: World coordinatesm with shape (point_id, coordinates)
    :param x_im: Image coordinates with shape (point_id, coordinates)
    :return P: Camera projection matrix with shape (3,4)
    """
    # Create the matrix A 
    ##-your-code-starts-here-##
    h = x_world.shape[0]
    print("h", h)
    w = x_world.shape[1]
    print("w", w)
    x = x_im[:, 0]
    y = x_im[:, 1]
    A = np.zeros((2 * h, 3 * w))  # that's how the dimension of our matrix is : see in assignment

    for i in range(h):
        temp = x_world[i, :]
        print("temp", temp)
        # hstack()– it performs horizontal stacking along with the columns.
        # equations
        A[2 * i, :] = np.hstack((np.zeros(4), temp, -y[i] * temp))
        A[2 * i + 1, :] = np.hstack((temp, np.zeros(4), -x[i] * temp))

    ##-your-code-ends-here-##

    # Perform homogeneous least squares fitting.
    # The best solution is given by the eigenvector of
    # A.T*A with the smallest eigenvalue.
    ##-your-code-starts-here-##
    temp_1, temp_2 = np.linalg.eig(A.T @ A)
    min_find = np.argmin(temp_1)
    ev = temp_2[:, min_find]
    ##-your-code-ends-here-##

    # Reshape the eigenvector into a projection matrix P
    P = np.reshape(ev, (3, 4))  # here ev is the eigenvector from above
    # P = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], dtype=float)  # remove this and uncomment the line above

    return P
