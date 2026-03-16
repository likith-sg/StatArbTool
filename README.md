# StatArbTool

## Project Overview

StatArbTool is a comprehensive trading strategy backtesting platform designed to help traders and investors optimize their arbitrage opportunities. The tool utilizes advanced statistical models to identify profitable trade windows and provides real-time data visualization for seamless decision-making.

### Key Features:

*   Advanced arbitrage strategy backtesting
*   Real-time data visualization for informed decision-making
*   Customizable model parameters for optimized performance
*   Integration with popular APIs for seamless data acquisition

## Tech Stack

### Languages & Frameworks:

*   **Python**: Primary programming language used for development and maintenance.
*   **Streamlit**: Used for building a user-friendly web-based interface.

### Libraries & Dependencies:

*   `numpy` for numerical computations
*   `pandas` for data manipulation and analysis
*   `scikit-learn` for machine learning algorithms
*   `statsmodels` for statistical modeling
*   `matplotlib` and `seaborn` for data visualization

## Installation & Setup

To set up StatArbTool, follow these steps:

1.  **Install Requirements**: Run the following command in your terminal:
    ```bash
pip install -r requirements.txt
```
2.  **Clone Repository**: Clone the repository using Git:
    ```bash
git clone https://github.com/your-username/statarbtool.git
```

## Usage

1.  **Run the Application**: Open a terminal and navigate to the project directory:
    ```
cd statarbtool
```
2.  **Run Streamlit**: Start the application using Streamlit:
    ```bash
streamlit run app.py
```
3.  **Access the Dashboard**: Open your web browser and navigate to `http://localhost:8501`.

## API Endpoints

The following endpoints are available:

*   `GET /`: Returns a list of available APIs.
*   `GET /api/dashboard/stats`: Displays statistical information about the trading strategy.
*   `POST /api/auth/signin`: Authenticates users and returns a token.

## Configuration

Environment variables can be set using the following command:
```bash
export API_KEY="your_api_key"
```
Replace "your_api_key" with your actual API key.

## Project Structure

The project consists of the following main files:

*   `app.py`: Contains the Streamlit application code.
*   `requirements.txt`: Lists dependencies required for installation.
*   `strategies/stat_arb.py`: Defines custom trading strategy backtesting functions.
*   `utils/cointegration.py`: Provides functions for cointegration analysis.
*   `modelsThresholdStrategy.py`: Implements a threshold-based trading strategy.