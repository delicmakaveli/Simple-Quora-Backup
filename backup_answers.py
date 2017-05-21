from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from file_io import *
import textwrap
import requests
from selenium.webdriver.common.keys import Keys


print('Thank you for using Simple Quora Backup')
print('This will backup your ANSWERS to a text file in the simplest form, ')
print('so there are no images, links, etc, just simple text')
print('This is just in case Quora disappears some day :)')
print('\n')
print('NOTE:', 'Chrome WebDriver is buggy so it gets stuck sometimes during login or loading pages')
print('if that happens just close it and run the script again.')
print('\n')

boolean = True

osType = None
bit = None
path = None

while boolean:
    osType = input('Please type in your operating system type(windows, mac, linux)')
    if osType == 'windows':
        path = "WebDriver/win/chromedriver"
        break
    elif osType is 'mac':
        path = "WebDriver/mac/chromedriver"
        break
    elif osType is 'linux':
        while boolean:
            bit = input('Please choose your version (64-bit, 32-bit)')
            if bit is '64':
                path = "WebDriver/linux/64/chromedriver"
                break
            elif bit is '32':
                path = "WebDriver/linux/32/chromedriver"
                break
        break


email = None
password = None
while boolean:
    email = input('Please type in your Quora account email: ')
    if email is not None:
        break
while boolean:
    password = input('Please type in your Quora account password: ')
    if password is not None:
        break


numOfScrolls = 0
num = 0

while boolean:
    numOfScrolls1 = input('How many Answers do you have (approximately)?')
    if numOfScrolls1 is not None:
        numOfScrolls = int(numOfScrolls1)
        if numOfScrolls >= 10:
            num = numOfScrolls / 10
        else:
            num = 2
        break

browser = webdriver.Chrome(executable_path=path)
browser.get('https://www.quora.com/content?content_types=answers')
browser.maximize_window()
sleep(2)
quoraElems = browser.find_elements_by_xpath("//form/div/div/input")
emailQuora = quoraElems[0]
passwordQuora = quoraElems[1]
emailQuora.send_keys(email)
passwordQuora.send_keys(password)
passwordQuora.send_keys(Keys.RETURN)

sleep(3)
browser.get('https://www.quora.com/content?content_types=answers')
sleep(3)

print('Scrolling to load all ANSWERS...')

# scroll to the bottom
i = 0
while i < num:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(4)
    i += 1

# get html to extract content from
html = browser.page_source

# release resources
browser.close()
browser = None

# organize chaotic html
soup = BeautifulSoup(html, 'html.parser')

# find all the links to answers
answer_list = soup.find_all('a', {'class': 'question_link'})
answer_links = set()
link = ''
question_titles = set()

for ans in answer_list:
    question_title = ans.text
    question_titles.add(question_title)

print('You have ' + str(len(question_titles)) + ' answers')

# assemble the links and put them in a set
for answer in answer_list:
    link = 'https://www.quora.com' + str(answer.get('href'))
    answer_links.add(link)

# create folder and file to save to
dir_name = 'Quora Answers'
create_project_dir(dir_name)
create_data_file1(dir_name, '')
file_path = 'Quora Answers' + '/my_answers.txt'

print('Saving to file (my_answers.txt)...')

content = ''
title = ''
# scrape each link in the set and write to text file in formatted fashion
# write question title, answer content and the date that it was written
for link in answer_links:
    html = requests.get(link)
    soup = BeautifulSoup(html.content, 'html.parser')
    element = soup.find('div', {'class': 'Answer AnswerPageAnswer AnswerBase'})

    for q_title in question_titles:
        if q_title in soup.find('span', {'class': 'question_text'}).text:
            title = 'QUESTION TITLE ' + q_title

    q_text = element.text

    content = textwrap.fill(title, 66)
    writing = content.encode('utf-8')
    append_to_file(file_path, writing)

    content = textwrap.fill(q_text, 66)
    index = content.index('Views')
    content = content[0:index]
    writing = content.encode('utf-8')
    append_to_file(file_path, writing)

append_to_file(file_path, 'created by delicmakaveli'.encode('utf-8'))
print('Done.')
print('Your ANSWERS are saved in Quora Answers/my_answers.txt')
