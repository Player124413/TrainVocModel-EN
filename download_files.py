import os
import subprocess

assets_folder = "./assets/"
os.makedirs(assets_folder, exist_ok=True)

file_links = {
    "rmvpe/rmvpe.pt": "https://huggingface.co/Rejekts/project/resolve/main/rmvpe.pt",
    "hubert/hubert_base.pt": "https://huggingface.co/spaces/Hobis/bark-voice-cloning-polish-HuBERT-quantizer/resolve/main/hubert.pt"
}

for file, link in file_links.items():
    file_path = os.path.join(assets_folder, file)
    if not os.path.exists(file_path):
        try:
            subprocess.run(['wget', '-O', file_path, link], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {file}: {e}")
