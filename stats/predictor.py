import pandas as pd
import json
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

with open('games2024.json') as games_file:
    games= json.load(games_file)

df1 = pd.DataFrame(columns=['team1', 'team2', 'score1', 'score2', 'em1', 'em2'])
teams = pd.read_csv('kenpom2024.csv')

print(games)
for game in games['data']:
    team1 = game[1]
    team2 = game[6]
    score1 = game[5]
    score2 = game[10]
    t1 = -1
    t2 = -1
    index = 0
    t1em=-1
    t2em=-1
    for team in teams['TeamName']:
        if(team.lower() in team1.lower()):
            t1 = index
        if(team.lower() in team2.lower()):
            t2 = index
        index+=1
    if t1!= -1:
        t1em = teams.loc[[t1]].values[0][14]
    if t2!= -1:
        t2em = teams.loc[[t2]].values[0][14]
    if t1em!=-1 and t2em!=-1:
        df2 = pd.DataFrame([[team1, team2, score1, score2, t1em, t2em]], columns=['team1', 'team2', 'score1', 'score2', 'em1', 'em2'])
        df1 = pd.concat([df1, df2], ignore_index=True)

X = df1[['em1', 'em2']]
x = df1['em1']-df1['em2']
y= df1['score1'] - df1['score2']

# poly = PolynomialFeatures(degree=2)
# X2 = poly.fit_transform(x)
# y2 = poly.fit_transform(y)
# X2 = np.delete(X2,(1),axis=1)
# y2 = np.delete(y2,(1),axis=1)
#
# clf = linear_model.LinearRegression()
# #preform the actual regression
# clf.fit(X2, [20,-10])
#
# print("X2 = ",X2)
# print("predict_ = ",y2)
# print("Prediction = ",clf.predict(y2))



# predictions = poly.predict([[-14, -4]])
# plt.scatter(X, y)
# plt.show()

polynomial_features = PolynomialFeatures(degree=3,
                                         include_bias=False)
linear_regression = LinearRegression()
pipeline = Pipeline([("polynomial_features", polynomial_features),
                     ("linear_regression", linear_regression)])
pipeline.fit(X[:, np.newaxis], y)



X_test = np.linspace(0, 1, 100)

plt.plot(X_test, pipeline.predict(X_test[:, np.newaxis]), label="Model")

plt.show

