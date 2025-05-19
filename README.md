# PLAN B – Offline Responsible AI Workshop

Denne pakken lar deg kjøre hele workshopen lokalt **uten** Colab, Docker eller GPU.

## 1 . Installer Python ≥ 3.10

## 2 . Virtuelt miljø
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

## 3 . Installer avhengigheter
```bash
python -m pip install --upgrade pip
pip install -r requirements_offline.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## 4 . Start JupyterLab
```bash
jupyter lab
```
Åpne **offline_workshop.ipynb** og følg instruksjonene.

## 5 . Hent data
```bash
python scripts/fetch_adult.py
```

Generert 2025-05-13