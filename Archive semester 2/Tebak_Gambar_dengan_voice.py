import os
import streamlit as st
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

# Lokasi direktori gambar
image_directory = r"D:/Jupyter lab/Ai-Experiment/gambar"
image_files = os.listdir(image_directory)

# Fungsi untuk merekam audio
def record_audio(duration):
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
    sd.wait()
    sf.write("recorded_audio.wav", audio, 44100)
    return "recorded_audio.wav"  # Mengembalikan nama file audio yang direkam

# Fungsi untuk mengonversi suara menjadi teks
def convert_speech_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text

# Fungsi utama
def main():
    st.title("Tebak Gambar dengan Suara")
    st.markdown("<center> Wahyu Ikbal Maulana</center>", unsafe_allow_html=True)
    st.markdown("<center> D4 Sains Data Terapan</center>", unsafe_allow_html=True)
    st.markdown("<center> 3323600056</center>", unsafe_allow_html=True)
    st.markdown("#####")
    st.markdown("#####")
    score = 0  # Variable untuk menyimpan nilai
    for file in image_files:
        if file.endswith(".jpg") or file.endswith(".png"):
            st.image(os.path.join(image_directory, file))
            if st.button("Rekam & Jawab", key=file[:4]):
                audio_file = record_audio(3)
                text = convert_speech_to_text(audio_file)
                st.write("Hasil transkripsi:", text)
                if text.lower() == file[:-4].lower():
                    st.write("Selamat, Anda benar!")
                    score += 1  # Tambahkan 1 ke nilai jika jawaban benar
                else:
                    st.write("Maaf, jawaban Anda salah.")
    st.write("Nilai Anda:", score)  # Menampilkan nilai setelah semua gambar selesai

if __name__ == "__main__":
    main()