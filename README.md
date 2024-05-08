# BeoTrigger

BeoTrigger is a Python script designed to control GPIO pins based on messages received via MQTT. It utilizes the `gpiozero` library for GPIO control and the `paho.mqtt.client` library for MQTT communication.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [MQTT Message Format](#mqtt-message-format)
- [Logging](#logging)
- [Watchdog Mechanism](#watchdog-mechanism)
- [Contributing](#contributing)
- [License](#license)

## Features

- Listens for MQTT messages on specified topics and triggers GPIO pin states accordingly.
- Supports multiple MQTT topics for different control scenarios.
- Implements a watchdog mechanism to ensure the script is running properly.

## Requirements

- Python 3.x
- `gpiozero` library (`pip install gpiozero`)
- `paho-mqtt` library (`pip install paho-mqtt`)
- `sdnotify` library (`pip install sdnotify`)

## Usage

1. Install the required Python libraries using pip:

   ```bash
   pip install gpiozero paho-mqtt sdnotify
   ```

2. Configure the script by modifying the variables in the script file according to your setup:
   - `GPIO_PIN`: The GPIO pin number you want to control.
   - `MQTT_BROKER`: The IP address or hostname of your MQTT broker.
   - `MQTT_PORT`: The port number on which your MQTT broker is running.
   - `TOPIC_A`, `TOPIC_B`: The MQTT topics to subscribe to for message reception.
   - `WATCHDOG_CONFIG`: Configuration for the watchdog mechanism.

3. Run the script:

   ```bash
   python beotrigger.py
   ```

## MQTT Message Format

The script expects MQTT messages in specific formats to trigger GPIO actions:
- `00.80`: Turn on GPIO pin (e.g., TV).
- `00.60`, `00.64`: Turn on GPIO pin (e.g., Volume Up, Volume Down).
- `00.0C`: Turn off GPIO pin (e.g., Standby).
- `00.36`: Stop GPIO pin action.
- `TIMER.SHORT`: Trigger a short timer action.
- `TIMER.LONG`: Trigger a long timer action.

## Logging

The script logs events and errors to both console and a log file located at `/home/styppen/beotrigger/beotrigger.log`.

## Watchdog Mechanism

BeoTrigger implements a watchdog mechanism using the `sdnotify` library to notify systemd about the script's status. This ensures that the script continues to run and remains responsive.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

