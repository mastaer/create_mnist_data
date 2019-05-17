import tensorflow as tf
import os


# Create Data-Dir in parent folder
current_path =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(current_path+'/data'):
    os.mkdir(current_path+'/data')
    
# download the dataset
# here you can also manipulate (preprocess) the data, so that you can work with it
tf.keras.datasets.mnist.load_data(path=current_path + '/data/mnist1.npz')
tf.keras.datasets.mnist.load_data(path=current_path + '/data/mnist2.npz')
tf.keras.datasets.mnist.load_data(path=current_path + '/data/mnist3.npz')

# Write to gitignore to ignore the data folder in the parent folder.
f= open(os.path.join(current_path, '.gitignore'),"a+")
f.write('\ndata')
f.close()
