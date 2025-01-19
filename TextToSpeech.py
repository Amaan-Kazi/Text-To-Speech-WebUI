import torch
from TTS.api import TTS
import gradio as gr

device: str = "cuda" if torch.cuda.is_available() else "cpu"
print("Device: ", device)

tts = TTS(model_name='tts_models/en/vctk/vits').to(device)
print("Speakers: ", tts.speakers)

def generateAudio(text: str, speaker: int):
  tts.tts_to_file(text, file_path="outputs/output.wav", speaker=f"p{speaker}")
  return "outputs/output.wav"

webUI = gr.Interface(
  title       = "Text To Speech",
  fn          = generateAudio,

  inputs = [
    gr.Text(label="Text"),
    gr.Number(label=f"Speaker [{tts.speakers}]")
  ],

  outputs = [
    gr.Audio(label="Audio")
  ]    
)

webUI.launch()
