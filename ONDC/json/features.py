#Collaborating all the functions here

def signed_in():
    #Check if user is signed in to the website
    return "Sorry! Not built yet."


def trending():
    #Show links to some trending articles
    return "Sorry! Not built yet."


def article():
    #Gives info about a particular item
    return "Sorry! Not built yet."


def preferences():
    #Displays user's preferences
    return "Sorry! Not built yet."


def option_2(parts):
    #Decides what to display on basis of user's input
    if parts == "ratings":
        return "ratings()"
    elif parts == "feedback" or parts == "reviews":
        return "feedback()"
    elif parts == "product quality details":
        return "product quality details()"
    elif parts == "360 view":
        return "360 view"
    elif parts == "trial room":
        return "trial()"
    elif parts == "similar products":
        return "similar()"
    else:
        return "Sorry, I don't have that information right now."