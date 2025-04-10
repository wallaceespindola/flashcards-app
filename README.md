# Flashcards App

A web-based flashcards application that allows users to upload and study flashcards from CSV files.

## Description

This project is a Flask-based web application that demonstrates:

- **CSV Upload**: Easy import of flashcards via CSV files
- **Interactive UI**: Flip cards, navigate through sets
- **Keyboard Navigation**: Use arrow keys for efficient studying
- **Modern Design**: Clean and responsive interface
- **Set Management**: Create and delete flashcard sets

## Features

- **CSV Import**: Upload your flashcard sets in CSV format
- **Interactive Cards**: Click or use keyboard to flip cards
- **Keyboard Shortcuts**:
  - ↑/↓: Flip card
  - ←/→: Navigate between cards
- **Progress Tracking**: See your position in the deck
- **Set Management**: Delete sets you no longer need
- **Mobile Responsive**: Study on any device

## Requirements

- Python 3.11+
- Flask
- Modern web browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/wallaceespindola/flashcards-app.git
cd flashcards-app
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the application with:

```bash
python app.py
```

Open your browser at http://localhost:5000 to start using the flashcards app.

## CSV Format

Your CSV files should follow this format:
```csv
question,answer
"What is the capital of France?","Paris"
"What is 2+2?","4"
```

You can also include a header row with "Question" and "Answer" (case insensitive).

The name of the uploaded file will be used as the name of the flashcard set.

## Some screenshots

The home:
![The home](/resources/img-home-page.png)

The study cards:
![The study cards](/resources/img-study-cards.png)

You finished cards:
![You finished cards](/resources/img-study-cards-finished.png)

## Author Information

- **LinkedIn**: [linkedin.com/in/wallaceespindola](https://linkedin.com/in/wallaceespindola/)
- **GitHub**: [github.com/wallaceespindola](https://github.com/wallaceespindola)
- **Email**: wallace.espindola@gmail.com
- **Twitter/X**: [@wsespindola](https://twitter.com/wsespindola)
- **Dev Community**: [dev.to/wallaceespindola](https://dev.to/wallaceespindola)
- **DZone**: [DZone Profile](https://dzone.com/users/1254611/wallacese.html)
- **Website**: [W-Tech IT Solutions](https://www.wtechitsolutions.com/)

## License

This project is released under the Apache 2.0 License.
See the LICENSE file for details.

Copyright 2025 Wallace Espindola.
