
class Emotion:
    def __init__(self, emotionType, intensity):
        self.emotionType = emotionType
        self.intensity = intensity

    def get_info(self):
        return [self.emotionType, self.intensity]