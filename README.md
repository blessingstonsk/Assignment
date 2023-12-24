#Assignment 1 : Lip Syncing using wave2lip
# Lip Syncing with Wave2Lip

This repository contains a simple script for lip-syncing using the Wave2Lip model. The code synchronizes the lip movements of characters in a given video file with the corresponding audio file.

## Requirements

- Python (>=3.6)
- PyTorch
- Other dependencies (install using `pip install -r requirements.txt`)

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/Rudrabha/Wav2Lip.git
    cd your-repo
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your input files:
   - Place your input video file (`Input.mp4`) in the root directory.
   - Place your input audio file (`audio.mp3`) in the root directory.
   - Download the pre-trained model checkpoint (`wav2lip_gan.pth`) from [here](https://github.com/Rudrabha/Wav2Lip) and place it in the `checkpoints` directory.

4. Run the lip-syncing script:

    ```bash
    python lipsync.py
    ```

5. Check the output:
   - The lip-synced video will be saved in the root directory with the name `result.mp4`.

## Directory Structure

```plaintext
your-repo/
|-- lip_sync_script.py
|-- README.md
|-- Input.mp4
|-- audio.mp3
|-- checkpoints/
|   `-- wav2lip_gan.pth
|-- result.mp4
|-- other_files_and_directories/
###

