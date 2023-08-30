import requests

USERNAME = os.environ["SHEETY_AUTH_USERNAME"]
PASSWORD = os.environ["SHEETY_PASSWORD"]
BASIC_AUTH_PARAMS = (USERNAME, PASSWORD)
SHEETY_USERNAME = os.envrion["SHEETY_USERNAME"]

PROJECT = "flightDeals"
SHEET = "users"

base_url = "https://api.sheety.co"


def post_new_row(first_name, last_name, email):
    endpoint_url = f"/{SHEETY_USERNAME}/{PROJECT}/{SHEET}"
    url = base_url + endpoint_url

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=url, auth=BASIC_AUTH_PARAMS, json=body)
    response.raise_for_status()
