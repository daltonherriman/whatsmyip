from requests import get 

public_ip = get('https://api.ipify.org').text

print(f"Public IP: {public_ip}")