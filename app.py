import csv
import io
import json
import logging

from flask import Flask, render_template, request, redirect, flash

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your-super-secret-key-123'  # Set a secure secret key for session management


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'csv_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['csv_file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Read and parse the CSV file
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            logger.info(f"Reading CSV file: {file.filename}")
            csv_input = csv.reader(stream)
            flashcards = []
            # Check if the first row is a header
            header = next(csv_input)
            if header[0].strip().lower() in ['question', 'q']:
                for row in csv_input:
                    if len(row) >= 2:
                        append_and_log(flashcards, row)
            else:
                # If no header, treat the first row as a flashcard
                flashcards.append({'question': header[0], 'answer': header[1]})
                for row in csv_input:
                    if len(row) >= 2:
                        append_and_log(flashcards, row)

            # Immediately render the flashcard page with the first flashcard visible
            logger.info(f"Rendering flashcards page with {len(flashcards)} flashcards")
            return render_template('flashcards.html', flashcards=json.dumps(flashcards))
    return render_template('index.html')


def append_and_log(flashcards, row):
    flashcards.append({'question': row[0], 'answer': row[1]})
    logger.info(f'Flashcard added - question: {row[0]} -> answer: {row[1]}')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
