from mycroft import MycroftSkill, intent_file_handler


class TestPauseTts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tts.pause.test.intent')
    def handle_tts_pause_test(self, message):
        self.speak_dialog('tts.pause.test')


def create_skill():
    return TestPauseTts()

