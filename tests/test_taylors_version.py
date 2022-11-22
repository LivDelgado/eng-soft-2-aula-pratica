"""
Test TaylorsVersion class
"""
from unittest import TestCase

from app.taylors_version import TaylorsVersion


class TestTaylorsVersion(TestCase):
    def setUp(self):
        self.taylors_version = TaylorsVersion()

    def test_get_taylors_version_WHEN_invalid_album_RETURNS_invalid_album_message(
        self,
    ) -> None:
        album = "Pure Heroine"

        result = self.taylors_version.get_taylors_version(album)

        self.assertEqual("This album does not exist, what is that??", result)

    def test_get_taylors_version_WHEN_valid_album_with_re_recording_RETURNS_valid_album_message(
        self,
    ) -> None:
        album = "Fearless"

        result = self.taylors_version.get_taylors_version(album)

        self.assertEqual("Yes, the album Fearless was re-recorded!", result)

    def test_get_taylors_version_WHEN_valid_album_without_re_recording_RETURNS_valid_album_message(
        self,
    ) -> None:
        album = "Evermore"

        result = self.taylors_version.get_taylors_version(album)

        self.assertEqual(
            "This album was not re-recorded. Maybe it is already hers! Otherwise, just sit and wait.",
            result,
        )
