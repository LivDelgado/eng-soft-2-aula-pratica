class TaylorsVersion:
    _TAYLORS_VERSIONS = {
        "Debut": False,
        "Fearless": True,
        "Speak Now": False,
        "Red": True,
        "1989": False,
        "Reputation": False,
        "Lover": False,
        "Folklore": False,
        "Evermore": False,
        "Midnights": False,
    }

    def get_taylors_version(self, album: str) -> str:
        """
        returns information about the re-recording of the given album
        """
        re_recording = self._TAYLORS_VERSIONS.get(album)

        if re_recording is None:
            return "This album does not exist, what is that??"

        if re_recording is True:
            return f"Yes, the album {album} was re-recorded!"

        return "This album was not re-recorded. Maybe it is already hers! Otherwise, just sit and wait."
