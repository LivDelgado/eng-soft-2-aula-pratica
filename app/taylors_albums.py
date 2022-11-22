"""
Taylor Swift albums
"""


class TaylorAlbums:
    _TAYLORS_ALBUMS = {
        1: "Debut",
        2: "Fearless",
        3: "Speak Now",
        4: "Red",
        5: "1989",
        6: "Reputation",
        7: "Lover",
        8: "Folklore",
        9: "Evermore",
        10: "Midnights",
    }

    def get_album(self, album_number: int) -> str:
        """
        returns message about the album number
        """
        album = self._TAYLORS_ALBUMS.get(album_number)
        if album:
            return f"{album} was the #{album_number} Taylor Swift album!"

        if album_number < 1:
            return "You're kidding me, right"

        return "She didn't record it that far"
