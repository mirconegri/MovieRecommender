# 🎬 Movie Recommender

[![PDF Merge](https://img.shields.io/badge/Language-python-blue?style=for-the-badge)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE) 

I needed an application that could **recommend new movies** for me to watch,  
so I created this simple and elegant movie recommendation app built with **Python** and **Tkinter**.  
It suggests top-rated movies based on your selected genre and displays their posters — all in a clean, modern interface.

---

## 📸 Preview

Here are some screenshots of the app in action:

| ![Screenshot 1](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot0.png) | ![Screenshot 2](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot1.png) |
|:--:|:--:|
| **Main Interface** | **Genre Selection & Results** |

| ![Screenshot 3](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot2.png) | ![Screenshot 4](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot3.png) |
|:--:|:--:|
| **Scrollable Movie Grid** | **Hover & Poster View** |

| ![Screenshot 5](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot4.png) |
|:--:|
| **Dark Netflix-Inspired UI** |

---

## 🚀 Features

- 🎞️ Recommend **top 30 movies** per genre  
- 🖼️ Display **movie posters** inside the app  
- 💡 Clean, dark-themed interface inspired by Netflix  
- ⚡ Lightweight and **easy to run** — connects directly to the TMDb API  

---

## 🧠 How It Works

The app connects to the **TMDb API** to retrieve the most popular, top-rated movies by genre:

1. Select a genre from the dropdown menu.  
2. The app displays the **top 30 recommended movies** for that genre.  
3. Each poster is clickable — double-click to open the movie’s page on TMDb.  
4. Press **“I’ve already seen these movies”** to load more suggestions.

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** – GUI framework  
- **Pillow (PIL)** – image handling  
- **Requests** – API requests  
- **TMDb API** – movie data source  

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/mirconegri/MovieRecommender.git
cd MovieRecommender
```

Create a virtual environment and install dependencies:
```
python3 -m venv venv
source venv/bin/activate   # On `macOS/Linux`
venv\Scripts\activate      # On `Windows`
pip install -r requirements.txt
```
Then, Insert yout TMDb API key in [main.py](https://github.com/mirconegri/MovieRecommender/blob/main/main.py) run the app:
```
python3 main.py
```

---

### 👤 Author & Connect

**Mirco Negri** — *Computer Science Student @ UniTrento*

[![Portfolio](https://img.shields.io/badge/Portfolio-00599C?style=for-the-badge&logo=globe&logoColor=white)](https://mirconegri.github.io/Portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mirconegri)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mirco-negri-263810225)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mirconegri06@gmail.com)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mirco_negri_?igsh=MWtlbXY0a3R4NTJmNA==)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/share/172rhaPCUK/)

### 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
<br>
© 2026 Mirco Negri
