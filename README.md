# Assignment-1-End-to-End-Sentiment-Analysis-Pipeline

This project implements a sentiment analysis pipeline using the IMDB Movie Reviews dataset. The process includes data acquisition, storage, cleaning, exploration, model training, and serving via a Flask API. 
---

## Project Setup

### Steps

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Ensure you have the IMDB dataset saved as imdb_reviews.csv in the project directory.

4. Database Setup: The project uses SQLite for data storage. The database (imdb_reviews.db) is automatically created when the script runs.

5. Data Acquisition
   The dataset is expected to be a CSV file (imdb_reviews.csv) containing two columns:
   review: The text of the movie review.
   sentiment: The label (positive or negative).
If the dataset is not already available, you can download it from Kaggle or any similar source.

6. Run Instructions
   Run the Training Script **data_setup_and_train_model.ipynb**.
   This also includes data cleaning, exploratory analysis, and model training. This will generate and save the IMDB_Dataset..db, model.pkl and vectorizer.pkl file.

7. Start the Flask Server
   Start the Flask API to serve the trained model:
   ```bash
   python app.py
   ```
   The server will be accessible at http://localhost:5000.
   
9. Testing the Endpoint
   Run the test.py to test the api Endpoint.
   ```bash
   python test.py
   ```
   You can provide your know text to view the sentiment.
   
### Model Info
**Algorithm**: Logistic Regression
**Feature Extraction**: TF-IDF Vectorization

### Files Included
app.py: Main script for the pipeline and API.
test.py: To test the api endpoint.
data_setup_and_train_model.ipynb: File for data setup and model training.
imdb_reviews.csv: Dataset file (not included, must be added manually).
requirements.txt: Dependencies for the project.
model.pkl and vectorizer.pkl: Trained model and TF-IDF vectorizer (generated during training).
