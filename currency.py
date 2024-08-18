import requests

KEY = 'b046d6f0fee4f4bf7298256a'
URL = 'https://v6.exchangerate-api.com/v6/'

def get_exchange_rate(base_currency, target_currency):
    url = f"{URL}/{KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'conversion_rate' in data:
            return data['conversion_rate']
        else:
            print("Error: Unable to retrieve conversion rate.")
    else:
        print("Error: Unable to connect to the API.")
    return None

def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Currency Converter")
    
    base_currency = input("Enter the base currency : ").upper()
    target_currency = input("Enter the target currency : ").upper()
    amount = float(input(f"Enter the amount in {base_currency}: "))
    rate = get_exchange_rate(base_currency, target_currency)
    
    if rate:
        converted_amount = convert_currency(amount, rate)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed. Please try again.")

if __name__ == "__main__":
    main()