import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.ensemble import AdaBoostRegressor
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\user\OneDrive\Рабочий стол\new\12.xlsx')

X = df[['City', 'Place_type']]  # Признаки: Название города и тип места
y = df['Number of households']  # Целевая переменная: Количество домохозяйств

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


svm_model = SVR()
svm_model.fit(X_train, y_train)

svm_accuracy = svm_model.score(X_test, y_test)
print(f"Точность модели SVR: {svm_accuracy}")


adaboost_model = AdaBoostRegressor()
adaboost_model.fit(X_train, y_train)


adaboost_accuracy = adaboost_model.score(X_test, y_test)
print(f"Точность модели AdaBoost: {adaboost_accuracy}")

plt.figure(figsize=(10, 5))


plt.subplot(1, 2, 1)
plt.scatter(y_test, svm_model.predict(X_test))
plt.xlabel('Реальные значения')
plt.ylabel('Предсказанные значения')
plt.title('SVR')


plt.subplot(1, 2, 2)
plt.scatter(y_test, adaboost_model.predict(X_test))
plt.xlabel('Реальные значения')
plt.ylabel('Предсказанные значения')
plt.title('AdaBoost')

plt.tight_layout()
plt.show()
