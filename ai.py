from keras.datasets import imdb 
top_words = 10000 
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=top_words)