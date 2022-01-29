class Song:

    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.params = (
                        ('q', self.name + self.artist),
                        ('rlz', '1C1GCEU_enAE893AE893'),
                        ('oq', self.name + self.artist),
                        ('aqs', 'chrome.0.35i39i355j46i39j0i512l3j0i22i30j69i60l2.7127j0j7'),
                        ('sourceid', 'chrome'),
                        ('ie', 'UTF-8'),
        )

    def __str__(self):
        return f"Song <{self.name} by {self.artist}>"
