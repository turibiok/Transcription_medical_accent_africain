
import os
from pathlib import Path
from scipy.io.wavfile import write
from bark import SAMPLE_RATE, generate_audio

# 📁 Dossier contenant les fichiers texte (.txt)
corpus_dir = Path("corpus_textes")
output_dir = Path("audio_from_corpus")
corpus_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

# 🔁 Parcours des fichiers .txt et génération audio avec Bark
for txt_file in corpus_dir.glob("*.txt"):
    with open(txt_file, "r", encoding="utf-8") as f:
        texte = f.read().strip()

    prompt = f"African French accent, male voice. {texte}"
    audio_array = generate_audio(prompt)
    output_path = output_dir / f"{txt_file.stem}_bark.wav"
    write(output_path, SAMPLE_RATE, audio_array)
    print(f"✅ Audio généré : {output_path.name}")

print("🎉 Tous les textes ont été convertis en audio.")
