import os
import subprocess
import sys

from urllib.parse import urlparse


def download_file(url, destination):
    try:
        subprocess.run(["wget", "-O", destination, url], check=True)
        # Извлекаем имя файла из URL
        file_name = os.path.basename(urlparse(url).path)
        print(f"Установка {file_name} в {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка {url}: {e}")


def main(assets_folder, custom_embedder, custom_config_url=None, custom_model_url=None, embedder_name=None):
    os.makedirs(assets_folder, exist_ok=True)

    hugg_link = "https://huggingface.co/Politrees/RVC_resources/resolve/main/embedders/transformers"
    config_file_name = "config.json"
    model_file_name = "pytorch_model.bin"

    file_links = {
        "rmvpe/rmvpe.pt": f"{hugg_link}/predictors/rmvpe.pt",
    }

    if custom_embedder:
        file_links.update({
            "hubert/config.json": custom_config_url,
            "hubert/pytorch_model.bin": custom_model_url,
        })
    else:
        file_links.update({
            "hubert/config.json": f"{hugg_link}/{embedder_name}/{config_file_name}",
            "hubert/pytorch_model.bin": f"{hugg_link}/{embedder_name}/{model_file_name}",
        })

    for file, link in file_links.items():
        file_path = os.path.join(assets_folder, file)
        if not os.path.exists(file_path):
            download_file(link, file_path)


if __name__ == "__main__":
    assets_folder = sys.argv[1]  # ./assets/
    custom_embedder = sys.argv[2].lower() == 'true'  # True - включить кастомные ссылки, False - выключить

    if custom_embedder:
        if len(sys.argv) < 5:
            print("Ошибка: При использовании пользовательского embedder необходимо указать URL-адреса для конфигурации и модели.")
            sys.exit(1)
        custom_config_url = sys.argv[3]  # кастомная ссылка на конфиг-файл
        custom_model_url = sys.argv[4]  # кастомная ссылка на модель
        main(assets_folder, custom_embedder, custom_config_url=custom_config_url, custom_model_url=custom_model_url)
    else:
        if len(sys.argv) < 4:
            print("Ошибка: Необходимо указать имя embedder, если не используется пользовательский embedder.")
            sys.exit(1)
        embedder_name = sys.argv[3]  # contentvec, chinese_hubert_base, japanese_hubert_base, korean_hubert_base
        main(assets_folder, custom_embedder, embedder_name=embedder_name)
