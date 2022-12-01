from pytube import YouTube
import os

def TitulosYoutube(Link):
    Titulo = "'" + Link.title + "'"
    print("El titulo del video es:", Titulo)
    # return Titulo

def AutorVideo(Link):
    Autor = "'" + Link.author + "'"
    print("El autor del video es:", Autor)
    # return Autor

def CancionVideo(Opcion, path):
    
    if Opcion == 1:
        Formato = "Cancion"
        video = yt.streams.filter(only_audio=True).first()
        downloaded_file = video.download(path)
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)

    else:
        Formato = "Video"
    print("La eleccion fue:", Formato)
    print("Done") 
    

VideoOrCancion = int(input("Selecciona una opcion:\n 1) Cancion\n 2) Video \n Opcion a elegir: "))
url = str(input("Ingrese el url:- "))
yt = YouTube(url)
DireccionGuardado = r"D:\Descargas Edge"

TitulosYoutube(yt)
AutorVideo(yt)
CancionVideo(VideoOrCancion, DireccionGuardado)
