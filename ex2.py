import requests


class YaUploader:
  def __init__(self, token: str):
    self.token = token

  def upload(self, file_path: str):
    """Метод загруджает файл file_path на яндекс диск"""
    over_write = '&overwrite=true'
    file_name = file_path.split('\\')[-1]
    stat = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_name+over_write}', headers={'Accept': 'application/json', 'Authorization': self.token})
    send_url = stat.json()['href']
    with open(file_path, 'rb') as file:
      requests.put(send_url, data=file, headers={'Accept': 'application/json'})
    return print(f"Файл {file_path} отправлен на Яндекс диск")


if __name__ == '__main__':

  uploader = YaUploader(t)
  result = uploader.upload("test\\2.txt")
