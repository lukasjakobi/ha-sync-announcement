# Sync Announcement - Home Assistant TTS Script

![GitHub release (with filter)](https://img.shields.io/github/v/release/lukasjakobi/ha-sync-announcement)
[![GitHub license](https://img.shields.io/github/license/lukasjakobi/ha-sync-announcement)](https://github.com/lukasjakobi/ha-sync-announcement/blob/master/LICENSE)

This repository contains a [Home Assistant](https://www.home-assistant.io/) [Python Script](https://www.home-assistant.io/integrations/python_script/) that enables text-to-speech (TTS) messaging across multiple media player entities. It offers features like caching, language selection and volume control (including automatically resetting the volume after the announcement to the previous state).

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=lukasjakobi&repository=ha-sync-announcement&category=automations)

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

## Inputs

| Input           | Type    | Description                                                                             |
| --------------- | ------- | --------------------------------------------------------------------------------------- |
| `media_players` | List    | List of media player entities to which the TTS message will be sent.                    |
| `message`       | String  | The text-to-speech message to be played.                                                |
| `language`      | String  | Optional. Sets the language of the TTS message (default: `'en-US'`).                       |
| `volume`        | Float   | Optional. Specifies a volume level for the message (min: 0, max: 1, default: `None`).  |
| `volume_reset`  | Boolean | Optional. Resets the volume to its previous state after the message (default: `True`). |
| `cache`         | Boolean | Optional. Enables or disables caching of the TTS message (default: `True`).            |

## Usage

To use this script in your Home Assistant environment, you can either download it manually or install it via a custom repository in HACS

### Installation via HACS Custom Repository

- Go to HACS in your Home Assistant interface.
- Navigate to the "Automations" section.
- Click the three dots in the top right corner and select "Custom repositories."
- Enter `https://github.com/lukasjakobi/ha-sync-announcement` into the "Repository" field.
- Choose `Python Script` as the category and click "Add."
- The repository will appear in you automations overview, click on the repository and install it via the button on the bottom right
- Run the service `python_script.reload` or restart your Home Assistant instance

### Manual Installation

- Download the `sync_announcements.py` file.
- Copy the file into the `homeassistant/python_scripts` folder in your Home Assistant installation.
- Run the service `python_script.reload` or restart your Home Assistant instance

### Enabling UI support

- Download the `services.yaml` file.
- Add the file content into the `homeassistant/python_scripts/services.yaml` file, create the file if it is not present.
- Run the service `python_script.reload` or restart your Home Assistant instance

## Running the Script
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
