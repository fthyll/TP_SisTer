Indirect communication adalah jenis komunikasi antara komponen perangkat lunak atau sistem yang tidak berkomunikasi secara langsung, tetapi melalui entitas perantara yang disebut broker atau server pusat. Broker ini berfungsi sebagai perantara yang menerima pesan dari penerbit (publisher) dan mengirimkannya ke pelanggan (subscriber) yang tertarik pada pesan tersebut.

### Cara Kerja Indirect Communication:

1. **Publisher (Penerbit)**: Publisher adalah komponen yang menghasilkan pesan atau data yang akan dibagikan kepada subscriber. Publisher mengirimkan pesan ke broker.

2. **Broker**: Broker adalah entitas perantara yang bertindak sebagai pusat komunikasi. Broker menerima pesan dari publisher dan menyebarkannya kepada subscriber yang tertarik. Broker juga bertanggung jawab untuk mengelola daftar subscriber dan topik-topik yang tersedia.

3. **Subscriber (Pelanggan)**: Subscriber adalah komponen yang tertarik pada pesan tertentu. Mereka mendaftar ke broker untuk menerima pesan dari topik tertentu. Ketika pesan yang sesuai dengan topik yang diinginkan tiba, subscriber menerima pesan tersebut.

Indirect communication seperti yang digunakan dalam protokol publish-subscribe (pub-sub) dan message queue memungkinkan aplikasi yang berbeda berkomunikasi secara efisien tanpa perlu tahu tentang eksistensi satu sama lain. Protokol pub-sub dan message queue memiliki perbedaan dalam cara pesan dikirim dan diterima:

1. **Publish-Subscribe (Pub-Sub)**: Dalam protokol pub-sub, publisher mengirim pesan ke topik tertentu. Subscriber yang berlangganan topik ini akan menerima pesan tersebut. Subscribing tidak perlu berhubungan langsung dengan publisher. Broker adalah yang mengelola semua hubungan antara publisher dan subscriber.

2. **Message Queue**: Dalam message queue, pesan disimpan dalam antrian dan diberikan kepada subscriber yang memintanya. Setiap pesan hanya dapat dikonsumsi oleh satu subscriber. Message queue umum digunakan dalam skenario antrian pesan yang dapat diambil oleh worker (pemroses).
