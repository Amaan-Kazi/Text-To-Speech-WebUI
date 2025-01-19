import torch
from TTS.api import TTS
import gradio as gr

device: str = "cuda" if torch.cuda.is_available() else "cpu"
print("Device: ", device)

tts = TTS(model_name='tts_models/en/vctk/vits').to(device)
# use tts.speakers for getting available speakers

def generateAudio(text: str, speaker: int, speed: float, playback: bool):
  tts.tts_to_file(text, file_path="outputs/output.wav", speaker=f"p{speaker}", speed=speed)
  return "outputs/output.wav", ""

# Using Gradio Blocks to recreate the interface
with gr.Blocks() as webUI:
  gr.Markdown("# Text to Speech")
  
  with gr.Row():
    with gr.Column(variant="panel"):
      inputsHeading  = gr.Markdown("## Inputs")
      text_input     = gr.Textbox(label="Text", value="")
      speaker_input  = gr.Number(label="Speaker", value=238)
      speed_input    = gr.Slider(minimum=0.5, maximum=2.0, step=0.1, label="Speed", value=1)
      playback_input = gr.Checkbox(label="Playback to device immediately", value=True)
      # Add models dropdown and accordingly speakers dropdown
      # Add Audio Output device(s)
            
      with gr.Row():
        with gr.Column(): clear_button = gr.ClearButton(value="Clear", variant="secondary")
        with gr.Column(): generate_button = gr.Button(value="Generate Audio", variant="primary")

    with gr.Column(variant="panel"):
      outputsHeading = gr.Markdown("## Outputs")
      audio_output   = gr.Audio(label="Audio")

      flag_button = gr.Button("Flag")

  clear_button.add([text_input, audio_output])
  generate_button.click(fn=generateAudio, inputs=[text_input, speaker_input, speed_input, playback_input], outputs=[audio_output, text_input])
  text_input.submit(fn=generateAudio, inputs=[text_input, speaker_input, speed_input, playback_input], outputs=[audio_output, text_input])

webUI.launch()
