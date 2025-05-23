from pytubefix import YouTube

url = 'https://youtu.be/wuNaJxU2ElY?si=BjYN0BPR4_cjhMZe'

yt = YouTube(url)

description = yt.description

def info(titulo, descricao):
    return f'Vídeo: {titulo} \n' + f'Descrição: {descricao}\n'

# resolucao = input('Resolução: \n [1] - 360p \n [2] - 480p \n [3] - 720p')
# if resolucao == 1:
#     stream = yt.streams.get_by_itag(18)
# elif resolucao == 2:
#     stream = yt.streams.get_by_itag(135)
# elif resolucao == 3:
#     stream = yt.streams.get_by_itag(22)
# else:
#     print('Não existe essa opção')

ys = yt.streams.get_highest_resolution()
ys.download(output_path=r'C:\\Users\\joaom\\OneDrive\\Documents\\Vídeos')

