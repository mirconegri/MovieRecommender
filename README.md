# 🎬 Movie Recommender

[![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A desktop GUI application that recommends top-rated movies by genre using the TMDb API, displaying posters and ratings in a scrollable, dark, Netflix-inspired interface.

Built to solve a specific friction point: streaming platforms surface what they want to promote, not what is objectively highest-rated in a genre. This tool queries TMDb directly, filters by minimum vote count to avoid statistical noise, and pages through results so previously seen titles can be skipped without leaving the app.

## Table of Contents

- [Preview](#preview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration and Environment](#configuration-and-environment)
- [Contributing](#contributing)
- [License](#license)

## Preview

| Main Interface | Genre Selection & Results |
|:---:|:---:|
| ![Screenshot 1](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot0.png) | ![Screenshot 2](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot1.png) |

| Scrollable Movie Grid | Poster Detail View |
|:---:|:---:|
| ![Screenshot 3](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot2.png) | ![Screenshot 4](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot3.png) |

**Full Dark UI**

<p align="center"><img src="https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot4.png"></p>

## Features

- Genre-based discovery via TMDb's `discover` endpoint — results sorted by `vote_average` descending, filtered to titles with at least 200 votes to avoid low-sample noise
- Scrollable 5-column poster grid displaying title, release year, and rating for up to 20 titles per page
- **"I've already seen these movies"** pagination button — loads the next batch for the same genre without resetting the genre selection
- Double-click any poster to open the movie's TMDb page in the system default browser
- Custom dark `ttk` theme throughout — no external UI library required

## Tech Stack

- **Language:** Python 3
- **GUI:** Tkinter / `ttk`
- **Image handling:** Pillow (`PIL`)
- **HTTP:** `requests`
- **Data source:** [TMDb API v3](https://developer.themoviedb.org/docs)

> `requirements.txt` includes `pandas`, which is not imported or used anywhere in `main.py`. This dependency should be removed before any production or distribution use — it adds roughly 30 MB to the install footprint for no benefit.

## Project Structure

```
MovieRecommender/
├── main.py              # Application entry point — UI, TMDb fetch, poster grid
├── requirements.txt
├── images/
│   ├── screenshot0.png
│   ├── screenshot1.png
│   ├── screenshot2.png
│   ├── screenshot3.png
│   └── screenshot4.png
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites

- Python 3
- A free TMDb API key — see [Configuration and Environment](#configuration-and-environment)

### Installation

```bash
git clone https://github.com/mirconegri/MovieRecommender.git
cd MovieRecommender
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Configure your API key first (see below), then run:

```bash
python3 main.py
```

1. Select a genre from the dropdown
2. Click **Recommend Movies**
3. Browse the poster grid — double-click any title to open its TMDb page
4. Click **I've already seen these movies** to load the next page

## Configuration and Environment

The TMDb API key is set as a constant at the top of `main.py`:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

To obtain a key:

1. Create a free account at [themoviedb.org](https://www.themoviedb.org/)
2. Go to **Settings → API** and generate a key
3. Replace the placeholder in `main.py`

Without a valid key the genre fetch fails on startup and the app displays an error dialog.

> The key is embedded directly in source rather than read from an environment variable. If you fork this project, ensure `main.py` is excluded from any public commits that contain a real key — or refactor to read from `os.environ` instead.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes with a clear message
4. Open a Pull Request

For bugs or feature ideas, open an [Issue](https://github.com/mirconegri/MovieRecommender/issues).

### Author

**Mirco Negri** — Computer Science @ UniTrento

[![Portfolio](https://img.shields.io/badge/Portfolio-00599C?style=for-the-badge&logo=globe&logoColor=white)](https://mirconegri.github.io/Portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mirconegri)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mirco-negri-263810225)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mirconegri06@gmail.com)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
