import re

def get_headers(text):
    headers={}
    ex = '\s*(.*?):(.*)'
    text_list = re.findall(ex,text)
    for text in text_list:
        headers[text[0]] = text[1]
    return headers

if __name__ == '__main__':
    text = '''
            晨哥:小坏蛋
            小明:大帅哥
            奥利奥:大肥猫
            朱耍强:睡睡觉
            梦凡:去约会
    '''
    get_headers(text)
