import json
import subprocess
from pytubefix import YouTube

def download_audio_from_video_youtube(url: str, output_path: str = ".", file_name: str = ".") -> str:
    """
    Parámetros:
    - url: str -> Enlace completo al Short (por ejemplo, https://www.youtube.com/shorts/1Fxq3DIUPuk)
    - output_path: str -> Carpeta de destino (por defecto, directorio actual)

    Retorna:
    - str: url of file downloaded.
    """
    yt = YouTube(url, use_po_token=True, po_token_verifier=po_token_verifier)

    video = yt.streams.get_audio_only()
    return video.download(output_path=output_path, filename=file_name)


def po_token_verifier():
    token_object = generate_youtube_token()
    return token_object["visitorData"], token_object["poToken"]

def generate_youtube_token() -> dict:
    result = cmd("npx youtube-po-token-generator")
    data = json.loads(result.stdout)
    return data

def cmd(command, check=True, shell=True, capture_output=True, text=True):
    """
    Runs a command in a shell, and throws an exception if the return code is non-zero.
    :param command: any shell command.
    :return:
    """
    try:
        return subprocess.run(command, check=check, shell=shell, capture_output=capture_output, text=text)
    except subprocess.CalledProcessError as error:
        return ('0','