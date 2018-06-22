
"""尽量使用泛匹配，非贪婪 ，有换行的话用re.s"""
import re
content = 'Hello 123 4567 World_This is Regex Demo'
#空格\s 数字\d 字母\w
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$',content)
#print(result.group())
#print(result.span())

"""泛匹配"""
result2 = re.match('^Hello.*Demo$',content)
#print(result2)

"""匹配目标"""
result3 = re.match('.*\s(\d+)\s.*?',content)
#print(result3.group(1))

result4 = re.match('.*\s(\w+)',content)
#print(result4.group(1))

"""匹配模式"""
content2 = 'Hello 123 4567 World_This ' \
           'is Regex Demo'
result5 = re.match('.*?',content2)
print(result5)