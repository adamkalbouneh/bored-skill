from mycroft import MycroftSkill, intent_file_handler


class Bored(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bored.intent')
    def handle_bored(self, message):
        self.speak_dialog('bored')


def create_skill():
    return Bored()

