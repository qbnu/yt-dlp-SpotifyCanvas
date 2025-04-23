import base64
import pyotp

from yt_dlp.extractor.spotify import SpotifyBaseIE
from yt_dlp.utils import float_or_none, traverse_obj, unified_strdate

from yt_dlp_plugins.extractor.proto.canvas_pb2 import EntityCanvazRequest, EntityCanvazResponse


class SpotifyCanvasIE(SpotifyBaseIE):
    _VALID_URL = r'https?://open\.spotify\.com/(?:embed/)?track/(?P<id>\w+)'

    def _real_initialize(self):
        secretCipher = [12, 56, 76, 33, 88, 44, 88, 33, 78, 78, 11, 66, 22, 22, 55, 69, 54]
        processed = b''.join(bytes(str(byte ^ (i % 33 + 9)), 'ascii') for (i, byte) in enumerate(secretCipher))
        secretBase32 = base64.b32encode(processed)

        totp = pyotp.TOTP(secretBase32)
        server_time = self._download_json('https://open.spotify.com/server-time', None)['serverTime']
        code = totp.at(server_time)
        token_url = f'https://open.spotify.com/get_access_token?reason=transport&productType=web_player&totpVer=5&ts={server_time}&totp={code}'
        self._ACCESS_TOKEN = self._download_json(token_url, None)['accessToken']

    def _real_extract(self, url):
        cookies = self._get_cookies('https://open.spotify.com')
        if not traverse_obj(cookies, 'sp_dc'):
            self.raise_login_required(
                'sp_dc cookie is required to download Canvases!', metadata_available=True)

        track_id = self._match_id(url)

        # Get Canvas info
        canvas_request = EntityCanvazRequest()
        canvas_request.entities.add().entity_uri = f'spotify:track:{track_id}'
        canvas_response_bytes = self._request_webpage(
            'https://api-partner.spotify.com/canvaz-cache/v0/canvases', track_id,
            headers={
                'Content-Type': 'application/x-protobuf',
                'Authorization': f'Bearer {self._ACCESS_TOKEN}',
            },
            data=canvas_request.SerializeToString(),
        ).read()
        canvas_response = EntityCanvazResponse()
        canvas_response.ParseFromString(canvas_response_bytes)

        # Fail early if there is no Canvas
        formats = []
        thumbnails = []
        for canvas in canvas_response.canvases:
            if canvas.url:
                formats.append({'url': canvas.url})
            for thumbnail in canvas.thumbnails:
                thumbnails.append({
                    'width': thumbnail.width,
                    'height': thumbnail.height,
                    'url': thumbnail.url,
                })
        if not formats:
            self.raise_no_formats('No formats are available', expected=True, video_id=track_id)

        # Get track info
        track_info = self._download_json(
            f'https://api.spotify.com/v1/tracks/{track_id}', track_id,
            headers={'Authorization': f'Bearer {self._ACCESS_TOKEN}'},
        )

        # Parse data
        track = track_info.get('name')
        artists = traverse_obj(track_info, ('artists', ..., 'name'))
        # Set title for convenience
        title = f'{", ".join(artists)} - {track} (Canvas)' if artists and track else None
        return {
            'id': track_id,
            'duration': float_or_none(track_info.get('duration_ms'), scale=1000),
            'title': title,
            'track': track,
            'track_number': track_info.get('track_number'),
            'track_id': track_info.get('id'),
            'artists': artists,
            'album_artists': traverse_obj(track_info, ('album', 'artists', ..., 'name')),
            'album': traverse_obj(track_info, ('album', 'name')),
            'disc_number': track_info.get('disc_number'),
            'release_date': unified_strdate(traverse_obj(track_info, ('album', 'release_date'))),
            'thumbnails': thumbnails,
            'formats': formats,
        }
