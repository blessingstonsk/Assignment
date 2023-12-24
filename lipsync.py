import torch
import subprocess
import os

def lip_sync(input_video_path, input_audio_path, output_video_path, checkpoint_path):
    # Use absolute paths
    input_video_path = os.path.abspath(input_video_path)
    input_audio_path = os.path.abspath(input_audio_path)
    output_video_path = os.path.abspath(output_video_path)
    checkpoint_path = os.path.abspath(checkpoint_path)

    # Check if the output directory exists, create it if not
    output_dir = os.path.dirname(output_video_path)
    os.makedirs(output_dir, exist_ok=True)

    # Run the lip-syncing script
    subprocess.run([
        "python", "inference.py",
        "--checkpoint_path", checkpoint_path,
        "--face", input_video_path,
        "--audio", input_audio_path,
        "--outfile", output_video_path
    ])

if __name__ == "__main__":
    # Replace these paths with the actual paths to your files
    input_video_path = "Input.mp4"
    input_audio_path = "audio.mp3"
    output_video_path = "result.mp4"
    checkpoint_path = "checkpoints/wav2lip_gan.pth"

    # Check if the model file exists
    if not os.path.exists(checkpoint_path):
        print(f"Error: Pre-trained model file not found at {checkpoint_path}.")
    else:
        # Perform lip-syncing
        lip_sync(input_video_path, input_audio_path, output_video_path, checkpoint_path)
        print(f"Lip-syncing completed. Output video saved at {output_video_path}.")
