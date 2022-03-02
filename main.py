from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def _get_upload_link(self, file_path):
        upload_url = ""
        heders = self.get_heders()
        params = {"path": file_path, "owerwrite": "true"}
        response = requests.get(upload_url, heders=heders, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str, file_name: str):
        href = self._get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_name, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)