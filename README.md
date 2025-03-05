# Bidoo Points Scraper

This tool scrapes links from the [Bidoo Puntate Gratis Telegram Channel](https://t.me/bidoo_puntate_gratis) and automatically opens Bidoo links to collect free bet points on [Bidoo](https://it.bidoo.com).

## Features
- Automates the process of collecting free bet points.
- Parses Telegram messages to extract Bidoo links.
- Uses the Telegram API for authentication and data retrieval.
- Runs with minimal configuration using `config.ini`.
- Handles Cloudflare anti-bot pages.
- Closes tabs automatically after processing links.

## Prerequisites
- Python 3.x installed.
- `telethon` package for Telegram API interaction.
- `requests` package for handling HTTP requests.
- `beautifulsoup4` package for parsing HTML content.
- `pyautogui` for automating browser interactions.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourrepo/bidoo_scraper.git
   cd bidoo_scraper
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
1. Create a `config.ini` file in the project root.
2. Obtain `api_id` and `api_hash` from [Telegram API](https://core.telegram.org/api/obtaining_api_id).
3. Add the following content to `config.ini`:
   ```ini
   [Telegram]
   api_id = YOUR_API_ID
   api_hash = YOUR_API_HASH
   ```

## Usage
Run the script to start scraping and opening Bidoo links:
```sh
python bidoo_points.py
```

## Technical Details
- The script uses `telethon` to connect to Telegram and fetch messages from the channel.
- Extracted links are opened using Python's `webbrowser` or `requests` for automation.
- Implements logic to detect Cloudflare's anti-bot page and pause execution if necessary.
- The script handles login sessions securely using a `.session` file.
- Uses `pyautogui` to close the opened browser tabs after processing links.

## Notes
- Ensure you are subscribed to the [Telegram Channel](https://t.me/bidoo_puntate_gratis) for access to the latest free bet links.
- The script may require periodic updates if the Telegram API or Bidoo link structure changes.
- Cloudflare protection might change, requiring additional bypass mechanisms.

