import paho.mqtt.client as mqtt
import threading

# Callback saat pesan diterima
def on_message(client, userdata, message):
    print(f"Pesan diterima pada topik {message.topic}: {message.payload.decode()}")

# Fungsi untuk menjalankan loop pada thread terpisah
def run_mqtt_subscriber():
    client = mqtt.Client("Subscriber")
    client.username_pw_set(username="fthyll", password="aio_OYaQ94OgGGufPDrPAk8kv1qw01Mu")
    client.connect("io.adafruit.com", 1883)  # Alamat broker Adafruit IO
    client.subscribe("fthyll/feeds/TPMOD5")
    client.on_message = on_message
    client.loop_forever()

# Membuat thread untuk menjalankan subscriber
subscriber_thread = threading.Thread(target=run_mqtt_subscriber)
subscriber_thread.daemon = True  # Agar thread berhenti saat program utama berhenti

# Mulai thread subscriber
subscriber_thread.start()

# Program utama tetap dapat menjalankan perintah lain di sini
# Anda dapat menghentikan program dengan menekan Ctrl+C atau menghentikan proses program

try:
    # Ini akan menjaga program utama berjalan
    while True:
        pass
except KeyboardInterrupt:
    print("Program dihentikan.")
