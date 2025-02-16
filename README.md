A [yt-dlp](https://github.com/yt-dlp/yt-dlp) extractor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) for downloading [Spotify Canvas](https://artists.spotify.com/canvas) videos.


## Installation

Requires yt-dlp `2023.01.02` or above.

You can install this package with pip:
```
python3 -m pip install -U https://github.com/qbnu/yt-dlp-SpotifyCanvas/archive/master.zip
```

See [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the other methods this plugin package can be installed.


## Usage

**IMPORTANT**: Downloading will NOT work anymore unless you specify your `sp_dc` cookie. See [*How do I pass cookies to yt-dlp?*](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp).  
You can use a cookie file like this:
```
# For yt-dlp-SpotifyCanvas
.spotify.com	TRUE	/	TRUE	2147483647	sp_dc	<your cookie value>
```

Download the Canvas for a song:
```
yt-dlp --cookies spotify-cookies.txt https://open.spotify.com/track/0DiWol3AO6WpXZgp0goxAV
```
Write the song info in [yt-dlp format](https://github.com/yt-dlp/yt-dlp#output-template) without downloading:
```
yt-dlp --write-info --skip-download --ignore-no-formats-error https://open.spotify.com/track/0DiWol3AO6WpXZgp0goxAV
```
Note: if you download a static Canvas (JPEG) with `--write-thumbnail` set then the thumbnail will overwrite the Canvas


## Related projects

Thanks to [Canvas Downloader](https://www.canvasdownloader.com/) for help with figuring out what cookies need to be sent.

[My Spotify Canvas](https://github.com/bartleyg/my-spotify-canvas)  
[librespot-java](https://github.com/librespot-org/librespot-java)  
[Spotify Canvas Downloader](https://github.com/Delitefully/spotify-canvas-downloader)  
[Spicetify Canvas](https://github.com/itsmeow/Spicetify-Canvas)  
