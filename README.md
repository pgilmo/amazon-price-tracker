# 🛒 Amazon Price Tracker Bot

A robust and efficient Python-based web scraper that monitors Amazon product prices in real-time. It alerts you via the console as soon as the price drops below your specified target.

## 🌟 Key Features

- **Real-Time Scraping**: Uses `BeautifulSoup4` to extract precise pricing data from Amazon's live site.
- **Error Handling**: Built with `try-except` blocks to prevent crashes during network timeouts or HTML changes.
- **Smart Retry Logic**: 
  - On success: Waits **1 hour** before the next check to avoid server spam.
  - On failure: Retries every **1 minute** until the connection is restored.
- **Clean Execution Logs**: Displays formatted timestamps for every check, keeping you informed of the bot's status.
- **Professional Structure**: Organized using the `if __name__ == "__main__":` entry point standard.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/pgilmo/amazon-price-tracker.git](https://github.com/pgilmo/amazon-price-tracker.git)
   cd amazon-price-tracker
Set up a virtual environment (Recommended):

Bash
python -m venv venv
# Activate on Windows:
.\venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
⚙️ Configuration
Before running the bot, you need to set your target product. Open main.py and modify the configuration section at the top:

Python
# Paste the full Amazon URL
URL = '[https://www.amazon.es/your-chosen-product-link](https://www.amazon.es/your-chosen-product-link)'

# Set your target price in Euros (€)
DESIRED_PRICE = 10.0
🚀 Usage
Simply run the script from your terminal:

Bash
python main.py
The bot will stay active in your terminal, checking the price every hour. If the price is equal to or lower than your DESIRED_PRICE, you will see a success message!

📋 Requirements
Python 3.x

requests

beautifulsoup4

⚠️ Disclaimer
This project was created for educational purposes. Please be mindful of Amazon's policies regarding automated web scraping. Use it responsibly and do not overwhelm their servers with high-frequency requests.

Developed by pgilmo
