# Text To Speech - Web UI
A Web UI made with gradio for running local text to speech models with Coqui TTS \
Web UI: [http://127.0.0.1:7860](http://127.0.0.1:7860)

## Installation
Download python 3.9.0 via [pyenv](https://github.com/pyenv/pyenv#installation) or [python.org](https://python.org) \
Create virtual environment, through vscode or venv

Activate your virtual environment with the following command (replace .venv with your virtual environment name)
```bash
.venv/Scripts/activate
```
---

Ensure everything is up to date
```bash
pip install --upgrade pip
pip install --upgrade pip setuptools wheel
```
---

Install Coqui TTS \
Use _**prebuilt wheel**_ incase you are getting wheel build error
<!--pip install https://files.pythonhosted.org/packages/66/34/f321773e7ac1432de207da10d2f8a42b94357cb989e122f431c3a536d8b/coqui_tts-0.25.3-py3-none-any.whl-->
```bash
pip install TTS
```
---

Install CUDA 11.8, 12.1 or 12.4 if you have CUDA enabled GPU
```
https://pytorch.org/get-started/locally to get your torch install command
```
---

Install gradio for WebUI and pygame for automatic voice playback
```bash
pip install gradio
pip install pygame
```

For using tts_models/en/vctk/vits you need to install [espeak-ng](https://github.com/espeak-ng/espeak-ng/releases)

## Running the program
Activate your virtual environment (replace .venv with your virtual environment name) then run TextToSpeech.py
```bash
.venv/Scripts/activate
```

OR

If you are using vscode, modify .vscode/launch.json from .venv to your virtual environment name
```json
"env": {
  "PATH":  "${workspaceFolder}/.venv/Scripts:${env:PATH}"
}
```
