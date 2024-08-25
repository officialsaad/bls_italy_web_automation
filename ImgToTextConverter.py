# website URL: https://www.imgocr.com/p/api
# Refferal Token: https://www.imgocr.com/register/ref/66863d97c5462

import requests
import base64


def send_post_request(url, file_path):
    with open(file_path, 'rb') as file:
        file_data = base64.b64encode(file.read()).decode('utf-8')

    post_data = {
        'api_key': 'eebbeaff66f26be042aca84e66bbbfe1',
        'image': file_data
    }

    response = requests.post(url, data=post_data, verify=False)

    if response.status_code == 200:
        data = response.json()
        print("Response in jason format is :", data)
        text = data.get("text")
        print("caption text is :", text)
    else:
        print(f"Error: {response.status_code}")


# Usage example
# url = 'https://www.imgocr.com/api/imgocr_get_text'
file_path = 'capta_folder/image.jpg'
url = 'https://www.imgocr.com/api/imgocr_get_text'

send_post_request(url, file_path)
