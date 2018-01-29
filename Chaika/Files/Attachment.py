import os
import random


class Attachment:
    def __init__(self, directory, action, function):
        self.directory = directory
        self.action = action
        self.function = function

    def send(self, message, bot):
        all_files_in_directory = os.listdir(self.directory)
        print(all_files_in_directory)
        random_file = random.choice(all_files_in_directory)
        file = open(self.directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, self.action)
        function()
        file.close()
