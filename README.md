![Baner](https://github.com/knappygd/speek/assets/124533439/eee38298-949e-4c4e-b3df-0e4626aaaa78)

# Speek
This repository represents our final project at Holberton School, where we intend to apply the comprehensive range of skills acquired throughout our course. From our proficiency in both soft skills and programming, encompassing both backend and frontend development, we have created a web platform. Our platform caters to individuals seeking to practice and enhance their language skills, offering a space for language practice and improvement rather than formal language learning.
#### How it works?
This website is tailored to serve as a chat platform connecting individuals worldwide who share an interest in practicing the same language. Upon registration, a new account will be created in our database, granting you access to the main page. Here, you have the flexibility to engage in various activities, such as chatting with random users who share your linguistic interests, or reaching out to friends you've connected with.
#### Functionalities of this web:
* Create new account.
* Chat with friend.
* Chat with random user.
* Chat with SpeekBot.
## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/knappygd/speek.git"`
* Access Speek directory: `cd speek`
* ............

## File Descriptions
``` ALGO VA ACA!!!!!! ```

#### `models/engine/` directory contains methods used for this project:
* `def delete_user(ex_user: str)` - Delete a user.
* `def modify_user()` - Modify a user.
* `def invite(user_name: str, new_friend: str)` - Lets a user send a friend request.
* `def list_friends(user_name: str)-> List[Dict]` - List the friends of a user.
* `def change_status(user_name: str)` - Let the user can change their status.
* `def del_friednf(user: str, exFriend: str)` - Let a user to erase a friend of their friend list.
* `def block_user(user_name: str)` - Let a user to block them so they will not be able to talk any longer.
* `def report_user(reported: str)` - Sends a report to another user for misbehavior or some inapropiated behavior.
* `def search_user(user_name: str) -> Dict` - Search for a user.
* `def list_random_chat(user_name: str)` - Lists all your active random chats.
* `def login(user_name: str, password: str)` - Verify the identity of the user an allow them to use the page.
* `def send_message(sender: str, receiver: str, content: str)` - Let an user will be able to send a message to another user.
* `def create_chat(User1: str, user2: str)` - Create a chat.
* `def delete_chat(chat_id)` - Delete a chat when they finish their talk.
* `def search_chat(user_name: str)-> Dict` - Looks for a chat a specific chat.
* `def dictionary_topics()-> Dict` - Returns a dictionary with all the topics.
* `def list_languages()-> List(str)` - Returns a list with all the languages supported by speek.
* `def list_languages(user_name: str)-> List(str)` - Returns a list with all the languages of the user.

#### `/tests` directory contains all unit test cases for this project:
[/test_chat.py](/tests/test_chat.py) - Contains the TestChat classes.
* `def Test_chat_id(self)`- Set up and test of id.
* `def Test_start_chat(self)` - Start a new chat and test it.

## Architecture
Back-End: 
* Django
* SupaBase

Front-End:
* Java-Script
* React

External API's:
* Chat GPT API

## Examples of use
``` ALGO VA ACA!!!!!! ```

## Bugs
No known bugs at this time.

## Authors
* Lucas Soria - Front-End and UX/UI Designer - [Github](https://github.com/lucassoriabusto).
* Mishel Tomas - Front-End - [Github](https://github.com/Mishel450).
* Emilio Damasco - Back-End - [Github](https://github.com/knappygd).
* Leonardo Rodriguez - Full-Stack - [Github](https://github.com/LeoRod17).
* Guillermo Vega - Full-Stack and Project Manager - [Github](https://github.com/Korchea).

## License
Public Domain. No copy write protection. 
