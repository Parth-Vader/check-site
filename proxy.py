from bs4 import BeautifulSoup
import urllib2

def main():
	#f = open('ListOfSites.txt','r+')
	fname = 'Results.txt'
	i = 0
	with open('ListOfSites.txt','r+') as f:
		for line in f:
			i = i + 1
			number = str(i)
			url = line
			data = urllib2.urlopen(url).read()
			bs =BeautifulSoup(data,"lxml")
			while True:
						try:
							print bs.title

										    	
							with open(fname, 'a') as outf :
						        			#outf.write(i)
					       				outf.write(number + ' can be opened\n')
					       				break
				        
				        	except urllib2.URLError:
						        	#if(bs.title == "<title>Trend Micro InterScan Web Security Event</title>"):
							with open(fname, 'a') as outf :
			        			#outf.write(i)
					        			outf.write(number + ' is Banned\n')
					        			break

					
if __name__=="__main__":
	main()
