import requests
from Belong import myRequests
from tqdm import tqdm
def download(url,path,name,headers={}):
    header={
        'User-Agent':myRequests.get_agent()
    }
    header.update(headers)
    resp = requests.get(url=url, stream=True, headers=header)
    content_size = int(int(resp.headers['Content-Length']) / 1024)
    print("Size:"+str(content_size/1024)+'MB'+' or '+str(content_size)+'KB')
    with open(path+'\\'+name, "wb") as f:
         for data in tqdm(iterable=resp.iter_content(1024), total=content_size, unit='k', desc=name):
            f.write(data)
        # print("download finished!")