def song_decoder(song):
    song = song.split("WUB")
    while song.count('') != 0:
        song.remove('')
    return ' '.join(song)




print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
  # =>  WE ARE THE CHAMPIONS MY FRIEND
