import pytube

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag

def input_links():
    f = open("../youtubeVideoDownloader/videourls.txt","r") #İndirmek istediğiniz linkleri satır satır buradaki adrese ekleyin.

    links = f.readlines()
    download_videos(links,"low") #Burada bulunan "low" kısmı choose_resolution kısmından seçilebilir.
    #download_playlist(url,"low") Burayada aynı mantıkla kalite ekleyebilirsiniz. Video url kısmına herhangi bir ekleme yapılmasına gerek yok. 
                                # Sadece playlist url i koymanız yeterli. 

input_links()
