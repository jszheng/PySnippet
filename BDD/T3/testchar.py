import chardet
import codecs

fp = codecs.open('test.txt', 'r', 'UTF-8')
raw = fp.read()
code = compile(raw, 'test.txt', 'exec')


