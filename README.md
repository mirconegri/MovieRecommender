# 🎬 Movie Recommender

[![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A desktop GUI application built with Python and Tkinter that recommends top-rated movies by genre using **The Movie Database (TMDb) API**, displaying posters and ratings in a clean, dark, Netflix-inspired interface.

## Table of Contents

- [Preview](#preview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration / Environment](#configuration--environment)
- [Contributing](#contributing)
- [License](#license)

## Preview

| Main Interface | Genre Selection & Results |
|:---:|:---:|
| ![Screenshot 1](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot0.png) | ![Screenshot 2](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot1.png) |

| Scrollable Movie Grid | Hover & Poster View |
|:---:|:---:|
| ![Screenshot 3](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot2.png) | ![Screenshot 4](https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot3.png) |

**Dark Netflix-Inspired UI**

<p align="center"><img src="https://raw.githubusercontent.com/mirconegri/MovieRecommender/main/images/screenshot4.png"></p>

## Features

- Genre-based movie discovery via TMDb's `discover` endpoint, sorted by rating (highest `vote_average` first, filtered to titles with at least 200 votes)
- Displays up to 20 movies per page in a scrollable 5-column poster grid, each showing title, release year, and rating
- **"I've already seen these movies"** button to paginate and load the next batch of results for the same genre
- Double-click any poster to open that movie's page directly on TMDb in your default browser
- Dark, Netflix-inspired Tkinter UI (custom `ttk` styling)

## Tech Stack

- **Language:** Python 3
- **GUI:** Tkinter / `ttk`
- **Image handling:** Pillow (`PIL`)
- **HTTP requests:** `requests`
- **Data source:** [TMDb API](https://www.themoviedb.org/documentation/api)

> **Note:** `requirements.txt` also lists `pandas`, which is not currently imported or used anywhere in `main.py`. It can likely be removed unless it's intended for a future feature.

## Getting Started

### Prerequisites

- Python 3
- A free TMDb API key (see [Configuration](#configuration--environment) below)

### Installation

```bash
git clone https://github.com/mirconegri/MovieRecommender.git
cd MovieRecommender
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Usage

Once your API key is configured (see below), run:

```bash
python3 main.py
```

1. Select a genre from the dropdown menu
2. Click **🎥 Recommend Movies**
3. Browse the scrollable poster grid — top-rated movies for that genre appear automatically
4. Double-click a poster to open its TMDb page in your browser
5. Click **"I've already seen these movies"** to load the next page of recommendations

## Configuration / Environment

This project does **not** use a `.env` file. The TMDb API key must be set directly as a constant at the top of `main.py`:

```python
API_KEY = "YOUR PERSONAL API KEY"
```

To obtain a key:
1. Create a free account at [themoviedb.org](https://www.themoviedb.org/)
2. Generate an API key from your account settings
3. Replace the placeholder value of `API_KEY` in `main.py` with your own key

Without a valid key, genre loading will fail on startup and the app will show an error dialog.

## Contributing

Contributions are welcome! To propose a change:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes with a clear message
4. Open a Pull Request

Found a bug or have a feature idea? Open an [Issue](https://github.com/mirconegri/MovieRecommender/issues).

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

© 2026 Mirco Negri
