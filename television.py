

class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self):
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            elif self.__muted == True:
                self.__muted = False

    def channel_up(self):
        if self.__status == True:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        self.__muted = False
        if self.__status == True:
            self.__volume += 1
            if self.__volume > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        self.__muted = False
        if self.__status == True:
            self.__volume -= 1
            if self.__volume < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME

    def __str__(self):
        if self.__muted == False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
