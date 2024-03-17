import threading
import requests

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}


class WEB_DIR(threading.Thread):
    def __init__(self, url_queue, domain):
        threading.Thread.__init__(self)
        self._queue = url_queue
        self._domain = domain

    def run(self):
        while not self._queue.empty():
            url = self._queue.get()
            try:
                response = requests.get(url, headers=head, timeout=1)
                if response.status_code in [200, 302, 403]:
                    print('[*]' + url + ' status[' + str(response.status_code) + ']')
                    # 使用当前命令行参数传入的域名命名文件
                    file_name = f"{self._domain}.txt"
                    # 保存内容到以当前命令行参数传入的域名命名的文件中
                    with open(file_name, 'a') as file:
                        file.write('[*]' + url + ' status[' + str(response.status_code) + ']\n')
            except:
                pass
