import torch
from TTS.api import TTS
import gradio as gr

# Immediate Audio Playback
import pygame
from pygame import mixer
import pygame._sdl2 as sdl2

import os


processor: str = "cuda" if torch.cuda.is_available() else "cpu"
print("Device: ", processor)
tts = TTS(model_name='tts_models/en/vctk/vits').to(processor)
# use tts.speakers for getting available speakers


pygame.init()
defaultAudioDevice = None
audioDevices = sdl2.get_audio_device_names(False)
pygame.quit()

defaultAudioDevice = audioDevices[0]
for device in audioDevices:
  if (device == "CABLE Input (VB-Audio Virtual Cable)"):
    defaultAudioDevice = "CABLE Input (VB-Audio Virtual Cable)"
    break
mixer.init(devicename=defaultAudioDevice)
currentAudioDevice = defaultAudioDevice
index = 0


# Emptry previous TTS
for filename in os.listdir("outputs/tts"):
  os.remove(os.path.join("outputs/tts", filename))


def generateAudio(text: str, speaker: int, speed: float, audioDevice: str, playback: bool ):
  global currentAudioDevice
  global index

  index += 1
  mixer.music.stop()
  tts.tts_to_file(text, file_path=f"outputs/tts/tts{index}.wav", speaker=f"p{speaker}", speed=speed)

  # If audio device is changed
  if audioDevice != currentAudioDevice:
    mixer.quit()
    mixer.init(audioDevice)
    currentAudioDevice = audioDevice

  if playback:
    mixer.music.load(f"outputs/tts/tts{index}.wav")
    mixer.music.play()

  return f"outputs/tts/tts{index}.wav", ""


# Using Gradio Blocks to recreate the interface
with gr.Blocks() as webUI:
  gr.Markdown("# Text to Speech")
  
  with gr.Row():
    with gr.Column(variant="panel"):
      inputsHeading        = gr.Markdown("## Inputs")
      text_input           = gr.Textbox(label="Text", value="")
      speaker_input        = gr.Number(label="Speaker", value=238)
      speed_input          = gr.Slider(minimum=0.5, maximum=2.0, step=0.1, label="Speed", value=1)
      
      with gr.Group():
        audio_device_input   = gr.Dropdown(audioDevices, label="Output Device", value=defaultAudioDevice)
        playback_input       = gr.Checkbox(label="Playback to device immediately", value=True)
      # Add models dropdown and accordingly speakers dropdown
            
      with gr.Row():
        with gr.Column(): clear_button = gr.ClearButton(value="Clear", variant="secondary")
        with gr.Column(): generate_button = gr.Button(value="Generate Audio", variant="primary")

    with gr.Column(variant="panel"):
      outputsHeading = gr.Markdown("## Outputs")
      audio_output   = gr.Audio(label="Audio")

      flag_button = gr.Button("Flag")

  clear_button.add([text_input, audio_output])
  generate_button.click(fn=generateAudio, inputs=[text_input, speaker_input, speed_input, audio_device_input, playback_input], outputs=[audio_output, text_input])
  text_input.submit(fn=generateAudio,     inputs=[text_input, speaker_input, speed_input, audio_device_input, playback_input], outputs=[audio_output, text_input])

webUI.launch()
