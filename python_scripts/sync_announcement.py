class SyncAnnouncement:
    def __init__(self, hass, data):
        self.hass = hass
        self.data = data

    def run(self):
        # Extracting data
        media_players = self.data.get('media_players')
        message = self.data.get('message')
        cache = self.data.get('cache', True)
        language = self.data.get('language', 'en-US')
        volume = self.data.get('volume')
        volume_reset = self.data.get('volume_reset', False)

        states_before_run = {}

        # store the volume level of all media_players
        # before running the script if specified
        if volume_reset:
            for entity_id in media_players:
                states_before_run[entity_id] = (
                    self.hass.states.get(entity_id).attributes['volume_level']
                )

        # set volume to all media_players if specified
        if volume is not None:
            self.hass.services.call('media_player', 'volume_set', {
                'entity_id': media_players,
                'volume_level': volume,
            })

        # send message through tts.cloud_say
        self.hass.services.call('tts', 'cloud_say', {
            'entity_id': media_players,
            'message': message,
            'cache': cache,
            'language': language,
        })

        # set respective previous volume to all media_players if specified
        if volume_reset:
            for entity_id, previous_volume in states_before_run.items():
                self.hass.services.call('media_player', 'volume_set', {
                    'entity_id': entity_id,
                    'volume_level': previous_volume,
                })
