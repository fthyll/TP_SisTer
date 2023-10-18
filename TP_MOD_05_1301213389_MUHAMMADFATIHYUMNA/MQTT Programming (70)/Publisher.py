import paho.mqtt.client as mqtt
import time

# Inisialisasi MQTT client
client = mqtt.Client("Publisher")

# Koneksi ke broker Adafruit IO
client.username_pw_set(username="fthyll", password="aio_OYaQ94OgGGufPDrPAk8kv1qw01Mu")  # Gantilah dengan kunci AIO Anda
client.connect("io.adafruit.com", 1883)  # Alamat broker Adafruit IO

# Mulai loop untuk mengirim pesan
client.loop_start()

while True:
    # Dapatkan waktu saat ini
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Publish waktu ke feed "TPMOD5"
    client.publish("fthyll/feeds/TPMOD5", current_time)  # Pastikan feed dan nama pengguna sesuai
    print(f"Publisher mempublish waktu: {current_time}")

    # Tunggu 10 detik sebelum mempublish waktu berikutnya
    time.sleep(10)

# Loop terus menerus
client.loop_forever()
