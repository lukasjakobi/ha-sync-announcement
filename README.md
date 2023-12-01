# Home Automation TTS Script

This repository contains a script for [Home Assistant](https://www.home-assistant.io/) that enables text-to-speech (TTS) messaging across multiple media player entities. It offers features like caching, language selection, volume control, and the ability to reset volume after message delivery.

## Badges

[![GitHub issues](https://img.shields.io/github/issues/lukasjakobi/ha-sync-announcement)](https://github.com/lukasjakobi/ha-sync-announcement/issues)
[![GitHub forks](https://img.shields.io/github/forks/lukasjakobi/ha-sync-announcement)](https://github.com/lukasjakobi/ha-sync-announcement/network)
[![GitHub stars](https://img.shields.io/github/stars/lukasjakobi/ha-sync-announcement)](https://github.com/lukasjakobi/ha-sync-announcement/stargazers)
[![GitHub license](https://img.shields.io/github/license/lukasjakobi/ha-sync-announcement)](https://github.com/lukasjakobi/ha-sync-announcement/blob/master/LICENSE)

## Inputs

| Input           | Type    | Description                                                                             |
| --------------- | ------- | --------------------------------------------------------------------------------------- |
| `media_players` | List    | List of media player entities to which the TTS message will be sent.                    |
| `message`       | String  | The text-to-speech message to be played.                                                |
| `cache`         | Boolean | Optional. Enables or disables caching of the TTS message (default: `True`).            |
| `language`      | String  | Optional. Sets the language of the TTS message (default: `'en-US'`).                       |
| `volume`        | Float   | Optional. Specifies a volume level for the message (min: 0, max: 1, default: not set).  |
| `volume_reset`  | Boolean | Optional. Resets the volume to its previous state after the message (default: `False`). |

## Usage

To use this script in your Home Assistant environment, follow these steps:

1. **Installation:**
   - Download the `sync_announcements.py` file.
   - Copy the file into the `homeassistant/python_scripts` folder in your Home Assistant installation.

2. **Running the Script:**
   - Create a service call within Home Assistant to execute the script. 
   - You can do this by going to the 'Developer Tools' section, selecting 'Services', and configuring the service call as follows:

     ```yaml
     service: python_script.sync_announcement
     data:
       media_players:
         - media_player.speaker_1
         - media_player.speaker_2
         - media_player.speaker_3
       message: "Hello World"
       volume: 0.3
     ```

   - This service call will play the message "Hello World" at a volume level of 0.3 (30%) on the specified media players.

Feel free to adjust the `media_players`, `message`, and `volume` in the service call to suit your specific setup and needs.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## Contact

Lukas Jakobi - lukas@jakobi.io

Project Link: [https://github.com/lukasjakobi/ha-sync-announcement](https://github.com/lukasjakobi/ha-sync-announcement)
