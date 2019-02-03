import os
import requests
import pathlib
import time
import re 
import spoof

from threading import Thread


currentdir = os.path.dirname(__file__)

def func1():



	os.system("dir "+currentdir)

	os.system("mitmdump -s spoof.py")

def func2():
	url = "http://mitm.it/cert/p12"
	r = requests.get(url)
	d = r.headers['content-disposition']
	fname = re.findall("filename=(.+)", d)
	filename = pathlib.Path(fname[0])

	open(filename, 'wb').write(r.content)
	os.system(str(filename))


def main():
	Thread(target = func1).start()

	Thread(target = func2).start()

if __name__ == '__main__':
	main()