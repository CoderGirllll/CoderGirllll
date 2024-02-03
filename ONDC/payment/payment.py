import requests

response = requests.get("https://google.com")   #Website url

code = response.status_code    #Storing the status code

#Function to check the code
def check(code):
    if ((code//100) == 2):   #Success codes
        return "OK"
    elif ((code//100) == 1):    #Information codes
        if (code == 101):
            return "Switching Protocols: Setting the environment to process the information."   #This code is a response to an Upgrade header field request and states the protocol the server will switch to.
        elif (code == 102):
            return "Processing: The request is being processed."    #This response indicates the server received and is processing the request, but no response is yet available.
        else:
            return "Sorry, we're unable to detect the reason for this payment failure."
    elif ((code//100) == 3):    #Redirection codes
        if (code == 301):
            return "Moved permanently: This site/piece of information has been moved to another location."
        elif (code == 307):
            return "Temporary redirect: Redirecting to another site for a short while."
        elif (code == 308):
            return "Permanent redirect: Redirecting to another site."
        else:
            return "Sorry, we're unable to detect the reason for this payment failure."
    elif ((code//100) == 4):    #Client Error codes
        if (code == 400):
            return "Bad request: This is not a safe request."
        elif (code == 401):
            return "Unauthorized: You are not authorized to view this site."    #The user doesn’t have valid authentication credentials to get the requested resource.
        elif (code == 402):
            return "Payment required: Payment is required to view this site."   #Reserved for future use. Rarely used.
        elif (code == 403):
            return "Forbidden: The contents of this site are forbidden from public use."    #The client doesn’t have access rights to the content.
        elif (code == 404):
            return "Not found: The site/information you are looking for is not available."
        elif (code == 405):
            return "Method not allowed: The method you're trying to use is not allowed."    #The server supports the request method, but the target resource doesn’t.
        elif (code == 406):
            return "Not appectable: This value is not acceptable."    #The server doesn’t find any content that satisfies the criteria given by the user according to the Accept headers requested.
        elif (code == 407):
            return "Proxy authentication required: The server is unable to authenticate the client due to lack authentication credetails."
        elif (code == 408):
            return "Request Timeout: The time limit for this site (payment) is over. Please refresh the page."    #The server timed out waiting because the client didn’t produce a request within the allotted time.
        elif (code == 409):
            return "Conflict: The request cannot be completed due to a conflict with the current state of the resource."    #The server can’t fulfill the request because there’s a conflict with the resource. It’ll display information about the problem so the client can fix it and resubmit.
        elif (code == 410):
            return "Gone: The content requested has been permanently deleted from the server and will not be reinstated."
        elif (code == 412):
            return "Precondition failed: The client indicates preconditions in the header fields that the server fails to meet."
        elif (code == 413):
            return "Payload too large: The client’s request is larger than the server’s defined limits, and the server refuses to process it."
        elif (code == 417):
            return "Expectation failed: The server can’t meet the requirements indicated by the Expect request header field."
        elif (code == 421):
            return "Misdirected request: The client sends a request to a server that can’t produce a response."
        elif (code == 422):
            return "Unprocessable entity: The client correctly sends the request, but the server can’t process it because of semantic errors or similar issues."
        elif (code == 423):
            return "Locked: The requested method’s resource is locked and inaccessible."
        elif (code == 424):
            return "Failed dependency: The request failed because a request the initial request depended on also failed."
        elif (code == 425):
            return "Too early: The server is unwilling to process a request that might be replayed."
        elif (code == 426):
            return "Update required: The server refuses to process the request using the current protocol unless the client upgrades to a different protocol."
        elif (code == 428):
            return "Precondition required: The server needs the request to be conditional."
        elif (code == 429):
            return "Too Many Requests: The user sends too many requests in a certain amount of time."
        elif (code == 451):
            return "Unavailable for legal reasons: The user requests a resource the server can’t legally provide."
        else:
            return "Sorry, we're unable to detect the reason for this payment failure."
    elif ((code//100) == 5):    #Server Error codes
        if (code == 500):
            return "Internal Server Error: The server has encountered an unexpected error and cannot complete the request."
        elif (code == 501):
            return "Not Implemented: The server can’t fulfill the request or doesn’t recognize the request method."
        elif (code == 502):
            return "Bad Gateway: The server acts as a gateway and gets an invalid response from an inbound host."
        elif (code == 503):
            return "Service Unavailable: The server is unable to process the request. This often occurs when a server is overloaded or down for maintenance."
        elif (code == 504):
            return "Gateway Timeout: The server was acting as a gateway or proxy and timed out, waiting for a response."
        elif (code == 506):
            return "Variant Also Negotiates: The server has an internal configuration error."
        elif (code == 507):
            return "Insufficient Storage: The server doesn’t have enough storage to process the request successfully."
        elif (code == 508):
            return "Loop Detected: The server detects an infinite loop while processing the request."
        elif (code == 509):
            return "Network Authentication Required: The client must be authenticated to access the network."
        else:
            return "Sorry, we're unable to detect the reason for this payment failure."
    

print(check(code))