#import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={}&l={}'
    # Complete the missing part of this function here 
    #format url and get response
    newURL = url.format(role, location)
    response = requests.get(newURL)
    job = BeautifulSoup(response.text, 'html.parser')
    #extract data from response
    title = job.find('h2', class_='jobTitle').text
    company = job.find('span', class_='companyName').text
    desc = job.find('div', class_='job-snippet').text
    salary = job.find('div', class_='salary-snippet-container').text
    #returns array
    return {"title":title, "company": company, "description":desc, "salary": salary}
    
#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    #with open()
    with open("jobDetails.json", "w") as job:
        json.dump(jobDetails, job)
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location you want to search")
    location = input()

    print("Job Role: ", role)
    print("Job Location: ", location)
    
    getJobList(role, location)


if __name__ == '__main__':
    main()
