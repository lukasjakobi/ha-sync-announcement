def log_error(logger, message):
    logger.error(f"Sync Announcement: {message}")


try:
    # list of media_player entities
    media_players = data.get('media_players')

    # the message to play
    message = data.get('message')

    # use caching mechanisms
    # optional - true/false, default: true
    cache = data.get('cache') or True

    # specify the language for the tts model
    # optional - default: en-US
    language = data.get('language') or 'en-US'

    # specify a volume to set to all media_players before playing the message
    # optional - min: 0, max: 1, step: 0.01, default: None
    volume = data.get('volume') or None

    # specify if the volume should be reset to the previous state after the
    # tts message
    # optional - true/false, default: false
    volume_reset = data.get('volume_reset') or True

    # store the volume level of all media_players before running the script if
    # specified
    if volume_reset and volume is not None:
        media_player_states_before_run = {}
        for entity_id in media_players:
            media_player_states_before_run[entity_id] = (
                hass.states.get(entity_id).attributes['volume_level']
            )

    # set volume to all media_players if specified
    if volume is not None:
        hass.services.call('media_player', 'volume_set', {
            'entity_id': media_players,
            'volume_level': volume,
        })

    # send message through tts.cloud_say
    hass.services.call('tts', 'cloud_say', {
        'entity_id': media_players,
        'message': message,
        'cache': cache,
        'language': language,
    })

    # set respective previous volume to all media_players if specified
    if volume_reset and volume is not None:
        for entity_id, prev_volume in media_player_states_before_run.items():
            hass.services.call('media_player', 'volume_set', {
                'entity_id': entity_id,
                'volume_level': prev_volume,
            })
except Exception as e:
    log_error("**An unhandled error has occurred.**\n\n{}".format(e))
