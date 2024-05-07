from src.jellyfin_emby import JellyfinEmby

class Jellyfin(JellyfinEmby):
    def __init__(self, baseurl, token):
        authorization = (
            "MediaBrowser , "
            'Client="JellyPlex-Watched", '
            'Device="script", '
            'DeviceId="script", '
            'Version="5.2.0", '
            f"Token=\"{token}\""
        )
        headers = {
            "Accept": "application/json",
            "Authorization": authorization,
        }

        super().__init__(server_type="Jellyfin", baseurl=baseurl, token=token, headers=headers)  
