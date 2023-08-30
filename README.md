# Flight Price Tracker

This script helps you track and notify about the lowest flight prices for various destinations. It uses flight search APIs to find flight prices and notifies you through SMS and email if there's a low price for any destination.

## Prerequisites

- Python 3.x
- Install required packages using the following command: pip install -r requirements.txt

## Setup

1. Clone this repository.
2. Create a virtual environment (optional but recommended).
3. Install the required packages as mentioned in the prerequisites.
4. Obtain necessary API keys:
  - Flight search API: You need an API key to access flight data.
  - Twilio API: For sending SMS notifications.
  - SMTP server details: For sending email notifications.

## Usage

1. Open `main.py` and update the following variables with your information:

 - `ORIGIN_CITY_IATA`: The IATA code of the city you are departing from.
 - API keys and credentials: Update the relevant sections with your API keys and credentials.

2. Run the script: python main.py

The script will fetch destination data, check flight prices, and notify you if there's a low price.
The script will iterate through the destination data, checking flight prices for each destination. If a flight with a lower price than the previously recorded lowest price is found, you will receive an SMS and an email notification.
The destination data will be updated with the new lowest prices.
Important Note

Make sure to keep your API keys, credentials, and other sensitive information secure and private. You can use environment variables or a configuration file to manage these values securely.
