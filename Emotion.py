
class Emotion:
    def __init__(self, id, emotionType, intensity):
        self.id = id
        self.emotionType = emotionType
        self.intensity = intensity

    def get_info(self):
        return [self.id, self.emotionType, self.intensity]