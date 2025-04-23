
# 🔁 Whisper + Bark Loop (Azure OpenAI + Accent Africain)

Ce projet permet de transcrire automatiquement un dossier de fichiers audio en français via Whisper (Azure OpenAI), puis de générer un nouvel audio "revoicé" avec un accent africain réaliste grâce à Bark.

## 🧰 Fonctionnalités
- Transcription via Whisper (`whisper-1` sur Azure)
- Revoicing / TTS avec accent africain francophone (modèle Bark)
- Support batch de fichiers `.wav` / `.mp3`
- Export CSV avec résumé des transcriptions et noms de fichiers audio générés

## 📁 Arborescence attendue
```
/content/
├── audio_batch/               # Vos fichiers audio originaux à transcrire
├── audio_synthetise/          # Résultat : audios générés par Bark
├── resume_transcription_tts.csv  # Résumé CSV
└── .env                       # Contient la clé API Azure
```

## 🔐 Configuration
Modifiez le fichier `.env` comme suit :

```
AZURE_OPENAI_API_KEY=VOTRE_CLÉ
AZURE_OPENAI_ENDPOINT=https://instancehackatonpionners05.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-pionners34
AZURE_OPENAI_API_VERSION=2024-05-01-preview
```

## ▶️ Utilisation
1. Ouvrez le notebook `whisper_azure_to_bark_loop.ipynb` dans Google Colab.
2. Téléversez vos fichiers `.mp3` ou `.wav` dans `/content/audio_batch`.
3. Remplissez `.env` avec votre clé API Azure.
4. Exécutez toutes les cellules.
5. Téléchargez vos audios générés dans `/content/audio_synthetise`.

## 📦 Technologies utilisées
- [Azure OpenAI Whisper](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/quickstart)
- [SunO Bark](https://github.com/suno-ai/bark)
- Python, Colab, SciPy, dotenv

## 🗣️ Exemple de prompt utilisé
```
"African French accent, male voice. Bonjour, docteur. Je ressens une douleur à la poitrine."
```

## 📬 Contact
Créé par Mahuvivi Turibio KEKE | @turibiok
