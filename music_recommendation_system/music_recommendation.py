import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import tkinter as tk
from tkinter import ttk
import numpy as np


def recommend_songs():
    # Veri setini okuma
    data = pd.read_csv("top10s.csv", encoding='ISO-8859-1')

    # Veri setini temizleme ve düzenleme
    data.drop("dB", axis=1, inplace=True)  # dB sütunu silindi
    data.drop("dur", axis=1, inplace=True)  # dur sütunu silindi

    le = LabelEncoder()

    data['title'] = le.fit_transform(data['title'])  # Kategorik değişkenler numeric değerlere dönüştürüldü ve sözlüğe kaydedildi
    title_encoding = dict(zip(le.transform(le.classes_), le.classes_))

    data['artist'] = le.fit_transform(data['artist'])  # Kategorik değişkenler numeric değerlere dönüştürüldü ve sözlüğe kaydedildi
    artist_encoding = dict(zip(le.transform(le.classes_), le.classes_))

    data['top genre'] = le.fit_transform(data['top genre'])  # Kategorik değişkenler numeric değerlere dönüştürüldü ve sözlüğe kaydedildi
    top_genre_encoding = dict(zip(le.transform(le.classes_), le.classes_))

    from sklearn.model_selection import train_test_split

    X = data.drop("pop", axis=1)  # Hedef değişkeni 'pop' hariç tutuldu
    y = data["pop"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    def show_recommendations():
        # Seçilen şarkılar alındı
        song1 = song1_entry.get()
        song2 = song2_entry.get()
        song3 = song3_entry.get()

        # Öneri işlemleri
        input_data = []

        # Seçilen şarkıların sözlükteki karşılıkları kontrol ediliyor
        song1_encoded = list(title_encoding.keys())[list(title_encoding.values()).index(song1)]
        song2_encoded = list(title_encoding.keys())[list(title_encoding.values()).index(song2)]
        song3_encoded = list(title_encoding.keys())[list(title_encoding.values()).index(song3)]

        # Şarkıları X_test yerine doğrudan X'den aldık
        song1_data = X.loc[X.index[song1_encoded]][:12]
        song2_data = X.loc[X.index[song2_encoded]][:12]
        song3_data = X.loc[X.index[song3_encoded]][:12]

        input_data.append(song1_data)
        input_data.append(song2_data)
        input_data.append(song3_data)

        input_data = np.array(input_data)  # input_data'yı bir numpy array'ine dönüştürdük

        predicted_popularity = model.predict(input_data)

        # Tahmin edilen popülerlik değerine dayalı olarak en yakın şarkıları bulma
        y_pred_all = model.predict(X)  # Tüm tahminleri aldık
        diff = np.abs(y_pred_all - predicted_popularity[0])  # predicted_popularity'yi bir sayı olarak aldık

        closest_indices = diff.argsort()[:3]  # En küçük farka sahip olan üç şarkının dizinlerini aldık

        # Önerilen şarkıları bulma
        recommended_songs = []
        for index in closest_indices:
            recommended_songs.append((data.loc[X.index[index], "title"], data.loc[X.index[index], "artist"]))

        recommended_song_list = []
        for song in recommended_songs:
            song_title = title_encoding.get(song[0], "Unknown Title")
            song_artist = artist_encoding.get(song[1], "Unknown Artist")
            recommended_song_list.append("{} by {}".format(song_title, song_artist))

        # Önerilen şarkıları yazdırma
        recommended_songs_label.config(text="Önerilen Şarkılar:\n{}".format("\n".join(recommended_song_list)))

        # Input kutucuklarını öneriden sonra temizledik
        song1_entry.set('')
        song2_entry.set('')
        song3_entry.set('')

    # Arayüz penceresi oluşturma
    window = tk.Tk()
    window.title("Şarkı Öneri Sistemi")
    window.geometry("400x400")

    # Başlık etiketi
    title_label = tk.Label(window, text="Şarkı Öneri Sistemi", font=("Arial", 16))
    title_label.pack(pady=20)

    # Şarkı isimlerini aldık
    song_names = list(title_encoding.values())

    # Şarkı giriş alanları
    song1_entry = ttk.Combobox(window, values=song_names, width=40)
    song1_entry.pack(pady=10)
    song2_entry = ttk.Combobox(window, values=song_names, width=40)
    song2_entry.pack(pady=10)
    song3_entry = ttk.Combobox(window, values=song_names, width=40)
    song3_entry.pack(pady=10)

    # Şarkı öneri düğmesi
    recommend_button = tk.Button(window, text="Şarkıları Öner", command=show_recommendations)
    recommend_button.pack(pady=10)

    # Önerilen şarkılar etiketi
    recommended_songs_label = tk.Label(window, text="Önerilen Şarkılar:")
    recommended_songs_label.pack(pady=20)

    # Arayüzü çalıştırma
    window.mainloop()

# Şarkı öneri arayüzünü başlatma
recommend_songs()