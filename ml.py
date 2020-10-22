import sklearn

vectorSize = 10

def getVectorByIndex(history, index):
    vector = []
    for i, row in history.iloc[index - vectorSize:index - 1].iterrows():
        vector.append(row.Close)

    return vector, history.iloc[index].Open

def getLearningData(history, minIndex, maxIndex):
    X = []
    y = []
    for i in range(minIndex, maxIndex):
        vector, result = getVectorByIndex(history, i)
        X.append(vector)
        y.append(result)

    return X, y

# vector = getVectorByDate(history, '2020-09-29')
# print(vector)


def predict(history, index):
    if index < vectorSize*2:
        return

    model = sklearn.linear_model.LinearRegression()
    model.fit(*getLearningData(history, vectorSize, index-1))

    vector, result = getVectorByIndex(history, index)
    ynew = model.predict([vector])
    print("prev=%s, Predicted=%s, result=%s," % (vector[vectorSize - 2], round(ynew[0], 2), result,))

    return round(ynew[0], 2)

# for i in range(0, 10):
#     print(ml.predict(df, i))
