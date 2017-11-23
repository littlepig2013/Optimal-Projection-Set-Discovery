import numpy as np
import math

def  gram_schmidt_orth(projectionMatrix):
    dimension = projectionMatrix.shape[0]
    orthProjectionMatrix = [projectionMatrix[0]/np.linalg.norm(projectionMatrix[0])]

    for i in range(1, dimension):
        # Orthogonalize
        offsetVector = 0
        for existedVector in orthProjectionMatrix:
            offsetVector += projectionMatrix[i].dot(existedVector)*existedVector
        vector = projectionMatrix[i] - offsetVector
        # Normalize
        if vector.any() != 0:
            orthProjectionMatrix.append(vector/np.linalg.norm(vector))
        else:
            orthProjectionMatrix.append(vector)

    return np.array(orthProjectionMatrix)


def projection_matrix_combination(currProjectionMatrixList, dimension):
    # Generate [0 .. 0 1] (length: dimension+1)
    initVector = np.array([np.zeros(dimension + 1)])
    initVector[0][dimension] = 1
    A_ = initVector.copy()

    # Concatenate projection matrix with the init vector
    zerosVector = np.array([[0, 0]])
    for projectionMatrix in currProjectionMatrixList:
        tempProjectionMatrix = np.concatenate((projectionMatrix, zerosVector.copy().T), axis=1)
        A_ = np.concatenate((tempProjectionMatrix, A_))

    return A_


def get_initial_projection(dimension, noise):
    indexes = range(dimension)
    noiseSqrt = math.sqrt(noise)
    # Generate no-noise initial projection
    A0 = np.zeros((2, dimension))
    alpha = 2*math.pi/dimension
    b = math.sqrt(2/dimension)
    for i in indexes:
        A0[0][i] = b*math.sin(i*alpha)
        A0[1][i] = b*math.cos(i*alpha)

    # Noise added: randomly choose vectors and make them have a p2-norm of l each
    chosenRecordNum = np.random.randint(0, dimension/3)
    chosenIndexes = np.random.choice(indexes, chosenRecordNum, replace=False)
    for index in chosenIndexes:
        # X coordinate
        x = np.random.random()
        # randomly set whether it is negative or positive
        if np.random.random() < 0.5:
            x = -x
        A0[0][index] += x*noiseSqrt

        # Y coordinate
        y = math.sqrt(1 - x*x)
        # randomly set whether it is negative or positive
        if np.random.random() < 0.5:
            y = -y
        A0[1][index] += y*noiseSqrt

    return gram_schmidt_orth(A0)


def optimal_projections_discovery(dataset, noise=0.2, stepSize=1.0, convergence=0.1):
    # Load data
    dataFileName = "dataset/" + dataset + ".txt"
    data = np.loadtxt(dataFileName)
    records, dimension = data.shape

    # Generate some matrixes for further calculation
    data_ = np.concatenate((data.T, np.array([np.ones(records)])))
    D_ = data_.dot(data_.T)
    I_ = np.eye(dimension+1)
    A0 = get_initial_projection(dimension, noise)
    B = A0.copy()
    currProjectionMatrixList = []
    previousGradientNorm = float('inf')

    while True:

        A_ = projection_matrix_combination(currProjectionMatrixList, dimension)
        H_ = (I_ - D_.dot(A_.T).dot(np.linalg.pinv(A_.dot(D_).dot(A_.T))).dot(A_)).dot(data_)
        B = A0.copy()
        B_ = projection_matrix_combination([B], dimension)

        initGradientNorm = np.linalg.norm(B_.dot(H_).dot(H_.T))
        print(initGradientNorm)
        if previousGradientNorm < initGradientNorm or initGradientNorm < 1e-06:
            break
        previousGradientNorm = initGradientNorm

        # Gradient ascent starts
        while True:
            gradientMatrix = 2/records*(B_.dot(H_).dot(H_.T))
            stepMatrix = stepSize*gradientMatrix[0:2, 0:-1]
            BNext = gram_schmidt_orth(B + stepMatrix)
            if (np.linalg.norm(BNext - B))**2 < convergence:
                break
            else:
                B = BNext
                B_ = projection_matrix_combination([B], dimension)


        currProjectionMatrixList.append(B)

    currProjectionMatrixList.insert(0, A0)
    # Generate optimal projections
    projectionList = []
    for projectionMatrix in currProjectionMatrixList:
        projection = data.dot(projectionMatrix.T)
        projectionList.append(projection)

    return projectionList
