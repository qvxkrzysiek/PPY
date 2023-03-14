import vlc
__import__('pprint').pprint("Podaj sciezke do pliku:")
p = vlc.MediaPlayer(input())
p.play()
