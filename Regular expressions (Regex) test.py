import re

file_for_regex = open(r"C:\Users\dawid\OneDrive\Pulpit\Empty.txt",'r', encoding="utf-8")

file_to_read = file_for_regex.read()
print(type(file_to_read))
#print(file_for_regex.readlines())

title = re.findall(r'"title": ".+"', file_to_read)
print(title[0])
#matches the title as: "title": "Mid/Senior Backend Engineer @ Codete"



# images = bs.find_all('img',{'src':re.compile('..\/img\/gifts/img.*.jpg')})
# for image in images:
#     print(image['src'])
