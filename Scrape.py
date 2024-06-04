from bs4 import BeautifulSoup
import requests
 
page_to_scrape = requests.get("https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python/6581949#6581949")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
  
div = soup.find('div', id="question")
if div:
    # Find the <p> inside the <div>
    p = div.find('p')
    if p:
        print(p.text)
    else:
        print('No <p> found inside the <div>.')
else:
    print('No <div> with the specified class found.')
      
answers_div = soup.find('div', id="answers")
if answers_div:
    # Find all answer divs
    answer_divs = answers_div.find_all('div', class_='answer', limit=3)
    if answer_divs:
        for index, answer_div in enumerate(answer_divs):
            print(f"Answer {index + 1}:")
            # Print the text of all <p> tags inside each answer div
            paragraphs = answer_div.find_all('p')
            if paragraphs:
                for p in paragraphs:
                    print(p.text)
            else:
                print('No <p> found inside this answer <div>.')
            print()  # Print a newline for better readability
    else:
        print('No <div> with class="answer" found inside the answers <div>.')
else:
    print('No <div> with id="answers" found.')