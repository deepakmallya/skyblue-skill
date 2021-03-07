from mycroft import MycroftSkill, intent_file_handler


class Skyblue(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skyblue.intent')
    def handle_skyblue(self, message):
        self.speak_dialog('skyblue')


def create_skill():
    return Skyblue()

