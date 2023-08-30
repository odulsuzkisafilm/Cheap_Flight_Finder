# Flight Price Tracker

This script helps you track and notify about the lowest flight prices for various destinations. It uses flight search APIs to find flight prices and notifies you through SMS and email if there's a low price for any destination.

## Setup

1. Clone this repository.
2. Create a virtual environment (optional but recommended).
3. Obtain necessary API keys:
  - Tequila API: You need an API key to access flight data.
  - Twilio API: For sending SMS notifications.
  - Sheety API: For accessing destination data.
  - SMTP server details: For sending email notifications.
4. Create a google sheets document with sheets named "prices" and "users".
  - Arrange the prices sheet such that it contains the columns: "City", "IATA Code" and "Lowest Price". Add the cities you wish to visit. IATA Codes will be automatically filled.    - Initialize the Lowest Price columns.
  - Add the users who will be notified, via running `signUp.py`
5. Update the environment variables using the API keys and urls obtained in step 3.

## Usage

1. Open `main.py` and update the following variables with your information:

 - `ORIGIN_CITY_IATA`: The IATA code of the city you are departing from.
 - API keys and credentials: Update the relevant sections with your API keys and credentials.

2. Run the script: `main.py`

The script will fetch destination data, check flight prices, and notify you if there's a low price.
The script will iterate through the destination data, checking flight prices for each destination. If a flight with a lower price than the previously recorded lowest price is found, you will receive an SMS and an email notification.
The destination data will be updated with the new lowest prices.

## Important Note

Make sure to keep your API keys, credentials, and other sensitive information secure and private. You can use environment variables or a configuration file to manage these values securely.
