"""
Test TaylorAlbums class
"""
from unittest import TestCase

from app.taylors_albums import TaylorAlbums


class TestTaylorsAlbums(TestCase):
    def setUp(self):
        self.taylor_albums = TaylorAlbums()

    def test_get_album_WHEN_value_lower_than_one_RETURNS_invalid_album(self) -> None:
        album_number = -1

        result = self.taylor_albums.get_album(album_number)

        self.assertEqual("You're kidding me, right", result)

    def test_get_album_WHEN_value_is_valid_RETURNS_valid_album(self) -> None:
        album_number = 3

        result = self.taylor_albums.get_album(album_number)

        self.assertEqual("Speak Now was the #3 Taylor Swift album!", result)

    def test_get_album_WHEN_value_is_higher_than_current_albums_RETURNS_invalid_album(
        self,
    ) -> None:
        album_number = 11

        result = self.taylor_albums.get_album(album_number)

        self.assertEqual("She didn't record it that far", result)
