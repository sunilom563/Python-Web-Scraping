from bs4 import BeautifulSoup
import requests
import time
import data1      #importing the Database file we created

def crawlWebPage(tablename):
    htmlText = requests.get('https://www.spiegel.de/international/').text
    soup = BeautifulSoup(htmlText, 'lxml')

    job = soup.find('section', class_='relative flex flex-wrap w-full')

    titles = []
    subTitles = []
    abstractData = []
    downloadTime = []

    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    downloadTime.append(current_time)

    jobTitles = job.find_all('span', class_='align-middle hover:opacity-moderate focus:opacity-moderate')
    for jobb in jobTitles:
        j=jobb.text
        titles.append(j)

    jobSubTitles = job.find_all('span', class_='block text-primary-base dark:text-dm-primary-base hover:text-primary-dark '
                                                  'focus:text-primary-darker font-brandUI font-extrabold lg:text-xl md:text-xl '
                                                  'sm:text-l leading-tight mb-8')
    for rapper in jobSubTitles:
        k=rapper.text.strip()
        subTitles.append(k)

    jobAbstract = job.find_all('span',class_='font-serifUI font-normal lg:text-l md:text-base sm:text-base leading-loose mr-6')
    for apper in jobAbstract:
        l=apper.text
        abstractData.append(l)

    for i in range(len(titles)-1):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        downloadTime.append(current_time)

    finalScrapedData = list(zip(titles, subTitles, abstractData, downloadTime))  #Merged all the data in a single list

    data1.insertdata(finalScrapedData, tablename)                                # Connecting to the database

if __name__ == '__main__':                                                       # triggering  to run automatically for every 15minutes
    while True:
        crawlWebPage("public.sun")
        print(f'Waiting  every 15 minutes')
        time.sleep(900)
