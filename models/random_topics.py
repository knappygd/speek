#!/usr/bin/env python3
import random

topics = {
    0: "Travel",
    1: "Food",
    2: "Sports",
    3: "Technology",
    4: "Movies",
    5: "Music",
    6: "History",
    7: "Fashion",
    8: "Nature",
    9: "Art",
    10: "Politics",
    11: "Science",
    12: "Books",
    13: "Friendship",
    14: "Health",
    15: "Education",
    16: "Social Media",
    17: "Culture",
    18: "Work",
    19: "Hobbies",
    20: "Animals",
    21: "Parties",
    22: "Religion",
    23: "Economy",
    24: "Environment"
}


def random_topics():
    select_topic = ""

    random_number = random.randint(0, len(topics))
    select_topic = topics[random_number]
    print(select_topic)


if __name__ == "__main__":
    random_topics()
