import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree
from sklearn.metrics import accuracy_score
data = pd.read_csv(r"/Users/3052307/Downloads/Scripts/week1-example.csv")
X = data.drop(columns=['y'])
y = data['y']
print(X.shape)
print(y.shape)

clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

path = clf.cost_complexity_pruning_path(X, y)
ccp_alphas = path.ccp_alphas

np.random.seed(0)
my_list = [x for x in range(200)]
fold_1 = np.random.choice(my_list, 40, replace=False)
a1 = np.array([x for x in my_list if x not in fold_1])
fold_2 = np.random.choice(a1, 40, replace=False)
a2 = np.array([x for x in a1 if x not in fold_2])
fold_3 = np.random.choice(a2, 40, replace=False)
a3 = np.array([x for x in a2 if x not in fold_3])
fold_4 = np.random.choice(a3, 40, replace=False)
fold_5 = np.array([x for x in a3 if x not in fold_4])

folds = [fold_1, fold_2, fold_3, fold_4, fold_5]
training_lists = [[x for x in my_list if x not in fold_1], [x for x in my_list if x not in fold_2], [x for x in my_list if x not in fold_3], [x for x in my_list if x not in fold_4], [x for x in my_list if x not in fold_5]]
acc_scores = [0]*5

for p in range(0,5):
    training_Y = y[training_lists[p]]
    training_X = X.iloc[training_lists[p]]
    testing_Y = y[folds[p]]
    testing_X = X.iloc[folds[p]]
    clfs = []
    for ccp_alpha in ccp_alphas:
        clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
        clf.fit(training_X, training_Y)
        clfs.append(clf)
    acc_scores[p] = ([accuracy_score(testing_Y, clf.predict(testing_X)) for clf in clfs])

print(acc_scores)

avgaccuracy = [0]*15

for k in range(1,16):
    avgaccuracy[k - 1] = np.mean([acc_scores[p][k - 1] for p in range(0,5)])

print(avgaccuracy)

max_value = max(avgaccuracy)
max_index = avgaccuracy.index(max_value)

print(max_value, max_index)

print(ccp_alphas[11])

# Best Decision Tree

clf_ = DecisionTreeClassifier(random_state=0, ccp_alpha=0.01809090909090909)
clf_.fit(X, y)

tree.plot_tree(clf_)
plt.show()

