import json
from collections import defaultdict
from datetime import datetime, timedelta

"""
Covert prased chat history in JSON into a txt file for model training. 
"""

if __name__ == "__main__":
    train = defaultdict(list)
    idx = 0
    session_delta = timedelta(minutes=15)
    session_start = None

    with open("history.json", 'r', encoding='UTF-8') as f:
        history = json.load(f)
        for raw_dt, content in history.items():
            dt = datetime.fromisoformat(raw_dt)
            if session_start is None:
                session_start = dt
            if dt - session_start > session_delta:
                session_start = dt
                idx += 1
            train[idx].append(content)
    
    with open("train.txt", 'w', encoding='UTF-8') as f:
        for idx, session in train.items():
            for sent in session:
                f.write(sent + '\n')
            f.write('\n')