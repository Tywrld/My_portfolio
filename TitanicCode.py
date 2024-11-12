







import pandas as pd

trainData = pd.read_csv("train.csv")
testData = pd.read_csv("test.csv")

testData.head(5)

from sklearn.ensemble import RandomForestClassifier

y = trainData["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(trainData[features])
X_test = pd.get_dummies(testData[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X,y)
predictions = predicitions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': testData.PassengerId, 'Survived': predicitions})
output.to_csv("submission.csv", index = False) #this outputs to the submission csv file

output.head(15)







nameList = list(trainData["Name"])
drList = []
for name in nameList:
  if "Dr" in name:
    drList.append(name)
print(drList)
print(len(drList))

