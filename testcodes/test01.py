from urllib import parse 
import os
import ntpath

#url을 잘 분석해 봅니다.
url = parse.urlsplit('https://www.exeam.org/focuse/index.html?examParam1=value1&examParam1=value2&examParam2=value2#welcome')
#------------------------------------------------------------------------------------------------------------------------

print(url) #parse결과 여러가지로 분해된다.
#SplitResult(scheme='https', netloc='www.exeam.org', path='/index.html', query='examParam1=value1&examParam2=value2', fragment='welcome')

print(url.scheme, url.netloc, url.path, url.query, url.fragment)
#https www.exeam.org /index.html examParam1=value1&examParam2=value2 welcome

#쿼리스트링만 전문적으로 다룰려면 이렇게
print(parse.parse_qs(url.query))  # 리스트가 있는 딕셔너리 형태로 반환한다.
#{'examParam1': ['value1', 'value2'], 'examParam2': ['value2']}


#마지막 리소스 파일을 대처할때.
res = parse.urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
print(res)

fileURL = 'http://www.cwi.nl/%7Eguido/Python.html'
# '/path/to/somefile.ext' -> '/path/to/somefile' '.ext'
filename, file_extension = os.path.splitext(fileURL)
print(filename,file_extension)
# '/path/to/somefile.ext' -> somefile.ext
saved_name = ntpath.basename(filename+"_result"+file_extension)
print(saved_name)