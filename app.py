import csv
import io
import json
import logging
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = "your-super-secret-key-123"  # Set a secure secret key for session management

# Store flashcard sets in memory (in a real app, this would be a database)
flashcard_sets = {}


def format_title(filename):
    # Remove file extension
    title = filename.rsplit(".", 1)[0]
    # Replace dashes and underscores with spaces
    title = title.replace("-", " ").replace("_", " ")
    # Convert to title case
    return title.title()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "csv_file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["csv_file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file:
            # Read and parse the CSV file
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            logger.info(f"Reading CSV file: {file.filename}")
            # Use a maximum field size that can handle long answers
            csv.field_size_limit(100000)
            csv_input = csv.reader(stream, delimiter=";", skipinitialspace=True)  # Simple semicolon delimiter
            flashcards = []
            # Check if the first row is a header
            header = next(csv_input)
            if header[0].strip().lower() in ["question", "q"]:
                for row in csv_input:
                    if len(row) >= 2:
                        append_and_log(flashcards, row)
            else:
                # If no header, treat the first row as a flashcard
                flashcards.append({"question": header[0], "answer": header[1]})
                for row in csv_input:
                    if len(row) >= 2:
                        append_and_log(flashcards, row)

            # Store the flashcard set with timestamp as ID
            set_id = datetime.now().strftime("%Y%m%d_%H%M%S")
            formatted_title = format_title(file.filename)
            flashcard_sets[set_id] = {
                "name": formatted_title,
                "filename": file.filename,
                "cards": flashcards,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "card_count": len(flashcards),
            }

            # Immediately render the flashcard page with the first flashcard visible
            logger.info(f"Rendering flashcards page with {len(flashcards)} flashcards")
            return render_template("flashcards.html", flashcards=json.dumps(flashcards), title=formatted_title)

    # For GET requests, show the upload form and list of saved sets
    return render_template("index.html", flashcard_sets=flashcard_sets)


@app.route("/set/<set_id>")
def view_set(set_id):
    if set_id in flashcard_sets:
        flashcards = flashcard_sets[set_id]["cards"]
        return render_template(
            "flashcards.html", flashcards=json.dumps(flashcards), title=flashcard_sets[set_id]["name"]
        )
    flash("Flashcard set not found")
    return redirect("/")


@app.route("/delete/<set_id>", methods=["POST"])
def delete_set(set_id):
    if set_id in flashcard_sets:
        del flashcard_sets[set_id]
        flash("Flashcard set deleted successfully")
    else:
        flash("Flashcard set not found")
    return redirect("/")


def append_and_log(flashcards, row):
    # Take the full answer text as is, regardless of commas
    question = row[0].strip()
    answer = row[1].strip()
    flashcards.append({"question": question, "answer": answer})
    logger.info(f"Flashcard added - question: {question} -> answer: {answer}")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
