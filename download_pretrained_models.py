import subprocess, os
pretrained_folder = "/content/assets/pretrained_v2"
if not os.path.exists(pretrained_folder):
    os.makedirs(pretrained_folder)
files = {
    "f0D40k":"https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D40k.pth",
    "f0G40k":"https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G40k.pth",
    "f0D40k":"https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kD.pth",
    "f0G40k":"https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kG.pth",
    "f0D40k":"https://huggingface.co/MUSTAR/SnowyRuPretrain_EnP_40k/resolve/main/D_Snowie_RuPretrain_EnP.pth",
    "f0G40k":"https://huggingface.co/MUSTAR/SnowyRuPretrain_EnP_40k/resolve/main/G_Snowie_RuPretrain_EnP.pth",
    "f0D40k":"https://huggingface.co/ORVC/RIN_E3/resolve/main/RIN_E3_D.pth",
    "f0G40k":"https://huggingface.co/ORVC/RIN_E3/resolve/main/RIN_E3_G.pth",
    "f0D40k":"https://huggingface.co/MUSTAR/SnowieV3.1-40k/resolve/main/D_SnowieV3.1_40k.pth",
    "f0G40k":"https://huggingface.co/MUSTAR/SnowieV3.1-40k/resolve/main/G_SnowieV3.1_40k.pth",
    "f0D40k":"https://huggingface.co/MUSTAR/SnowieV3.1-X-RinE3-40K/resolve/main/D_Snowie-X-Rin_40k.pth",
    "f0G40k":"https://huggingface.co/MUSTAR/SnowieV3.1-X-RinE3-40K/resolve/main/G_Snowie-X-Rin_40k.pth"
}
for file, link in files.items():
    file_path = os.path.join(pretrained_folder, file)
    if not os.path.exists(file_path):
        try:
            subprocess.run(['aria2c', '--console-log-level=error', '-c', '-x', '16', '-s', '16', '-k', '1M', link, '-d', pretrained_folder, '-o', file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {file}: {e}")
