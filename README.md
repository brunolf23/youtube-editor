
# YouTube Video Downloader, Converter, and Transcriber

Este repositório contém um script Python que automatiza o processo de download, conversão de vídeo para áudio e transcrição de vídeos do YouTube. Utilizando as bibliotecas `pytube`, `ffmpeg` e Whisper, este script é ideal para educadores, pesquisadores e criadores de conteúdo que necessitam de transcrições precisas de vídeos.

## Funcionalidades

- **Download de Vídeos do YouTube**: Suporta vídeos individuais e playlists.
- **Conversão de Vídeo para Áudio**: Converte vídeos baixados em arquivos de áudio WAV.
- **Transcrição de Áudio**: Utiliza o Whisper para transcrever os áudios em texto.

## Pré-requisitos

Antes de executar o script, certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.x
- `pytube`: Instale com `pip install pytube`
- `ffmpeg`: Certifique-se de que o `ffmpeg` esteja instalado e configurado no PATH do sistema
- Whisper: Configure o Whisper no diretório especificado no script

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências Python:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure o `ffmpeg` e o Whisper conforme necessário.

## Uso

Edite o script `main.py` e defina a URL do YouTube (pode ser uma playlist ou vídeo único):

```python
youtube_url = 'https://www.youtube.com'
```

Execute o script:

```bash
python main.py
```
