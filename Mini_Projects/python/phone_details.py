import phonenumbers
from phonenumbers import geocoder, carrier, timezone

#Phone numbers
num = input("Enter the phone number: ")
try:
    phone_number = phonenumbers.parse(num, "IN")
    #phonenumbers.is_valid_number(num)
except:
    print("Invalid Number")

else:
    #Phone number regions
    try:
        phone_region = geocoder.description_for_valid_number(phone_number, "en")
        country = geocoder.country_name_for_number(phone_number, "en")
    except:
        print("Region Not Found")
    else:
        print("\nPhone Number's Region: ", phone_region)
        print("Origin Country: ", country)

    #Phone number service providers
    try:
        number_provider = carrier.name_for_valid_number(phone_number, "en")
    except:
        print("Service Provider Not Found")
    else:
        print("Service Provider: ", number_provider)

    #Phone number time zone
    try:
        time_zone = timezone.time_zones_for_number(phone_number)
    except:
        print("Time Zone Not Found")
    else:
        print("Time Zone: ", time_zone)