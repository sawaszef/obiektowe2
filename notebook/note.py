import datetime


class Note:

    notes_counter = 0

    def __init__(self, text, tag):
        self._text = text
        self._tag = tag
        self._date = datetime.datetime.now()
        self.id = Note.notes_counter
        Note.notes_counter += 1

    @property
    def text(self):
        return self._text

    @property
    def tag(self):
        return self._tag

    @text.setter
    def text(self, new_text):
        self._text = new_text

    @tag.setter
    def tag(self, new_tag):
        self._tag = new_tag

    def match(self, user_input):
        if user_input in self._text or user_input in self._tag:
            return True
        return False

    def __str__(self):
        return f"{self.id}: {self._text}. #{self._tag} {self._date}"
