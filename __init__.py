from mycroft import MycroftSkill, intent_handler
from mycroft.audio import wait_while_speaking

class TestPauseTts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('tts.pause.test.intent')
    def handle_tts_pause_test(self, message):
        self.speak_dialog('tts.pause.test.1', wait=True)
        self.speak_dialog('tts.pause.test.2')
        wait_while_speaking()
        self.speak_dialog('tts.pause.test.3')


def create_skill():
    return TestPauseTts()

