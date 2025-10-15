import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import io
import webbrowser

# -----------------------------
# TMDb API config
# -----------------------------
API_KEY = "YOUR KEY"
BASE_URL = "https://api.themoviedb.org/3"
IMG_URL = "https://image.tmdb.org/t/p/w200"

# -----------------------------
# Functions to fetch data
# -----------------------------
def get_genres():
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    r = requests.get(url, params=params)
    data = r.json()
    return {g["name"]: g["id"] for g in data.get("genres", [])}

def get_movies_by_genre(genre_id, page=1, limit=20):
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "vote_average.desc",
        "with_genres": genre_id,
        "vote_count.gte": 200,
        "page": page
    }
    r = requests.get(url, params=params)
    return r.json().get("results", [])[:limit]

# -----------------------------
# Load genres
# -----------------------------
try:
    GENRES = get_genres()
except Exception as e:
    messagebox.showerror("Error", f"Unable to fetch genres:\n{e}")
    exit()

# -----------------------------
# Tkinter setup
# -----------------------------
root = tk.Tk()
root.title("🎬 Movie Recommender")
root.geometry("1000x900")
root.configure(bg="#121212")  # dark mode

# ===== Modern dark style for Combobox =====
style = ttk.Style()
style.theme_use('clam')  # modern theme
style.configure("TCombobox",
                fieldbackground="#1e1e1e",  # background of text field
                background="#1e1e1e",       # background of dropdown
                foreground="white",          # text color
                arrowcolor="white",          # arrow color
                font=("Segoe UI", 12))       # font

# -----------------------------
# Global variables
# -----------------------------
ACCENT_COLOR = "#E50914"
TEXT_COLOR = "white"
INFO_FONT = ("Segoe UI", 10)
posters = []
movie_widgets = []
current_genre_id = None
current_page = 1
movies_per_page = 20

# -----------------------------
# Functions for UI and logic
# -----------------------------
def open_movie(movie_id):
    webbrowser.open(f"https://www.themoviedb.org/movie/{movie_id}")

def show_movies_grid(movies):
    global movie_widgets
    columns = 5
    for movie in movies:
        row = len(movie_widgets) // columns
        col = len(movie_widgets) % columns

        frame = tk.Frame(scroll_frame, bg="#1e1e1e")
        frame.grid(row=row, column=col, padx=10, pady=15, sticky="n")

        # poster image
        poster_url = movie.get("poster_path")
        if poster_url:
            img_data = requests.get(IMG_URL + poster_url).content
            img = Image.open(io.BytesIO(img_data)).resize((140, 210))
            img_tk = ImageTk.PhotoImage(img)
            posters.append(img_tk)
            lbl_img = tk.Label(frame, image=img_tk, bg="#1e1e1e", cursor="hand2")
            lbl_img.pack()
            lbl_img.bind("<Double-Button-1>", lambda e, id=movie["id"]: open_movie(id))
        else:
            lbl_img = tk.Label(frame, text="🎞️", font=("Segoe UI", 30), bg="#1e1e1e", fg="white")
            lbl_img.pack()

        title = f"{movie['title']} ({movie.get('release_date','')[:4]})\n⭐ {movie.get('vote_average','N/A')}"
        lbl_text = tk.Label(frame, text=title, justify="center", wraplength=140,
                            bg="#1e1e1e", fg="white", font=INFO_FONT)
        lbl_text.pack(pady=5)

        movie_widgets.append(frame)

    # Center columns
    for i in range(columns):
        scroll_frame.columnconfigure(i, weight=1)

def load_more_movies():
    global current_page
    current_page += 1
    movies = get_movies_by_genre(current_genre_id, page=current_page, limit=movies_per_page)
    if not movies:
        messagebox.showinfo("Info", "No more movies found.")
        return
    show_movies_grid(movies)
    load_more_btn.grid(row=(len(movie_widgets)//5)+1, column=0, columnspan=5, pady=20)

def on_recommend():
    global current_genre_id, current_page, movie_widgets
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    posters.clear()
    movie_widgets.clear()
    current_page = 1

    genre_name = genre_var.get()
    if not genre_name:
        messagebox.showwarning("Warning", "Please select a genre first.")
        return

    current_genre_id = GENRES[genre_name]
    movies = get_movies_by_genre(current_genre_id, page=current_page, limit=movies_per_page)
    if not movies:
        tk.Label(scroll_frame, text="No movies found.", bg="#121212", fg="gray").pack()
        return

    show_movies_grid(movies)

    # Load more button
    global load_more_btn
    load_more_btn = tk.Button(scroll_frame, text="I've already seen these movies", bg=ACCENT_COLOR, fg="white",
                              font=("Segoe UI", 12, "bold"), relief="flat", padx=8, pady=6, command=load_more_movies)
    load_more_btn.grid(row=(len(movie_widgets)//5)+1, column=0, columnspan=5, pady=20)

# -----------------------------
# Header
# -----------------------------
header_frame = tk.Frame(root, bg="#121212")
header_frame.pack(fill="x", pady=(10, 0))
tk.Label(header_frame, text="Double-click a movie poster to open it on TMDb",
         font=("Segoe UI", 10), bg="#121212", fg="gray").pack()

# -----------------------------
# Genre selection frame
# -----------------------------
genre_frame = tk.Frame(root, bg="#121212")
genre_frame.pack(pady=10)

tk.Label(genre_frame, text="Select a genre:", font=("Segoe UI", 12), bg="#121212", fg=TEXT_COLOR).pack()

genre_var = tk.StringVar()
genre_dropdown = ttk.Combobox(genre_frame, textvariable=genre_var,
                              values=list(GENRES.keys()), font=("Segoe UI", 12), state="readonly")
genre_dropdown.pack(pady=5)

btn = tk.Button(genre_frame, text="🎥 Recommend Movies", bg=ACCENT_COLOR, fg="white",
                font=("Segoe UI", 12, "bold"), relief="flat", padx=12, pady=6, command=on_recommend)
btn.pack(pady=8)

# -----------------------------
# Scrollable canvas for movies
# -----------------------------
canvas_frame = tk.Frame(root, bg="#121212")
canvas_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(canvas_frame, bg="#121212", highlightthickness=0)
scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scroll_frame = tk.Frame(canvas, bg="#121212")

scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scroll_frame, anchor="nw", tags="frame_window")

def resize_canvas(event):
    canvas.itemconfig("frame_window", width=event.width)

canvas.bind("<Configure>", resize_canvas)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# -----------------------------
# Start the Tkinter main loop
# -----------------------------
root.mainloop()
