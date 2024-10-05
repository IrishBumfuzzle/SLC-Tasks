from bs4 import BeautifulSoup 
import urllib.request
import urllib.parse
import os.path

file_extension = ".pdf" # extension to be searched for
file_type = "all" # this can be all or office depending upon how we want the links to be sorted
# file_type = "office"


if not os.path.exists("Files"):
    os.makedirs("Files")
r = urllib.request.urlopen("https://intranet.iiit.ac.in")
soup = BeautifulSoup(r, 'html.parser')

links = soup.find_all('a', href=True)

if file_type == "all":
    f = open("Files/urls.txt", "w")
    for link in links:
        href_link = link['href'].strip().replace(" ", "%20") # some links have leading whitespace in the website for some reason
        if file_extension in href_link and "http" not in href_link: # only intranet files 
            f.write("https://intranet.iiit.ac.in"+href_link+"\n")
            

        elif "http" not in href_link: # only intranet links are recursively added
            while True: # because shit server
                try:
                    r = urllib.request.urlopen("https://intranet.iiit.ac.in" + href_link)
                    break
                except:
                    pass
            soup = BeautifulSoup(r, 'html.parser')
            for recursion in soup.find_all('a', href=True):
                if recursion not in links: # without this program recurses on itself and forms infine loop
                    links.append(recursion)
    f.close()

else:
    f = open("Files/Homepage.txt", "w") # these are the links in the homepage of intranet
    office_sorter = {}
    for link in links:
        href_link = link['href'].strip().replace(" ", "%20") # some links have leading whitespace in the website for some reason
        if file_extension in href_link and "http" not in href_link: # only intranet files 
            f.write("https://intranet.iiit.ac.in"+href_link+"\n")
            

        elif "http" not in href_link and "office=" in href_link: # only intranet links and links which have an office are recursively added
            while True: # because shit server
                try:
                    r = urllib.request.urlopen("https://intranet.iiit.ac.in" + href_link)
                    break
                except:
                    pass
            soup = BeautifulSoup(r, 'html.parser')
            office_name = urllib.parse.unquote_plus(href_link.split("=")[1])
            if(office_name in office_sorter):
                office_sorter[office_name].extend(soup.find_all('a', href=True))
            else:
                office_sorter[office_name] = (soup.find_all('a', href=True))
    f.close()

    for key in office_sorter:
        f = open("Files/"+key+".txt", "w")
        for link in office_sorter[key]:
            if file_extension in href_link and "http" not in href_link: # only intranet files 
                f.write("https://intranet.iiit.ac.in"+href_link+"\n")
        f.close()




