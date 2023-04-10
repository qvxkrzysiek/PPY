import vlc
print("Podaj sciezke do pliku:")
p = vlc.MediaPlayer(input())
p.play()
