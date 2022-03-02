from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token):
        self.token = token
        
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    
    def _get_upload_link(self, file_path):
        upload_url = "http://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "owerwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        pprint(headers)
        return response.json()

    def upload(self, file_path, file_name):
        href = self._get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_name, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")



if __name__ == '__main__':
    path_to_file = "C:/Users/birulya.i/Desktop/Python/Netology/Ydisk/test.txt"
    file_name = "test.txt" 
    token = ""
    uploader = YaUploader(token)
    uploader.upload(path_to_file, file_name)