# libcrosschatrepo

This is a python module allowing you to create one chatbot and deploy it on multiple platforms.

Currently implemented platforms are:
Discord, Facebook Messenger, Telegram.

###### Table of Contents:
 - [What is this thing?](#whaaa??)
 - [How to install it?](#howinstall)
 - [How to make a bot with this?](#howuse)
 - [How to Deploy a bot with this?](#howdeploy)
 - [Creating a new backend](#moar_platforms)
 - [DevLog](#devlog)

<a name="whaaa??"/>

## Introduction

This project was developed as part of team programming class,  
in Applied Informatics degree at the University of Silesia.  

The aim of this project is to enable a single chatbot implementation and deployment to work with multiple chat platforms.
Write your bot once, and have it talk to humans through any of the supported chats.  

This is achieved by running several normal "bots" *(reffered to as **backends**)* concurrently with multithreading  
and having each backend call your function when it is asked something. 

<a name="howinstall"/>

## Steps to get this module set up
This is not available through pip, maybe it will be when i figure out how to release there.

1.create a venv if you don't have one already  
`python3 -m venv ./venv`

2.activate your venv  
`source venv/bin/activate`

3.get this package   
`pip install git+https://github.com/piotrenewicz/libcrosschatrepo.git#egg=libcrosschat`

4.get pymessenger (auto setup installs a bugged version)  
`pip install git+https://github.com/davidchua/pymessenger.git#egg=pymessenger`
you want pymessenger==1.0.0, not 0.0.7.0

<a name="howuse"/>

## Steps to implement your own bot using this module.
You need to do 3 things:  
1.Import the module  
2.define the function  
3.pass control.  

example:
```python
import crosschatbotAPI

@crosschatbotAPI.attach_text
def the_function(message: str, author: str):
    return "response"
  
crosschatbotAPI.begin_backends()
```
this is enough to make a bot that answers: "response" to everyting it is asked. 

Notice the decorator `@crosschatbotAPI.attach_text`  
using it you can mark your function to be used by backends for turning incoming messages into responses.  
When function is marked this way it needs to take two arguments (strings) which will be text recieved from a chat user, and that user's name or nick.
It also needs to return a string that will be sent back to that user.

After you're done defining your functions, at the end of your file call `crosschatbotAPI.begin_backends()`  
this will create threads for configured backends, start the messages flowing, and lock the main thread, to prevent the program from ending.

Have a look at `user_code_simple_demo.py` to see this in action.

#### About more advanced bots
The function described above is limiting you to responding once, when a user starts a conversation. 
If you need the ability to send multiple messages per user query, respond later at a given time or event, or keep track of conversation continuity and context. 
`@crosschatbotAPI.attach_full` is for you.

```python
@crosschatbotAPI.attach_full
def working_with_full_power(channel_id, message: str, author: str, send):
    if message.startswith(summon):
        send(parse_command(message[len(summon):], author, channel_id, send))
        return

    if channel_id in rooms:
        send_to_crosschat("["+author+"]:\n"+message, rooms[channel_id], channel_id)

```
This is the main piece of code from `user_code_crosschat_demo.py`  
By marking a function with `@crosschatbotAPI.attach_full`, that function needs to take a few arguments:
`channel_id` is a tuple that uniquely identifies the source of a conversation.  
`channel_id` contains `(Platform: str, chat_id: str)`, where `chat_id` is an identifier of the chatroom within a platform. Supplied by that platform itself. 
Now it could happen that two different platforms reported the same chat_id for two different chatrooms.   
To avoid that collision, theres `Platform: str` set to one of: `"DC", "FB", "TG"`. This has a nice side effect of giving you an idea which platform provided the message

`message: str, author: str` same as with simple function this is text sent by chat user, and his nick.  
`send` this is a callback function allowing you to send text to that chatroom at any time. `send("response")`

It's a good idea to store this information and callback for use later, and return from this function as fast as you can.
As it is untested wheather all backends are able to process new messages while this function is blocking.  

Lastly you need to pass control into the backends, but depending on what you're doing you may want control of the main thread back while backends operate.
For this reason you can call `crosschatbotAPI.begin_backends(blocking=False)`.  
Just like before this will create threads for backends, and set things in motion. But with blocking set to False, it will not lock the main thread, and instead return control to your code. You'll need to handle keeping the thread alive as ending the main thread stops everything.

If you don't need control over main thread you can just call `crosschatbotAPI.begin_backends()` as before.
For an extensive demo of capabilities of this function see:`user_code_crosschat_demo.py`


<a name="howdeploy"/>

## Steps to get your bot on all the supported platforms.
filler

filler

filler
filler
filler

filler

filler
filler
filler

filler

filler
filler
filler

filler

filler
filler

<a name="moar_platforms"/>

## Guide to creating a backend, and contributing to this project.
filler

filler

filler
filler
filler

filler

filler
filler
filler

filler

filler
filler

<a name="devlog"/>

## DevLog
filler

filler

filler
filler
filler

filler

filler
filler


%peter

%konrad

%mykhailo 

