import numpy as np


def estimateF(x1, x2):
    """
    :param x1: Points from image 1, with shape (coordinates, point_id)
    :param x2: Points from image 2, with shape (coordinates, point_id)
    :return F: Estimated fundamental matrix
    """

    # Use x1 and x2 to construct the equation for homogeneous linear system
    ##-your-code-starts-here-##
    # find u, v, u', v'
    u1 = x1[0, :]
    u2 = x2[0, :]
    v1 = x1[1, :]
    v2 = x2[1, :]
    temp = np.ones((11, 9))

    #  use this (u′u, u′v, u′, v′u, v′v, v′, u, v, 1) where v = v1 and v' = v2
    temp[:, 0] = u2 * u1
    temp[:, 1] = u2 * v1
    temp[:, 2] = u2
    temp[:, 3] = v2 * u1
    temp[:, 4] = v2 * v1
    temp[:, 5] = v2
    temp[:, 6] = u1
    temp[:, 7] = v1
    temp[:, 8] = 1

    ##-your-code-ends-here-##

    # Use SVD to find the solution for this homogeneous linear system by
    # extracting the row from V corresponding to the smallest singular value.
    ##-your-code-starts-here-##
    u, s, vh = np.linalg.svd(temp)
    index = np.argmin(s)
    v_min = vh[index, :]

    ##-your-code-ends-here-##
    F = np.reshape(v_min, (3, 3))  # reshape to acquire Fundamental matrix F
    # F = np.ones((3, 3))  # remove me and uncomment the above

    # Enforce constraint that fundamental matrix has rank 2 by performing
    # SVD and then reconstructing with only the two largest singular values
    # Reconstruction is done with u @ s @ vh where s is the singular values
    # in a diagonal form.
    ##-your-code-starts-here-##
    u, s, vh = np.linalg.svd(F)
    index = np.argmin(s)
    s[index] = 0
    s = np.diag(s)
    F = u @ s @ vh

    ##-your-code-ends-here-##

    return F
