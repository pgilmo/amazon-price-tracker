# 🛒 Amazon Price Tracker Bot

A robust Python-based web scraper that monitors Amazon product prices and alerts you via console when the price drops below your target.

## 🚀 Features
- **Real-time Data Extraction**: Powered by `BeautifulSoup4` and `Requests`.
- **Fault-Tolerant Logic**: Implements `try-except` blocks to handle network issues or HTML structure changes without crashing.
- **Automated Retry System**: Distinguishes between successful checks (1-hour wait) and failed attempts (1-minute retry).
- **Execution Logs**: Displays clear timestamps and status updates for every check.
- **Clean Architecture**: Follows the `if __name__ == "__main__":` professional standard.

## 🛠️ Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/your-username/amazon-price-tracker.git](https://github.com/your-username/amazon-price-tracker.git)
   cd amazon-price-tracker