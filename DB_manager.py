from pymongo import MongoClient
from datetime import datetime
import pickle

db_password = ''  # Enter DB Password HERE
cluster = MongoClient(f'mongodb+srv://admin:{db_password}@cluster0.bcv6e.mongodb.net',
                      serverSelectionTimeoutMS=15 * 1000)  # Timeout for each finding / updating

db = cluster['users']
collection = db['users']


def sign_up(name, email, preferred_color):
    email = email.lower()
    # if user exists, return
    try:
        user = collection.find_one({'email': email})
        if user is None:
            collection.insert_one({'name': name,
                                   'email': email,
                                   'preferred_color': preferred_color,
                                   'daily_emotions': []})
            return True
        else:
            return False
    except:
        pass


def exists(name, email, preferred_color):
    user = collection.find_one({'name': name, 'email': email, 'preferred_color': preferred_color})
    return user is not None


def sign_in(email):
    email = email.lower()
    try:
        user = collection.find_one({'email': email})
        if user:
            return {'name': user['name'],
                    'email': user['email'],
                    'preferred_color': user['preferred_color']}
    except:
        pass


def insert_emotion(email, emotion):
    email = email.lower()
    try:
        user = collection.find_one({'email': email})
        if user is None:
            return
        serialized_emotion = serialize(emotion)
        collection.update_one(user, {'$push': {'daily_emotions': serialized_emotion}})
    except:
        pass


def get_user_daily_emotions(email):
    try:
        user = collection.find_one({'email': email})
        if user is None:
            return

        all_emotions = list(map(lambda serialized_emotion: deserialize(serialized_emotion), user['daily_emotions']))
        date_today = datetime.now().date()
        updated_emotions = list(filter(lambda emotion: emotion.get_creation_date() == date_today, all_emotions))

        # Insert updated emotions
        if len(all_emotions) != len(updated_emotions):
            serialized_updated_emotions = list(map(lambda emotion: serialize(emotion), updated_emotions))
            collection.update_one(user, {'$set': {'daily_emotions': serialized_updated_emotions}})
        return updated_emotions
    except:
        pass


def serialize(obj):
    return pickle.dumps(obj)


def deserialize(obj):
    return pickle.loads(obj)
# print(insert_emotion('edenroz12@gmail.com', MyEmoji.Happy('emojis_images/happy.png')))
# print(get_user_daily_emotions('edenroz12@gmail.com'))
