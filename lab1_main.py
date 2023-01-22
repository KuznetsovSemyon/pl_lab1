from tqdm import tqdm
import requests
import sys
import time

def downloadFile( url, filename ):
    res = requests.get(url, stream=True)
    totalSize = int(res.headers.get('content-length', 0)) 
    blSize = 1024
    progBar = tqdm(total=totalSize, unit="iB", unit_scale=True)
    with open(filename, 'wb') as file :
        for data in res.iter_content(blSize):
            time.sleep(1)
            progBar.update(len(data))
            file.write(data)

def main( ):
    if (sys.argv[1] == None):
        print('URL is required')
    else:
        url = sys.argv[1]
        filename = url.split("/")[-1]
        downloadFile(url, filename)


# py lab1_main.py 'URL'
if __name__ == '__main__':
    main()