#wordcount 计算英文字符每个单词出现的次数
#返回一个字典，key为单词，value为对应单词出现的次数。
#{'hello': 1, 'world': 1, 'this': 1, 'is': 4, 'an': 1, 'example': 1, 'word': 1, 'count': 2,
# 'fun': 3, 'it': 2, 'to': 1, 'words': 1, 'yes': 1}
import re
from collections import Counter

input = """Hello world!  
This is an example.  
Word count is fun.  
Is it fun to count words?  
Yes, it is fun!"""

def wordcount(input_word:str):
    '''
    input:str
    output:dict
    '''
    # 使用正则表达式去除标点符号，并将所有单词转换为小写
    words = re.findall(r'\b\w+\b', input_word.lower())

    # 计算每个单词出现的次数
    word_counts = Counter(words)

    return dict(word_counts)

result = wordcount(input)
print('result dict',result)
