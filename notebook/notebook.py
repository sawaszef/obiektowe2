import note


class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, note_text, note_tag):
        anote = note.Note(note_text, note_tag)
        self.notes.append(anote)

    def modify_text(self, note_id, text):
        self.notes[note_id].text = text

    def modify_tag(self, note_id, tag):
        self.notes[note_id].tag = tag

    def search(self, searched_text):
        result = []
        for anote in self.notes:
            if anote.match(searched_text):
                result.append(anote)
        return result
