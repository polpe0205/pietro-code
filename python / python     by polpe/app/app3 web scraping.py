







import bs4,requests, webbrowser #inclusione delle librerie 
link = ' https://www.amazon.it/s?k=schede+grafiche+invidia&__mk_it_IT=ÅMÅŽÕÑ&ref=nb_sb_noss'
pre_link= ' https://www.amazon'

response =  requests.get(link)
response.raise_for_status()

#parte per andare diretti algli annunci con hiper link 
soup=bs4.BeautifulSoup(response.text, 'html.parser')
div_annunci=soup.find('div', class_='a-section aok-relative s-image-wide-16-15-aspect')




#parte per stampare e verificare i likn 
a_onion=div_annunci.find_all('a')
link_onion= []
for a_onion in a_onion:
    link_onion = str(a_onion.get('href'))
    if link in link_onion : 
        link_onion.append(link_onion)

