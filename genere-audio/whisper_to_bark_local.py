
import os
import openai
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
from scipy.io.wavfile import write
from bark import SAMPLE_RATE, generate_audio

# Charger la config
load_dotenv(".env")

openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Dossiers d'entrée et sortie
audio_dir = Path("audio_batch")
output_dir = Path("audio_synthetise")
audio_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

results = []

# Traitement de chaque fichier audio
for file_path in audio_dir.glob("*.[wm][ap][v3]"):
    print(f"▶️ Fichier : {file_path.name}")
    with open(file_path, "rb") as f:
        response = openai.Audio.transcribe(
            file=f,
            model="whisper-1",
            deployment_id=deployment_name,
            response_format="text"
        )
        texte_transcrit = response.strip()

    # Générer audio avec Bark
    prompt = f"African French accent, male voice. {texte_transcrit}"
    audio_out = generate_audio(prompt)
    out_path = output_dir / f"{file_path.stem}_bark.wav"
    write(out_path, SAMPLE_RATE, audio_out)

    results.append({
        "fichier_audio": file_path.name,
        "transcription": texte_transcrit,
        "audio_synthetise": out_path.name
    })

# Sauvegarde CSV
df = pd.DataFrame(results)
df.to_csv("resume_transcription_tts.csv", index=False)
print("✅ Résultat : resume_transcription_tts.csv")
