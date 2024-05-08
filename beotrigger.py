from gpiozero import OutputDevice
import paho.mqtt.client as mqtt
import time
import logging
import sdnotify

# Set up GPIO using gpiozero
GPIO_PIN = 16
gpio_pin = OutputDevice(GPIO_PIN)

# MQTT settings
MQTT_BROKER = "192.168.1.30"
MQTT_PORT = 1883
TOPIC_A = "beo/bridge/out"
TOPIC_B = "beo/eye/out"
WATCHDOG_CONFIG = "watchdog/beostream"

# Callback when a message is received
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8").strip()
    logger.info(f"Received message on topic {message.topic}: {payload}")

    # ON = 00.80, OFF = 00.0C
    if payload == "00.80": # TV
        gpio_pin.on()
    elif payload == "00.60": # VOL UP
        gpio_pin.on()
    elif payload == "00.64": # VOL DOWN
        gpio_pin.on()
    elif payload == "00.0C": # STDBY
        gpio_pin.off()
    elif payload == "00.36": # STOP
        gpio_pin.off()

    if payload == "TIMER.SHORT":
        gpio_pin.on()
    elif payload == "TIMER.LONG":
        gpio_pin.off()

def init_logging():
    # Configure logging
    logger = logging.getLogger('main')
    logger.setLevel(logging.INFO)
    log_handlers = [logging.StreamHandler(), logging.FileHandler('/home/styppen/beotrigger/beotrigger.log')]
    log_formatter = logging.Formatter('%(asctime)s %(levelname)-6s %(message)s')
    for handler in log_handlers:
        handler.setFormatter(log_formatter)
        logger.addHandler(handler)

    logger.info('Logger initalised')
    return logger    

logger = init_logging()



# Set up MQTT client
client = mqtt.Client("Beotrigger")
client.on_message = on_message

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Subscribe to topics
client.subscribe(TOPIC_A)
client.subscribe(TOPIC_B)

# start mqtt client in a different thread
client.loop_start()

# Watchdog mechanism via sd_notify API
sd_notify = sdnotify.SystemdNotifier()
sd_notify.notify("READY=1")
timeout = 10
while True:
    sd_notify.notify("WATCHDOG=1")
    logger.debug("Watchdog kick.")
    time.sleep(timeout)


