import phonenumbers
from phonenumbers import geocoder, carrier

#Phone numbers
num = input("Enter the phone number: ")
try:
    phone_number = phonenumbers.parse(num)
except:
    print("Invalid Number")

else:
    #Phone number regions
    try:
        phone_region = geocoder.description_for_number(phone_number, "en")
    except:
        print("Region Not Found")
    else:
        print("\nPhone Number's Region: ", phone_region)

    #Phone number service providers
    try:
        number_provider = carrier.name_for_number(phone_number, "en")
    except:
        print("Service Provider Not Found")
    else:
        print("Service Provider: ", number_provider)