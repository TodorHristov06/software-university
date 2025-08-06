def start_playing(instance):
    return instance.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


guitar = Guitar()
print(start_playing(guitar))     

children = Children()
print(start_playing(children))
