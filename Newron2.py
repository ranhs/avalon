from keras.models import load_model

from sklearn.preprocessing import StandardScaler
import joblib

model = load_model('avalon_model.h5')

test_board1 = [0,2,0,0,0,2,0,1,0,0,1,0,1,0,1,2,1,0,0,2,2,0,1,1,2,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,1,0,1,2,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,1,1]
test_board2 = [2,0,1,2,0,2,1,2,0,0,1,0,0,1,0,0,0,1,2,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,2,2,0,0,0,0,0,0,1,0,0,0,2,1,2,2,0,1,2,1,0,2,2,0,2,2]
scaler = joblib.load('scaler.save')
test_board_scaled = scaler.transform([test_board1,test_board2])


print(test_board_scaled)
predictions = model.predict(test_board_scaled)
#predictions = model.predict([[-0.69931498, -0.71389519, -0.72565311, -0.75492424, -0.75962935,  0.49405086,
#  -0.72902886,  0.58020038, -0.753408,   -0.76942196, -0.75911814,  0.41614001,
#   0.43550201, -0.75202432,  0.56549524, -0.76528269,  0.69438611,  0.75405552,
#   0.33726705,  1.51432631,  1.58388744, -0.76677633,  1.86869508,  0.63324412,
#  -0.7678604 ,  2.24780701,  1.40708321, -0.80733638, -0.79823067, -0.78223192,
# 0.47414231, -0.77106255,  2.02445828,  0.6737544 , -0.76072497, -0.80300795,
#  -0.80467373,  1.45940544,  0.38917198, -0.77268743, -0.7542827 , -0.74824067,
#  -0.75442375,  1.39456367, -0.80391921, -0.79379561, -0.76773178, -0.74691928,
#   1.89855642, -0.71957306, -0.79439068, -0.79908257, -0.77599466, -0.74804162,
#   1.79125136,  1.9478549 , -0.78535289, -0.78453342,  0.41003509, -0.72430983,
#   1.85106885, -0.99959639]])
print(predictions)
