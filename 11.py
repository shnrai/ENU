import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Загрузка данных
file_path = r'C:/Users/user/OneDrive/Рабочий стол/жукабаева/breast-cancer.csv'
data = pd.read_csv(file_path)

# Выбор признаков
selected_features = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
                      'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave points_mean',
                      'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se',
                      'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se',
                      'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
                      'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
                      'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

selected_data = data[selected_features]

# Определение целевой переменной и признаков
X = selected_data.drop(['id', 'diagnosis'], axis=1)
y = selected_data['diagnosis']

# Разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание моделей
rf = RandomForestClassifier(random_state=42)
gb = GradientBoostingClassifier(random_state=42)
lr = LogisticRegression(max_iter=1000, random_state=42)

# Квазилинейная композиция (VotingClassifier)
ensemble = VotingClassifier(estimators=[('rf', rf), ('gb', gb), ('lr', lr)], voting='soft')

# Обучение моделей
rf.fit(X_train, y_train)
gb.fit(X_train, y_train)
lr.fit(X_train, y_train)
ensemble.fit(X_train, y_train)

# Получение предсказаний
rf_preds = rf.predict(X_test)
gb_preds = gb.predict(X_test)
lr_preds = lr.predict(X_test)
ensemble_preds = ensemble.predict(X_test)

# Создание композиции моделей и оценка точности
rf_preds = rf_preds.astype(float)
gb_preds = gb_preds.astype(float)
lr_preds = lr_preds.astype(float)
ensemble_preds = ensemble_preds.astype(float)

# Оценка точности каждой модели
rf_accuracy = accuracy_score(y_test, rf_preds)
gb_accuracy = accuracy_score(y_test, gb_preds)
lr_accuracy = accuracy_score(y_test, lr_preds)
ensemble_accuracy = accuracy_score(y_test, ensemble_preds)

# Вывод результатов
print(f'Accuracy of Random Forest: {rf_accuracy}')
print(f'Accuracy of Gradient Boosting: {gb_accuracy}')
print(f'Accuracy of Logistic Regression: {lr_accuracy}')
print(f'Accuracy of the Ensemble model: {ensemble_accuracy}')

# Визуализация результатов
models = ['Random Forest', 'Gradient Boosting', 'Logistic Regression', 'Ensemble']
accuracies = [rf_accuracy, gb_accuracy, lr_accuracy, ensemble_accuracy]

plt.figure(figsize=(10, 6))
plt.bar(models, accuracies, color=['blue', 'orange', 'green', 'red'])
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracies')
plt.show()
