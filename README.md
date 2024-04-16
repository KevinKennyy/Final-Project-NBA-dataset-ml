## NBA Match Results Predictor

### Overview
The "NBA Match Results Predictor" project focuses on predicting the outcome of NBA basketball games using various team statistics and game-specific information. The project utilizes machine learning techniques, specifically a random forest classifier, to analyze historical NBA match data and make predictions about future game results. The application provides a user-friendly interface built with Streamlit, allowing users to input game-related parameters such as team abbreviations, matchups, game date, and season type. Once the data is entered, the model predicts whether the home team will win or lose the game based on the provided information. The project aims to assist NBA enthusiasts and sports analysts in making informed predictions about game outcomes.

### Structure
The project is organized as follows:

- **app.py:** The main Python script that executes the project and serves as the user interface.
- **total_data_final.csv:** Dataset containing clean and preprocessed NBA match data.
- **new_random_forest_regressor.pkl:** Pretrained machine learning model for predicting match results.
- **utils.py:** Utility functions for data preprocessing and model loading.
- **requirements.txt:** List of required Python packages.

### Setup
**Prerequisites:** Make sure you have Python 3.11+ installed on your system. You'll also need pip to install the required Python packages.

**Installation:**

1. Clone the project repository to your local machine.
2. Navigate to the project directory and install the required Python packages:
pip install -r requirements.txt

## Running the Application
To run the application, execute the app.py script from the root directory of the project:


streamlit run app.py
Working with the Data
The project uses the total_data_final.csv file as the dataset for training the machine learning model. If you need to preprocess or analyze the data further, you can modify the app.py script or create additional Python scripts to handle these tasks.

Contributors:

Kevin Badillo

Dario Zerpa

Notes
This project assumes basic familiarity with Python programming and machine learning concepts.
For any issues or questions, please contact.
