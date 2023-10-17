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
(
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
) This is not of the project but it is a example.

#### `models/` directory contains classes used for this project:
[Chat.py](/models/Chat.py) - The Chat class is where all chat methods are located.
* `def create_chat(self)` - Create a chat with two differents users.
* `def delete_chat(self)` - Delete a chat that was created before.
* `def search_chat(User, User)` - Search for all Chat class and return the one who have both Users.

[Lenguages.py](/models/Lenguages.py) - The Lenguages class is where all lenguages methods are located.
* `def list_lenguages(self)` - Show the list of all lenguages.

[Message.py](/models/Message.py) - The Message class is where all messages methods are located.
* `def send_message(self)` - Send a new message to the other user in the chat and save it on the list of messages.

[Topic.py](/models/Topic.py) - The Topic class is where all topics methods are located.
* `def topic_dict(self)` - Show random topics of a dict.

[User.py](/models/User.py) - The User class is where all user methods are located.
* `def create_user(self)` - Create a user with all his attributes.
* `def mod_user(self)` - Modifie some attribute of a User.
* `def del_user(self)` - Delete a user.
* `def invite(self, username)` - Send a recuest to some user to be friends.
* `def list_friends(self)` - Show all user friend.
* `def change_status(self)` - Modifie the User status.
* `def del_friend(self, username)` - Delete friend from user friends.
* `def block_user(self, username)` - Add user to a block list.
* `def report_user(username, reason)` - Add a report to the user report.
* `def search_user(username)` - Search for a user in the database.
* `def list_random_chat(self)` - Show all user in random list.
* `def login(self, email, password)` - Log to the User who has this attributes.

#### `/tests` directory contains all unit test cases for this project:
[/test_chat.py](/tests/test_chat.py) - Contains the TestChat classes.
* `def Test_chat_id(self)`- Set up and test of id.
* `def Test_start_chat(self)` - Start a new chat and test it.


## Examples of use
``` algo va aca!!!!!! ```

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
