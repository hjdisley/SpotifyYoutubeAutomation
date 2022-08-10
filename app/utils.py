from googleapiclient.discovery import build

def get_youtube_client(api_key):
    """
    Returns a youtube client object
    Parameters:
        api_key (str): The youtube api key
    
    Returns:
        YouTube client object
    """

    youtube_client = build('youtube', 'v3', developerKey=api_key)

    return youtube_client
