from bs4 import BeautifulSoup
import urllib2

def main():
	#f = open('ListOfSites.txt','r+')
	fname = 'Results.txt'
	i = 0
	with open('ListOfSites.txt','r+') as f:
		for line in f:
			i = i + 1
			url = line
			data = urllib2.urlopen(url).read()
			bs =BeautifulSoup(data,"lxml")
			print bs.title

			number = str(i)
	    	
			if(bs.title == "<title>Trend Micro InterScan Web Security Event</title>"):
				with open(fname, 'a') as outf:
	        			#outf.write(i)
	        			outf.write(number + ' is Banned\n')

			else:
				with open(fname, 'a') as outf:
	        			#outf.write(i)
	        			outf.write(number + ' can be opened\n')


if __name__=="__main__":
	main()