# import matplotlib.pyplot as plt
import svgwrite
import librosa
import sys
import os
# import librosa.display

# filename = "guitar.wav"

# y1, sr1 = librosa.load(filename, 22050)
# y2, sr2 = librosa.load(filename, 11025)
# y3, sr3 = librosa.load(filename, 4000)

# plt.figure()
# plt.subplot(3, 1, 1)
# librosa.display.waveplot(y1, sr=sr1)
# plt.subplot(3, 1, 2)
# librosa.display.waveplot(y2, sr=sr2)
# plt.subplot(3, 1, 3)
# librosa.display.waveplot(y3, sr=sr3)
# plt.show()

def createSVG(filepath):
  y, sr = librosa.load(filepath, 3000);

  vals = y.tolist();

  points = []

  offset = 200
  yscale = 200
  xscale = 0.04

  for i in range(0, len(vals)):
    if(vals[i] > 0):
      points.append((i * xscale, offset + vals[i] * yscale))

  for i in xrange(len(vals) -1, -1, -1):
    if(vals[i] < 0.0):
      points.append((i * xscale, offset + vals[i] * yscale))

  filepath = filepath.replace(".wav", "_waveform.svg")
  filename = filepath.split("/")[-1]
  dwg = svgwrite.Drawing(filename=filename, size=(3000, 400), debug=True)

  dwg.add(dwg.polygon(points))
  print filepath
  print filename
  dwg.saveas(filepath)

path = sys.argv[1]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for file in files:
  if file.endswith(".wav") or file.endswith(".wave"):
    createSVG(path + "/" + file)