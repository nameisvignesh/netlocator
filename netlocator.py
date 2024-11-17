import phonenumbers
from phonenumbers import carrier, geocoder

def get_mobile_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get the carrier name
        service_provider = carrier.name_for_number(parsed_number, "en")

        # Get the geographical location
        location = geocoder.description_for_number(parsed_number, "en")

        return {
            "Number": phone_number,
            "Service Provider": service_provider,
            "Location": location
        }
    except phonenumbers.NumberParseException:
        return {"Error": "Invalid phone number format."}

if __name__ == "__main__":
    # Display ASCII art header once
    print("""
 THE_  ______________    ___   ____    _  _________  ____  
| \ | | ____|_   _| |   / _ \ / ___|  / \|_   _/ _ \|  _ \ 
|  \| |  _|   | | | |  | | | | |     / _ \ | || | | | |_) |
| |\  | |___  | | | |__| |_| | |___ / ___ \| || |_| |  _ < 
|_| \_|_____| |_| |_____\___/ \____/_/   \_|_| \___/|_| \_\
          \nby nameisvignesh                                  
    """)

    while True:
        number_to_check = input("Enter the mobile number (with country code) or 'exit' to quit: ")
        
        if number_to_check.lower() == 'exit':
            print("Exiting the NetLocator tool. Goodbye :)")
            break
        
        info = get_mobile_info(number_to_check)
        
        print("\nMobile Number Information:")
        for key, value in info.items():
            print(f"{key}: {value}")