import requests


class YaUploader:
  def __init__(self, token: str):
    self.token = token

  def upload(self, file_path: str):
    """Метод загруджает файл file_path на яндекс диск"""
    #ya_path = 'path=netology%5C'
    over_write = '&overwrite=true'
    stat = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_path+over_write}', headers={'Accept': 'application/json', 'Authorization': self.token})
    print(stat)
    send_url = stat.json()['href']
    file_to_send = {file_path : open(file_path, 'rb')}
    print(file_to_send)
    # putting = requests.put(send_url, file_to_send, headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': self.token})
    puttting = requests.put(send_url, data=file_to_send, headers={'Accept': 'application/json'})
    print(puttting)
    # print(puttting.json())
    return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
  
  uploader = YaUploader(t)
  result = uploader.upload('1.txt')
