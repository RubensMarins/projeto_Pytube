import os
from pytube import YouTube
from pytube import Playlist

def baixarVideo() -> str:
    yt = getURL()
    print("Baixando video...")
    video = yt.streams.get_highest_resolution()
    video.download("./videos")
    print("Video baixado com sucesso!!!")
    os.system("pause")
    getMenu()

def baixarAudio() -> str:
    yt = getURL()
    print("Baixando audio...")
    
    audio = yt.streams.filter(only_audio=True).all()
    audio[0].download("./audios")    
    
    print("Audio baixado com sucesso!!!")
    os.system("pause")
    getMenu()
    
def baixarPlaylist() -> str:
    yt = getURL()
    playlist = Playlist(yt)
    
    print("Baixando video...")
    for url in playlist:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download("./playlist")
        
    print("Video baixado com sucesso!!!")
    os.system("pause")
    getMenu()


def getMenu() -> str:
    '''
    Função que exibe o menu principal da aplicação
    e retorna a opção escolhida pelo usuário
    '''
    os.system("cls")
    print(30*"=")
    print("    Download Midia YouTube")
    print(30*"=")
    
    print('1 - Download de Video')
    print('2 - Download de Audio')
    print('3 - Download da Playlist')
    print('5 - Sair')
    opc: str = input("Digite a sua opção: ")
    return opc

def getURL() -> str:
    print(30*"=")
    link: str = input("Digite ou cole o link para download : ")
    
    if link.startswith("https://www.youtube.com/watch?v="):
        yt = YouTube(link)
        return yt
    elif link.startswith("https://www.youtube.com/playlist?list="):
        return link
         
    else:
        print("Link não é válido ou não é do YouTube !!!")
        os.system("pause")
        menu()
        

def menu() -> None:
    os.system("cls")
    opcao: str =  getMenu()
    match opcao:
        case '1':
            baixarVideo()
            os.system("pause")
            menu()
        case '2':
           baixarAudio()
           os.system("pause")
           menu()
        case '3':
            baixarPlaylist()
            os.system("pause")
            menu()
        case '5':
            print("Saindo....")
            
        case _:
            print("Opção inválida")
            os.system("pause")
            menu()


if __name__ == '__main__':
   menu()
   
