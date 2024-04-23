
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import pandas as pd
from keras.models import load_model
import joblib

do_train = True

print('before')
data_frame = pd.read_csv('avalonscores.csv')
#print(data_frame)


X = data_frame.drop('score', axis=1)  # Features
y = data_frame['score']  # Target variable
# print(data_frame.loc[10:20])
# print(y.shape)



#y = to_categorical(y)
#print(y)#.shape)
# #exit()
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
#print("X", X.shape)
#print("x_train", x_train)
#
# print(x_test.shape, x_train.shape, y_test.shape, y_train.shape)

if do_train:
    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(x_train)
    # Save the scaler object to a file
    joblib.dump(scalar, 'scaler.save')
else:
    scalar = joblib.load('scaler.save')
    X_train_scaled = scalar.transform(x_train)
X_test_scaled = scalar.transform(x_test)

print(X_train_scaled)

if do_train:
    model = Sequential([
        Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        Dense(40, activation='relu'),
        #Dense(16, activation='relu'),
        Dense(1,activation='linear')  # Output layer for a single continuous output
       ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='mean_squared_error')


    # Train the model
    #model.fit(X_train_scaled, y_train, epochs=100, validation_split=0.2)
    model.fit(X_train_scaled, y_train, epochs=30, validation_split=0.2)

    #save the module
    model.save('avalon_model.h5')
    print('########################## model was saved ############################')
    # Evaluate the model on the test set
    test_loss = model.evaluate(X_test_scaled, y_test)
    print(f'Test Loss: {test_loss}')

else:
    # Load the model back from the disk
    model = load_model('avalon_model.h5')
#print('-----------------------------------')
#print(x_test[:5])
#print('-----------------------------------')
#print(y_test[:5])
#print('-----------------------------------')
#print(x_test[:1].to_numpy())

# Predpict new values (using X_test_scaled as an example)
predictions = model.predict(X_test_scaled)
print(predictions[:5])  # Print the first 5 predictions
#predictions1 = model.predict(scalar.transform(x_test[:1]))
#print(predictions1)
#test1 = x_test[:1].to_numpy()
#print(test1)
#predictions2 = model.predict(scalar.transform(test1))
#print(predictions2)

# model.compile(
#       optimizer='Adam',
#       loss= 'categorical_crossentropy',
#       metrics=['accuracy']
#    )
# print(y, y.shape)
#
# history = model.fit(
#       x=x_train,
#       y=y_train,
#       epochs=100,
#       shuffle=True
#    )
#
#
#
# score = model.evaluate(x_test, y_test, verbose = 0)
# score_train = model.evaluate(x_train, y_train, verbose = 0)
#
# print('Test loss:', score[0])
# print('Test accuracy:', score[1])
#
# answer = model.predict(np.array([1,0,2,0,1,2,0,0,1]).reshape(-1, 1).T)
# print("[1,0,2,0,1,2,0,0,1]",answer)
#
# print(history.history.keys())
# acc=history.history['accuracy']
# print("accuracy - train",score_train[1])
#
# loss=history.history['loss']
# #val_loss=history.history['val_loss']
#
# epochs=range(1,len(acc)+1)
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.plot(epochs, acc, 'bo', label='Training acc')
#
# plt.title('Training  accuracy')
# plt.legend()
#
#
#
# plt.show()
#
# # save and load model
# model.save('saved model.keras')
# model1 = keras.models.load_model('saved model.keras')
#
# answer1 = model1.predict(np.array([1,0,2,0,1,2,0,0,1]).reshape(-1, 1).T)
# print("[1,0,2,0,1,2,0,0,1] from saved  model",answer1)
