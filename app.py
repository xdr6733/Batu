import requests

while True:
    try:
        response = requests.get('https://sanane-yarram.onrender.com/')
        print(response.text)
    except Exception as e:
        # Hata detayını yazdırmak istersen:
        # print(f"Hata oluştu: {e}")
        pass
