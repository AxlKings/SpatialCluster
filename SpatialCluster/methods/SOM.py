from minisom import MiniSom  
import numpy as np
from SpatialCluster.utils.get_areas import get_areas
from SpatialCluster.utils.data_format import numpy_data_format, position_data_format

def SOM_Clustering(features_X, features_position, som_shape = (6,6), sigma=0.3, learning_rate=0.5, num_iterations = 100):
    features_X = numpy_data_format(features_X)
    features_position = position_data_format(features_position)
    
    som = MiniSom(som_shape[0], som_shape[1], features_X.shape[1], sigma=sigma, learning_rate=learning_rate) # initialization of SOM
    som.train(features_X, num_iterations)
    winner_coordinates = np.array([som.winner(x) for x in features_X]).T
    # with np.ravel_multi_index we convert the bidimensional
    # coordinates to a monodimensional index
    clusters = np.ravel_multi_index(winner_coordinates, som_shape)
    points = list(zip(features_position.lon, features_position.lat))
    areas_to_points = get_areas(clusters, points)
    return areas_to_points, clusters