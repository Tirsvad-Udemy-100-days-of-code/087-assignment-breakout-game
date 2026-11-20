# Refleksi

[English](Reflection) · [Dansk](Reflection-da) · **Bahasa Malaysia**

## Bagaimana kami mendekati projek ini

Kami bermula dengan senarai perkara yang mesti dapat dilakukan oleh permainan, dan membahagikannya kepada tujuh langkah yang masing-masing boleh dijalankan dan dilihat: tetingkap dan dayung, bola, pantulan dayung, bata, perlanggaran dan skor, nyawa dan penamat, peningkatan kelajuan. Sebelum menulis kod, kami mencatat untuk siapa projek ini, apa yang mesti disampaikannya dan dalam susunan apa. Kemudian setiap langkah dibina, diuji, disemak dan difoto sebelum langkah seterusnya bermula.

## Apa yang sukar

- **Sisi perlanggaran.** Menentukan sama ada bola terkena sisi atau bahagian atas bata memerlukan paling banyak pemikiran. Jawapannya ialah membandingkan sedalam mana bola masuk pada setiap paksi, dan pukulan di sudut memerlukan satu peraturan lagi.
- **Terowongan.** Bola yang laju boleh melompati objek nipis. Kami perlu membuktikan bahawa kelajuan maksimum lebih kecil daripada benda terkecil yang mesti dikena oleh bola.
- **Tangkapan skrin tanpa menyentuh desktop.** Menjalankan tetingkap dalam bekas dengan skrin maya memerlukan sedikit persediaan, tetapi memberi kami gambar yang boleh diulang daripada kod tepat bagi setiap langkah.
- **Masalah kecil alat.** Pengakhiran baris yang berbeza antara Windows dan Linux menyebabkan semakan skrip shell gagal dalam saluran paip sehingga kami membetulkannya.

## Apa yang mudah

- Turtle cepat untuk dimulakan: tetingkap dan bentuk yang bergerak hanya memerlukan beberapa baris.
- Oleh sebab peraturan tidak bergantung pada Turtle, ujian menjadi pendek dan pantas.

## Pembelajaran terbesar

Pisahkan peraturan daripada lukisan. Setelah peraturan permainan menjadi fungsi Python biasa pada nilai kecil yang tidak berubah, hampir setiap pepijat dapat ditangkap oleh ujian dalam milisaat, dan kami dapat memainkan satu permainan penuh tanpa tetingkap.

## Apa yang akan kami lakukan secara berbeza

- Menulis ujian perlanggaran sebelum kod perlanggaran, untuk menemui kes sudut lebih awal.
- Memilih gelung bingkai dengan `ontimer` dari awal dan bukan `time.sleep`.
- Menambah bunyi, peringkat dan senarai skor tertinggi. Perkara ini di luar skop tugasan ini.

[Kembali ke Utama](Home-ms)
