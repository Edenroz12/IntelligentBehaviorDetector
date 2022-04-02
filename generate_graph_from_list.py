import os

import matplotlib.pyplot as plt
from collections import Counter

from DB_manager import get_user_daily_emotions
import generate_random_id

UPLOAD_FOLDER = './upload'


def generate_graph(name,email):
    emotions_list = get_user_daily_emotions(email)
    emotions_only_list = list(map(lambda emotion: emotion.get_name(), emotions_list))
    data = Counter(emotions_only_list)
    emotions = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10, 7))

    # creating the bar plot
    plt.bar(emotions, values, width=0.3)

    plt.xlabel("Emotions")
    plt.ylabel("Count")
    plt.title(f"{name}'s Graph")
    rand_id = generate_random_id.generate_id(8)
    path = os.path.join(UPLOAD_FOLDER, rand_id + '.png')
    plt.savefig(path)

    return path
