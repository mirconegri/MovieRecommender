import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import io
import webbrowser

# ======================================================
# 🧩 CONFIGURATION SECTION
# ======================================================
# TMDb API (The Movie Database) provides access to movie data.
# You must replace "YOUR PERSONAL API KEY" with your actual TMDb API key.
API_KEY = "YOUR PERSONAL API KEY"
BASE_URL = "https://api.themoviedb.org/3"
IMG_URL = "https://image.tmdb.org/t/p/w200"  # Base URL for poster images (200px wide)

# ======================================================
# 🌐 FUNCTIONS TO FETCH DATA FROM TMDb API
# ======================================================
def get_genres():
    """
    Fetches all movie genres from TMDb API.
    Returns a dictionary mapping genre name → genre ID.
    Example: {"Action": 28, "Comedy": 35, ...}
    """
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    r = requests.get(url, params=params)
    data = r.json()
    return {g["name"]: g["id"] for g in data.get("genres", [])}

def get_movies_by_genre(genre_id, page=1, limit=20):
    """
    Fetches a list of movies by genre, sorted by rating.
    - genre_id: TMDb numeric ID for the genre
    - page: which result page to fetch (TMDb paginates results)
    - limit: max number of movies to show (default: 20)
    Returns a list of movie dicts (title, poster_path, etc.)
    """
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "vote_average.desc",  # top-rated movies first
        "with_genres": genre_id,
        "vote_count.gte": 200,           # filter out poorly-rated or obscure films
        "page": page
    }
    r = requests.get(url, params=params)
    return r.json().get("results", [])[:limit]

# ======================================================
# 🎬 LOAD GENRES ON STARTUP
# ======================================================
try:
    GENRES = get_genres()
except Exception as e:
    # If API fails (e.g., wrong API key, no internet), show an error box and exit
    messagebox.showerror("Error", f"Unable to fetch genres:\n{e}")
    exit()

# ======================================================
# 🪟 TKINTER UI SETUP
# ======================================================
root = tk.Tk()
root.title("🎬 Movie Recommender")
root.geometry("1000x900")
root.configure(bg="#121212")  # enable dark mode theme (Netflix-like)

# ======================================================
# 🎨 COMBOBOX STYLE (modern dark look)
# ======================================================
style = ttk.Style()
style.theme_use('clam')  # use the modern 'clam' theme
style.configure(
    "TCombobox",
    fieldbackground="#1e1e1e",
    background="#1e1e1e",
    foreground="white",
    arrowcolor="white",
    font=("Segoe UI", 12)
)

# ======================================================
# 📦 GLOBAL VARIABLES
# ======================================================
ACCENT_COLOR = "#E50914"      # Netflix red
TEXT_COLOR = "white"
INFO_FONT = ("Segoe UI", 10)

# Lists to hold dynamically loaded widgets and images
posters = []          # store references to PhotoImage objects (to prevent garbage collection)
movie_widgets = []    # keep track of movie frames (used for layout updates)
current_genre_id = None
current_page = 1
movies_per_page = 20

# ======================================================
# 🧠 CORE LOGIC + UI FUNCTIONS
# ======================================================
def open_movie(movie_id):
    """
    Opens the selected movie’s TMDb page in the default web browser.
    Triggered by double-clicking a movie poster.
    """
    webbrowser.open(f"https://www.themoviedb.org/movie/{movie_id}")

def show_movies_grid(movies):
    """
    Displays movies in a grid (5 columns per row) inside a scrollable frame.
    Each movie shows:
      - Poster image (or emoji placeholder)
      - Title, release year, and rating
    """
    global movie_widgets
    columns = 5

    for movie in movies:
        # Determine grid coordinates
        row = len(movie_widgets) // columns
        col = len(movie_widgets) % columns

        # Create a dark frame for each movie
        frame = tk.Frame(scroll_frame, bg="#1e1e1e")
        frame.grid(row=row, column=col, padx=10, pady=15, sticky="n")

        # --- Movie Poster ---
        poster_url = movie.get("poster_path")
        if poster_url:
            # Fetch and resize the image from TMDb
            img_data = requests.get(IMG_URL + poster_url).content
            img = Image.open(io.BytesIO(img_data)).resize((140, 210))
            img_tk = ImageTk.PhotoImage(img)
            posters.append(img_tk)  # store reference
            lbl_img = tk.Label(frame, image=img_tk, bg="#1e1e1e", cursor="hand2")
            lbl_img.pack()
            # Bind double-click to open TMDb page
            lbl_img.bind("<Double-Button-1>", lambda e, id=movie["id"]: open_movie(id))
        else:
            # Fallback if no poster is available
            lbl_img = tk.Label(frame, text="🎞️", font=("Segoe UI", 30),
                               bg="#1e1e1e", fg="white")
            lbl_img.pack()

        # --- Movie Info Text ---
        title = f"{movie['title']} ({movie.get('release_date','')[:4]})\n⭐ {movie.get('vote_average','N/A')}"
        lbl_text = tk.Label(
            frame,
            text=title,
            justify="center",
            wraplength=140,
            bg="#1e1e1e",
            fg="white",
            font=INFO_FONT
        )
        lbl_text.pack(pady=5)

        movie_widgets.append(frame)

    # Ensure even column spacing
    for i in range(columns):
        scroll_frame.columnconfigure(i, weight=1)

def load_more_movies():
    """
    Loads the next page of movies for the same genre.
    Increments current_page and appends new movies to the grid.
    """
    global current_page
    current_page += 1

    # Fetch next page of movies
    movies = get_movies_by_genre(current_genre_id, page=current_page, limit=movies_per_page)
    if not movies:
        messagebox.showinfo("Info", "No more movies found.")
        return

    show_movies_grid(movies)

    # Reposition "Load more" button below the new movies
    load_more_btn.grid(row=(len(movie_widgets)//5)+1, column=0, columnspan=5, pady=20)

def on_recommend():
    """
    Triggered when the user clicks the “🎥 Recommend Movies” button.
    Clears the current movie grid, resets pagination,
    and fetches the top-rated movies for the selected genre.
    """
    global current_genre_id, current_page, movie_widgets

    # Clear the previous movie results
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    posters.clear()
    movie_widgets.clear()
    current_page = 1

    # Check if a genre is selected
    genre_name = genre_var.get()
    if not genre_name:
        messagebox.showwarning("Warning", "Please select a genre first.")
        return

    # Get the TMDb genre ID and fetch movies
    current_genre_id = GENRES[genre_name]
    movies = get_movies_by_genre(current_genre_id, page=current_page, limit=movies_per_page)

    if not movies:
        tk.Label(scroll_frame, text="No movies found.", bg="#121212", fg="gray").pack()
        return

    # Display movie results
    show_movies_grid(movies)

    # Add “load more” button
    global load_more_btn
    load_more_btn = tk.Button(
        scroll_frame,
        text="I've already seen these movies",
        bg=ACCENT_COLOR,
        fg="white",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        padx=8,
        pady=6,
        command=load_more_movies
    )
    load_more_btn.grid(row=(len(movie_widgets)//5)+1, column=0, columnspan=5, pady=20)

# ======================================================
# 🧱 HEADER
# ======================================================
header_frame = tk.Frame(root, bg="#121212")
header_frame.pack(fill="x", pady=(10, 0))
tk.Label(
    header_frame,
    text="Double-click a movie poster to open it on TMDb",
    font=("Segoe UI", 10),
    bg="#121212",
    fg="gray"
).pack()

# ======================================================
# 🎭 GENRE SELECTION
# ======================================================
genre_frame = tk.Frame(root, bg="#121212")
genre_frame.pack(pady=10)

# Label for genre selection
tk.Label(
    genre_frame,
    text="Select a genre:",
    font=("Segoe UI", 12),
    bg="#121212",
    fg=TEXT_COLOR
).pack()

# Dropdown menu populated with available genres
genre_var = tk.StringVar()
genre_dropdown = ttk.Combobox(
    genre_frame,
    textvariable=genre_var,
    values=list(GENRES.keys()),
    font=("Segoe UI", 12),
    state="readonly"
)
genre_dropdown.pack(pady=5)

# Button to trigger recommendations
btn = tk.Button(
    genre_frame,
    text="🎥 Recommend Movies",
    bg=ACCENT_COLOR,
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=12,
    pady=6,
    command=on_recommend
)
btn.pack(pady=8)

# ======================================================
# 📜 SCROLLABLE MOVIE GRID
# ======================================================
canvas_frame = tk.Frame(root, bg="#121212")
canvas_frame.pack(fill="both", expand=True)

# Canvas is used for scrolling large content
canvas = tk.Canvas(canvas_frame, bg="#121212", highlightthickness=0)
scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scroll_frame = tk.Frame(canvas, bg="#121212")

# Bind scroll region dynamically when content changes
scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a window inside the canvas that holds all movie frames
canvas.create_window((0, 0), window=scroll_frame, anchor="nw", tags="frame_window")

# Resize inner frame when the window changes
def resize_canvas(event):
    canvas.itemconfig("frame_window", width=event.width)

canvas.bind("<Configure>", resize_canvas)
canvas.configure(yscrollcommand=scrollbar.set)

# Pack components
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ======================================================
# 🚀 START APPLICATION
# ======================================================
root.mainloop()