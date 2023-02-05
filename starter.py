import requests
from job import Job
from bs4 import BeautifulSoup

print('Starting...')
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

links = results.find_all("a", class_='card-footer-item')
python_job_links = []

print('\nCollecting all python developer job descriptions links')
# get all python job links
for link in links:
    job_position_link = link.get("href")[44:]
    if link.text == "Apply" and "python" in job_position_link: 
        python_job_links.append(link.get("href"))
print('Collected successfully ✅')

print('\nCollecting all python developer job details. This could take awhile ⌛️')
python_job_list = [] # list of Job object
for link in python_job_links:
    # soup each link
    dev_page = requests.get(link)
    dev_soup = BeautifulSoup(dev_page.content, "html.parser")

    # parse job details
    job_title = dev_soup.find(class_="title is-2").string
    company = dev_soup.find(class_="subtitle is-4 company").string
    content = dev_soup.find(class_="content")
    description = content.p.string
    # clean location
    dirty_location = content.find(id="location")
    dirty_location.strong.extract() # remove bolded location tag
    location = dirty_location.string

    python_job = Job(job_title, company, description, location)
    python_job_list.append(python_job)

print('\nCollected successfully ✅\n\n')
# complete task
for job in python_job_list:
    print('=' * 50)
    print(job.title)
    print(job.company)
    print(job.location)
    print(job.desc)
print('Here is the list of all python developer jobs 👨‍💻')