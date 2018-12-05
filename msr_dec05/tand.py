import librosa

file = "2018-8-4_23-16-40.wav"
sig, sr = librosa.load(file, sr=None)

print("sig " + str(len(sig)))
print("sr" + str(sr))

