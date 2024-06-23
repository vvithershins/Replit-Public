from pytube import YouTube

def download_video(url, save_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        stream.download(output_path=save_path)
        print(f"Downloaded to: {save_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the save path (default is current directory): ")

    if not save_path:
        save_path = '.'

    download_video(video_url, save_path)
