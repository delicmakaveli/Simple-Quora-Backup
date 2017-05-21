from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from file_io import *
import textwrap


print('Thank you for using Simple Quora Backup')
print('This will backup your BOOKMARKS to a text file in the simplest form, ')
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
    osType = input('Please type in your operating system (windows, mac, linux)')
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

# print(email + ' ' + password)

numOfScrolls = 0
num = 0

while boolean:
    numOfScrolls1 = input('How many Bookmarks do you have (approximately)?')
    if numOfScrolls1 is not None:
        numOfScrolls = int(numOfScrolls1)
        if numOfScrolls >= 10:
            num = numOfScrolls / 10
        else:
            num = 2
        break


print('NOTE: Saving BOOKMARKS is very slow, because Quora has lazy loading and it forbids scraping.')
print('The program has to manually scroll to load and then expand all the BOOKMARKS')
print('I had 290-300 answers and it took 11-12 minutes so you do the math :)')
print('\n')
print('There is no easy way around this, so go grab a cup of coffee/tea and do something else until this is done')
print('To do this by hand would take you several HOURS, instead this will only take several MINUTES.')
print('\n')
print('Starting Chrome WebDriver...')

browser = webdriver.Chrome(executable_path=path)
browser.get('https://www.quora.com/bookmarked_answers')
browser.maximize_window()
sleep(2)
quoraElems = browser.find_elements_by_xpath("//form/div/div/input")
emailQuora = quoraElems[0]
passwordQuora = quoraElems[1]
emailQuora.send_keys(email)
passwordQuora.send_keys(password)
passwordQuora.send_keys(Keys.RETURN)

sleep(2)
browser.get('https://www.quora.com/bookmarked_answers')
sleep(3)

print('Scrolling to load all BOOKMARKS...')

i = 0
while i < num:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(4)
    i += 1

# identifies answers to be expanded by the '(more)' element
answers = browser.find_elements_by_link_text('(more)')

print('Expanding BOOKMARKS...')

j = 1
for answer in answers:
    if j < len(answers):
        if j == 1:
            browser.execute_script('window.scrollTo(0, 0);')
            ActionChains(browser).click(answers[0]).perform()
            j += 1
        elif j < len(answers) - 1:
            ActionChains(browser).move_to_element(answers[j]).click(answer).perform()
            j += 1
            if j == len(answers) - 1:
                ActionChains(browser).move_to_element(answers[j]).click(answers[j-1]).perform()
                continue
    if j == len(answers) - 1:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        ActionChains(browser).click(answers[j]).perform()
        break
    sleep(2)

# after the scrolling and the clicking is done, the scraping can begin :)
html = browser.page_source
browser.close()
browser = None
soup = BeautifulSoup(html, 'html.parser')

# create the directory and the reading_list text file which has all the content in it
dir_name = 'Quora Reading List'

create_project_dir(dir_name)

create_data_file(dir_name, '')

print('Saving to file (reading_list.txt)...')

count = 1
# iterate through all items in the list
for item_list in soup.find_all('div', {'class': 'PagedList ReadLaterList'}):
    for list_item in item_list.find_all('div', {'class': 'pagedlist_item'}):

        # get question title
        question_title = list_item.find('span', {'class': 'question_text'})
        # In case it's not a question (probably blog post)
        if question_title is None:
            question_title = list_item.find('a', {'class': 'BoardItemTitle'})
        # write the question title to the text file
        content = str(count) + ' QUESTION TITLE: ' + question_title.text
        content1 = textwrap.fill(content, 66)
        writing = content1.encode('utf-8')
        append_to_file('Quora Reading List' + '/reading_list.txt', writing)
        count += 1

        # check for expanded question/answer text
        answer_content = list_item.find('div', {'class': 'ExpandedQText ExpandedAnswer'})

        if answer_content is None:
            # In case it's not an answer (probably a blog post)
            answer_content = list_item.find('span', {'class': 'inline_editor_value'})

            if answer_content is not None:
                rendered_qtext_all = answer_content.find_all('span', {'class': 'rendered_qtext'})
            # In case it's neither
            else:
                continue
        else:
            rendered_qtext_all = answer_content.find_all('span', {'class': 'rendered_qtext'})

        if rendered_qtext_all is not None:
            for piece in rendered_qtext_all:
                plain_text = False

                for element in piece:
                    # check for paragraphs
                    if element.name == 'p':
                        elem = element.attrs
                        if 'qtext_para' in elem['class']:
                            content = element.text
                            content1 = textwrap.fill(content, 66)
                            writing = content1.encode('utf-8')
                            append_to_file('Quora Reading List' + '/reading_list.txt', writing)
                    # check for ordered lists
                    elif element.name == 'ol':
                        ol_elements = element.find_all('li')
                        counter = 1
                        for li in ol_elements:
                            content = str(counter) + ' ' + li.text
                            content1 = textwrap.fill(content, 66)
                            writing = content1.encode('utf-8')
                            append_to_file('Quora Reading List' + '/reading_list.txt', writing)
                            counter += 1
                    # check for code-boxes (which are ordered lists)
                    elif element.name == 'pre':
                        sub_element = element.find('ol', {'class': 'linenums'})
                        if sub_element.name == 'ol':
                            ol_elements = sub_element.find_all('li')
                            counter = 1
                            for li in ol_elements:
                                content = str(counter) + ' ' + li.text
                                content1 = textwrap.fill(content, 66)
                                writing = content1.encode('utf-8')
                                append_to_file('Quora Reading List' + '/reading_list.txt', writing)
                                counter += 1
                    # check for unordered lists
                    elif element.name == 'ul':
                        ul_elements = element.find_all('li')
                        for li in ul_elements:
                            content = li.text
                            content1 = textwrap.fill(content, 66)
                            writing = content1.encode('utf-8')
                            append_to_file('Quora Reading List' + '/reading_list.txt', writing)
                    # check for images
                    elif element.name == 'div':
                        elem = element.attrs
                        if 'qtext_image_wrapper' in elem['class']:
                            writing = 'img source'.encode('utf-8')
                            append_to_file('Quora Reading List' + '/reading_list.txt', writing)
                    # check for HTML breaks
                    elif element.name == 'br':
                        continue
                    # check for plain text
                    else:
                        if element.name == 'hr':
                            continue
                        elif element.name == 'blockquote':
                            content = element.text
                            content1 = textwrap.fill(content, 66)
                            writing = content1.encode('utf-8')
                        elif element.name == 'span':
                            atr = element.attrs
                            if 'qlink_conainer' in atr['class']:
                                content = element.text
                                content1 = textwrap.fill(content, 66)
                                writing = content1.encode('utf-8')
                            else:
                                content = element.text
                                content1 = textwrap.fill(content, 66)
                                writing = content1.encode('utf-8')
                        elif element.name == 'i':
                            content = element.text
                            content1 = textwrap.fill(content, 66)
                            writing = content1.encode('utf-8')
                        elif element.name == 'b':
                            content = element.text
                            content1 = textwrap.fill(content, 66)
                            writing = content1.encode('utf-8')
                        else:
                            content = str(element)
                            content1 = textwrap.fill(content, 66)
                            writing = content1.encode('utf-8')

                        append_to_file('Quora Reading List' + '/reading_list.txt', writing)
                        continue

print('Done.')
print('Your BOOKMARKS are saved in Quora Reading List/reading_list.txt')
