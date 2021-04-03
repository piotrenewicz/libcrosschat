import crosschatbotAPI
import time

# @crosschatbotAPI.attach_text
# def this_is_client_job(message: str, author: str):
#     time.sleep(4)
#     return "Hello, you've contacted client code function!\nUnfortunately we are still under construction.\nLong story short, you're not getting any other response from us today!" + message + author


crosschats = dict()
rooms = dict()
summon = "!"


def create_crosschat(args: list, author, channel, responder):
    if channel in rooms:
        return "You are in crosschat: " + rooms[channel] + " \n" \
                "You can't create other crosschats, while being in one. Try !leave 'ing first"

    if len(args) < 1:
        return "You didn't specify a name for your new crosschat"

    new_crosschat_name = args[0]
    if new_crosschat_name in crosschats:
        return "crosschat with name: " + new_crosschat_name + " already exists!\n" \
                "Choose a different name or join that crosschat instead."

    # creating that crosschat now.
    crosschats[new_crosschat_name] = dict()
    return "Created and " + join_crosschat(args, author, channel, responder)


def destroy_crosschat(args, author, channel, responder):
    if channel in rooms:
        crosschat_to_destroy = rooms[channel]
        send_to_crosschat("User: "+author+" has destroyed this crosschat!\n"
                            "Everyone in here will be automatically ejected!", crosschat_to_destroy, channel)
        for other_channel, send_function in crosschats[crosschat_to_destroy].items():
            del rooms[other_channel]
        crosschats[crosschat_to_destroy].clear()
        del crosschats[crosschat_to_destroy]

        return "Crosschat: "+crosschat_to_destroy+" has been destroyed!"


def join_crosschat(args: list, author, channel, responder):
    if channel in rooms:
        return "You are in crosschat: " + rooms[channel] + " \n" \
                "You can't join other crosschats, while being in one Try !leave 'ing first"

    if len(args) < 1:
        return "You didn't specify which crosschat to join"

    crosschat_to_join = args[0]
    if crosschat_to_join in crosschats:
        rooms[channel] = crosschat_to_join
        crosschats[crosschat_to_join][channel] = responder
        send_to_crosschat("User: "+author+" has joined this crosschat!", crosschat_to_join, channel)
        return "Joined crosschat: " + crosschat_to_join

    return "Crosschat: " + crosschat_to_join + " was not found!\n" \
        "Make sure you didn't make any mistakes, or !create this crosschat"


def leave_crosschat(args, author, channel, responder):
    if channel in rooms:
        crosschat_to_leave = rooms[channel]
        send_to_crosschat("User: "+author+" has left this crosschat", crosschat_to_leave, channel)
        del crosschats[crosschat_to_leave][channel]
        del rooms[channel]
        return "You have left crosschat: "+crosschat_to_leave

    return "You are not in a crosschat!"


def status(args, author, channel, responder):
    if channel in rooms:
        result = "You are in crosschat: "+rooms[channel]
    else:
        result = "You are not in a crosschat"

    selection = list(crosschats.keys())
    result += "\n\nThere are "+str(len(selection))+" crosschats available:\n"
    for name in selection:
        result += name+", "
    return result[:-2]


command_list = {
    "create": create_crosschat,
    "destroy": destroy_crosschat,
    "join": join_crosschat,
    "leave": leave_crosschat,
    "status": status,
}


def parse_command(command, author, channel, responder):
    args = command.split(" ")
    if args[0] in command_list:
        return command_list[args[0]](args[1:], author, channel, responder)
    return "Command \"" + args[0] + "\" not found! Try one of:" + str(list(command_list.keys()))


def send_to_crosschat(message, crosschat_name, except_channel):
    for channel, send_function in crosschats[crosschat_name].items():
        if channel == except_channel:
            continue
        send_function(message)


@crosschatbotAPI.attach_full
def working_with_full_power(platform: str, room_id, message: str, author: str, send):
    channel = (platform, room_id)
    if message.startswith(summon):
        send(parse_command(message[len(summon):], author, channel, send))
        return

    if channel in rooms:
        send_to_crosschat("["+author+"]:\n"+message, rooms[channel], channel)


crosschatbotAPI.begin_backends()