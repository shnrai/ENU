import tkinter as tk
import requests
from sklearn.ensemble import RandomForestClassifier
root = tk.Tk()
root.title("Senim Cinema")

def predict_genre():
    keyword = entry.get() 
    params = {"keyword": keyword}
    response = requests.get(url, params=params, headers=headers)
    films_data = response.json()
    if 'films' in films_data and isinstance(films_data['films'], list):
        descriptions = [film.get('description', '') for film in films_data['films']]
        X = [
            [1, 0, 0],  # Мстители: боевик
            [0, 1, 0],  # Гарри Поттер: комедия
            [0, 0, 1],  # Ва банк: экшен
            [0, 0, 1],  # Кухня: экшен
            [0, 1, 0],  # Потомки солнца: комедия
            [0, 0, 1],  # Кровь: экшен
        ]
        y = [0, 1, 2, 1, 1, 2]  # Числовое представление жанров: боевик - 0, комедия - 1, экшен - 2
        random_forest = RandomForestClassifier(n_estimators=100)  
        random_forest.fit(X, y)  

        predicted_genre = random_forest.predict(X)
        result_label.config(text=f"Болжамды жанр: {predicted_genre}")
    else:
        result_label.config(text="API фильмдері туралы қате деректер")

entry = tk.Entry(root)
entry.pack()

predict_button = tk.Button(root, text="Деректер мен жанрды алыңыз", command=predict_genre)
predict_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

api_key = "71c5dd47-2ab2-40d4-bb00-4974097af5b6"
url = "https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword"
headers = {"X-API-KEY": api_key}

root.mainloop()
