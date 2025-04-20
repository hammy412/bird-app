from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer

# Load and initialize the BirdNET-Analyzer models.
analyzer = Analyzer()

recording = Recording(
    analyzer,
    "uploads/sample.mp3",
    min_conf=0.25,
)

recording.analyze()
seen = set()

print()
for result in recording.detections:
    commonName = result['common_name']
    scientificName = result['scientific_name']
    confidence = int(round(result['confidence'],2) * 100)
    if commonName not in seen:
        print(f"Common Name: {commonName}\nScientific Name: {scientificName}\nConfidence: {confidence}%")
        seen.add(commonName)