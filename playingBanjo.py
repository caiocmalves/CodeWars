def are_you_playing_banjo(name):
    if name.lower().find('r') == 0:
        return name + ' plays banjo'
    else:
         return name + ' does not play banjo'