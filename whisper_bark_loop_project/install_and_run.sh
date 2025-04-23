
#!/bin/bash
echo "📦 Installation environnement virtuel..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Prêt. Lancez : source venv/bin/activate && python whisper_to_bark_local.py"
