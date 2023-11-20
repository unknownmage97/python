

class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        sets default values for power, mute, volume, and channel
        '''
        self.__status = False
        self.__muted = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        '''
        changes the status of the TV to be on(true) or off(false)
        '''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def mute(self) -> None:
        '''
        changes if the TV is muted(true) or is not muted(false)
        '''
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            elif self.__muted == True:
                self.__muted = False

    def channel_up(self) -> None:
        '''
        increases the TV channel by 1, and loops it to the minimum if already at the max channel number
        '''
        if self.__status == True:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        decreases the TV channel by 1, and loops it to the maximum if already at the min channel number
        '''
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        increases the channel volume by 1, or keeps it at the max volume if already there
        '''
        self.__muted = False
        if self.__status == True:
            self.__volume += 1
            if self.__volume > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME

    def volume_down(self) -> None:
        '''
        decreases the channel volume by 1, or keeps it at the min volume if already there
        '''
        self.__muted = False
        if self.__status == True:
            self.__volume -= 1
            if self.__volume < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME

    def __str__(self) -> str:
        '''
        :return: a string containing if the TV is on, the channel number, and the volume
        '''
        if self.__muted == False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'