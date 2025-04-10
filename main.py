from datetime import datetime

def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello from flashcards-app! Current time: {current_time}")


if __name__ == "__main__":
    main()
