from bs4 import BeautifulSoup
import requests
from itertools import zip_longest
import csv


search_word = input("Enter the job you seek: ")
print('Preparing your excel sheet...')


def WordURL():
    if ' ' in search_word:
        word = '+'.join(search_word.split(' '))
        URL = f'https://wuzzuf.net/search/jobs/?a=navbl&q={word}&a=navbl'
    else:
        URL = f'https://wuzzuf.net/search/jobs/?a=navbl&q={search_word}&a=navbl'
    return URL


response = requests.get(url=WordURL())
soup = BeautifulSoup(response.text, "html.parser")

Jobs_title = [job.getText() for job in soup.find_all(name='h2', class_='css-m604qf')]
companies = [company.getText() for company in soup.find_all(name='a', class_='css-17s97q8')]
Location = [location.getText() for location in soup.find_all(name='span', class_='css-5wys0k')]
skills = [skill.getText() for skill in soup.find_all(name='div', class_='css-y4udm8')]

links = ["https://wuzzuf.net" + link.get('href') for link in soup.find_all(name='a', class_='css-o171kl', rel='noreferrer')]

newer_jobs_time = [time.getText() for time in soup.find_all(name='div', class_='css-4c4ojb')]
older_jobs_time = [time.getText() for time in soup.find_all(name='div', class_='css-do6t5g')]

times = newer_jobs_time + older_jobs_time
requirements = []
for link in links:
    response = requests.get(url=link)
    soup = BeautifulSoup(response.text, 'html.parser')
    req = soup.find(name='div', class_='css-1t5f0fr').find('ul')

    try:
        requirements.append(req.getText())
    except AttributeError:
        requirements.append('Not Found')

file_list = [Jobs_title, companies, Location, skills, links, requirements, times]
exported = zip_longest(*file_list)

with open("jobs.csv", mode='w', encoding='utf-8') as file:
    wr = csv.writer(file)
    wr.writerow(["Job title", "Company", "Location", "Skills", "Links", "Requirements", "Date"])
    wr.writerows(exported)

print('Done.')
