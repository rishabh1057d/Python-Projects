import sounddevice as sd
import wavio

default_sample_rate = 44100
duration = float(input("Enter the recording duration in seconds: "))

sample_rate_input = input(f"Enter the sampling rate in Hz (Press Enter to use default {default_sample_rate} Hz): ")
sample_rate = int(sample_rate_input) if sample_rate_input else default_sample_rate
filename = "output.wav"
print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
sd.wait()
print("Recording finished.")

wavio.write(filename, audio_data, sample_rate, sampwidth=2)
print(f"Audio saved as {filename}.")

playback_choice = input("Do you want to play the recorded audio? (yes/no): ").strip().lower()
if playback_choice in ['yes', 'y']:
    print("Playing audio...")
    sd.play(audio_data, samplerate=sample_rate)
    sd.wait() 
    print("Playback finished.")
else:
    print("Playback skipped.")
