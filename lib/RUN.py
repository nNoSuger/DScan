import queue

from lib.WEB import WEB_DIR


def run(domain, path, count):
    urls = []
    with open(path, mode='r+') as f1:
        for line in f1.readlines():
            subdomain = line.strip()
            url = subdomain + '.' + domain
            url = 'http://' + url if not url.startswith('http://') else url
            urls.append(url)

    url_queue = queue.Queue()
    for url in urls:
        url_queue.put(url)

    threads = []
    thread_count = int(count)
    for i in range(thread_count):
        threads.append(WEB_DIR(url_queue, domain))

    for t in threads:
        t.start()

    for t in threads:
        t.join()
