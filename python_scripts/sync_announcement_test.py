import unittest
from unittest.mock import MagicMock
from sync_announcement import SyncAnnouncement


class TestSyncAnnouncement(unittest.TestCase):
    def test_sync_announcement(self):
        # Mock the hass object
        mock_hass = MagicMock()

        # Mock the data dictionary
        data = {
            'media_players': ['media_player_1', 'media_player_2'],
            'message': 'Test message',
            'cache': True,
            'language': 'en-US',
            'volume': 0.5,
            'volume_reset': True
        }

        # Mock the hass.states.get method
        mock_hass.states.get.return_value.attributes = {'volume_level': 0.3}

        # Create an instance of SyncAnnouncement
        sync_announcement = SyncAnnouncement(mock_hass, data)

        # Call the run method
        sync_announcement.run()

        # Assert that the hass.services.call method was called
        # with the expected arguments
        mock_hass.services.call.assert_any_call('media_player', 'volume_set', {
            'entity_id': data['media_players'],
            'volume_level': data['volume'],
        })
        mock_hass.services.call.assert_any_call('tts', 'cloud_say', {
            'entity_id': data['media_players'],
            'message': data['message'],
            'cache': data['cache'],
            'language': data['language'],
        })
        mock_hass.services.call.assert_any_call('media_player', 'volume_set', {
            'entity_id': data['media_players'][0],
            'volume_level': 0.3,
        })


if __name__ == '__main__':
    unittest.main()
