# python libraries
import builtins
import camelcase
'''
builtins***
csv***     : <Prepare notes>
pickle***   :
datetime**
json*** json.dumps() json.loads() pickling/unpickling serialization/deserialization
logging***
pdb*** Debugging
pip***
unittest**
venv***

io**
os**
sys**
re**
random**
copy**
pdb**
base64**
threading**
multirproccesing**
collections**
http** - sftp https smtp ftp
time**
timeit**
xml**

urllib*
functools*
smtplib*
abc*        : abstract base class used in Abstract Class in OOPs
asyncio*    :
copy*


concurrent
html
http
importlib
site-packages
base64
calendar
contextlib
gzib
ipaddress
pathlib
ipaddress
smtplib
socket
sqlite3
ssl
subprocess
'''
# num =eval(input("hello: "))
# print(dir(num))
# print(help(AttributeError))
# print(dir(builtins))
# print(help(type(self)))
x = camelcase.CamelCase()
text = x.hump("hello world")
print(text)