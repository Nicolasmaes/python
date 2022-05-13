from gtts import gTTS

language = 'fr'


def textToAudio(str):
    audio = gTTS(str, lang=language, slow=False)
    audio.save('speech.mp3')


textToAudio('Bonjour, ce que vous entendez a été généré avec 9 lignes de Python.')
