
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all(name='section', class_="jobs")
    print(len(jobs))
    for job_section in jobs:
        job_posts = job_section.find_all("li")
        job_posts.pop(-1)  # 마지막 항목 날리기
        # 순서: 하이퍼링크 객체 가져온 후, 링크(a href), 회사, 종류, 지역(span "company"), 제목(span "title") 가져오기
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']
            company, kind, region = anchor.find_all(
                name='span', class_='company')
            title = anchor.find(name='span', class_='title')
            print(company, kind, region, title)
            print('//////////////////////////')

"""
==> 배열의 길이를 알 때, 배열의 각 데이터를 서로 다른 변수에 할당하는 방법
list_of_numbers = [1, 2, 3]
first, second, third = list_of_numbers
print(first, second, third)
"""
