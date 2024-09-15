import pandas as pd  
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.preprocessing import StandardScaler  
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split

data = pd.read_csv('WinePredictor.csv')

Y = data.iloc[:, 0]
X = data.iloc[:, 1:]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
test_values = [[13.2, 2.77, 2.51, 20.0, 96.0, 2.85, 2.91, 0.27, 1.44, 4.25, 1.12, 2.51, 550]]
test_values_scaled = scaler.transform(test_values)
prediction = classifier.predict(test_values_scaled)
print(f"Prediction for test values {test_values[0]}: Class {prediction[0]}")

def CheckAccuracy():
    X_train_full, X_test_full, Y_train_full, Y_test_full = train_test_split(X, Y, test_size=0.5, random_state=42)
    accuracies = {}
    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_full, Y_train_full)
        Y_pred_full = knn.predict(X_test_full)
        accuracy = accuracy_score(Y_test_full, Y_pred_full)
        accuracies[k] = accuracy
        print(f"Accuracy with k={k}: {accuracy*100:.2f}%")
    return accuracies

def main():
    accuracies = CheckAccuracy()

if __name__ == "__main__":
    main()
