# from the code wars challenge: https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python

def song_decoder(song):
    song = ' '.join(song.split('WUB'))
    song = ' '.join(song.split())
    while song[0] == ' ':
        song = song[1:]
    while song[-1] == ' ':
        song = song[:-1]

    return song 