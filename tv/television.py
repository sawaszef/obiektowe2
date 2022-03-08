class Television:

    volumes = [i+1 for i in range(100)]
    channels = [i+1 for i in range(34)]

    def __init__(self):
        self._channel = None
        self._volume = None

    @property
    def channel(self):
        return self._channel

    @property
    def volume(self):
        return self._volume

    @channel.setter
    def channel(self, new_channel):
        if new_channel in Television.channels:
            self._channel = new_channel
        else:
            print("Podano kanal spoza zakresu. (1-34)")

    @volume.setter
    def volume(self, new_volume):
        if new_volume in Television.volumes:
            self._volume = new_volume
        else:
            print("Podano glosnosc spoza zakresu 0-100")

    def __str__(self):
        return f"Kanal: {self._channel}\nGlosnosc: {self._volume}"
