import bs4
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from typing import Tuple, List

"""
A simple parser that coverts chat history from Telegram to organized JSON.
"""


def parse_text(x: bs4.element.Tag) -> Tuple[str, str]:
    """
    Parses a single message from the HTML file.
    """
    # Get the timestamp
    raw_timestamp = x.find('span', {'class': 'details'})
    # Get the message text
    raw_content = x.find('div', {'class': 'text'})

    timestamp = raw_timestamp.text.strip() if raw_timestamp else ""
    content = raw_content.text.strip() if raw_content else ""
    return timestamp, content


def timestamp_to_datetime(timestamp: str, offset=0) -> str:
    """
    Converts a timestamp to a datetime.
    """
    raw_date, raw_time = timestamp.split(' ')
    date = raw_date.split('.')
    time = raw_time.split(':')
    assert len(date) == len(time) == 3

    day, month, year = date
    hour, minute, second = time
    dt = datetime.fromisoformat(f"{year}-{month}-{day} {hour}:{minute}:{second}")
    dt += timedelta(seconds=offset)
    return dt.isoformat()


def add_entries(corpus_dict: dict, history: List[Tuple[str, str]]) -> None:
    """
    Adds a new entry to the corpus dictionary.
    """
    for raw_timestamp, content in history:
        if raw_timestamp and content:
            timestamp = timestamp_to_datetime(raw_timestamp)
            if timestamp in corpus_dict:
                print(f"Duplicate timestamp: {timestamp}")
                print(f"Previous: {corpus_dict[timestamp]}")
                print(f"New: {content}")
                corpus_dict[timestamp_to_datetime(raw_timestamp, offset=1)] = content
            else:
                corpus_dict[timestamp_to_datetime(raw_timestamp)] = content


if __name__ == '__main__':
    file_names = ["messages.html", "messages2.html"]
    corpus_dict = {}

    for name in file_names:
        with open(name, 'r', encoding='UTF-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            forwarded_body = soup.find_all('div', class_='forwarded body')
            corpus = [parse_text(x) for x in forwarded_body]
            add_entries(corpus_dict, corpus)
    
    with open('history.json', 'w', encoding='UTF-8') as f:
        json.dump(corpus_dict, f, ensure_ascii=False)
