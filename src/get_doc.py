import requests
from bs4 import BeautifulSoup
import html2text

res_url = r'https://golang.google.cn/doc/'

#custom headers
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
# get
def get_content(url):
    r = requests.get(url)
    try:
        r.raise_for_status()
        soup = BeautifulSoup(r.content,"lxml")
        return soup
    except Exception as e:
        print(e)
        exit()

def make_tree(url_split,d=dict):
    if len(url_split) == 1:
        if url_split[0]:
            d[url_split[0]] = False
    else: 
        if d.get(url_split[0],0):
            make_tree(url_split[1:],d[url_split[0]])
        else:
            d[url_split[0]]=dict()
            make_tree(url_split[1:],d[url_split[0]])
        

def get_tree(soup):
    '''<soup> is expected to get from catalog '''
    tag = soup.find_all(href=True)
    all_url = [i['href'] for i in tag]
    fit_url = set()
    tree=dict()
    for i in all_url:
        if i[:4]=='http':
            continue
        else:
            fit_url.add(i)
    for i in fit_url:
        make_tree(i.split('/'),tree)
    return tree

def input_pos(tree):
    url = []
    input_ = True
    while input_:
        if tree:
            for idx, i in enumerate(tree):
                print(f'{idx:-<3d}>{i}')
            index = int(input('(enter 99 to finish)>>'))
            if  index == 99:
                tree = tree.keys()
                break
            else:
                node = list(tree.keys())[index]
                url.append(node)
                tree = tree[node]

        else:
            tree = ['']
            input_ = False
    url = '/'.join(url)
    url_list = [url+'/'+ i for i in tree]
    print('\n'.join(url_list))
    return url_list


def get_article(soup):
    article=soup.find('article')
    if not article:
        print('未发现<article>标签，请修改匹配特征')
        return ''
    return html2text.html2text(str(article))

def struct_markdown(urls):
    for url in urls:
        file_name = url.split('/')[-1]+'.md'
        print(f':{url}--->{file_name}')
        soup = get_content(url)
        with open(file_name,'w') as f:
            f.write(get_article(soup))

def main():
    res_url = input('目录url>>')
    root = '/'.join(res_url.split('/')[:3])
    catalog_soup = get_content(res_url)
    tree = get_tree(catalog_soup)
    print('链接结构 -------------┒')
    urls = input_pos(tree)
    urls = [root + '/' + i for i in urls]
    struct_markdown(urls)
    print('-----------------finsh----------------')

    
if __name__ == '__main__':
    main()