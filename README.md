# Hebrew Vocabulary Flashcards 🇮🇱

An interactive desktop application built with Python to help users learn the 1,000 most common Hebrew words. The project features a custom-built data pipeline that dynamically fetches translations and phonetic pronunciations using Google Cloud APIs.

## 🚀 Features

* **Interactive GUI:** A flashcard-style user interface built with `Tkinter` for a smooth learning experience.
* **Smart Progress Tracking:** The application tracks user progress by removing known words from the active learning pool and updating the dataset dynamically using `pandas`.
* **Google APIs Integration:** Utilizes Google Cloud Translation and Google Transliteration APIs to automatically generate accurate English translations and Romanized phonetics for Hebrew words.
* **Automated Data Pipeline:** A standalone builder script that processes raw text files, interacts with external APIs, and generates structured CSV datasets ready for the application.

## 📊 Data Source & Processing

The original Hebrew frequency word list was sourced from the [InvokeIT Frequency Word Lists](https://invokeit.wordpress.com/frequency-word-lists/). 
For this application, the raw dataset of 10,000 words was filtered and reduced to the **top 1,000 most frequently used words** to provide an optimal entry-level learning curve.

## 🛠️ Technologies Used

* **Language:** Python
* **Libraries:** `pandas`, `requests`, `Tkinter`
* **External Services:** Google Cloud Translation API (v2), Google Transliteration API

## 📁 Project Structure

* `main.py` - The core application script containing the UI and flashcard game logic.
* `data_builder.py` - The data pipeline script that fetches data from Google APIs and generates the CSV.
* `hebrew_words.txt` - The raw text file containing the top 1,000 Hebrew words.
* `data/` - Directory containing the generated `hebrew_words.csv` and `words_to_learn.csv` files.
* `images/` - UI assets and icons.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yanivgekhman/hebrew-flash-cards.git
   cd hebrew-flash-cards
2. **Install required dependencies**:
   ```bash
   pip install pandas requests
3. **Set up Google Cloud API credentials:**
   To run the data builder script, you need a valid Google Cloud API Key.
Set your API key in the data_builder.py file or securely via an environment variable.
**Note**: The API key is not included in this repository for security reasons).
4. **Run the data builder script to generate the CSV files:**
   ```bash
   python data_builder.py
5. **Start the flashcard application:**
   ```bash
   python main.py
## 👨‍💻 Author
**Yaniv Gekhman** 
- LinkedIn: [https://www.linkedin.com/in/yanivgeh/](https://www.linkedin.com/in/yanivgeh/)
