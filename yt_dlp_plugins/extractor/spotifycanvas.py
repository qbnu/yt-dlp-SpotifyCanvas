from yt_dlp.extractor.spotify import SpotifyBaseIE
from yt_dlp.utils import float_or_none, traverse_obj, unified_strdate

from yt_dlp_plugins.extractor.proto.canvas_pb2 import EntityCanvazRequest, EntityCanvazResponse


class SpotifyCanvasIE(SpotifyBaseIE):
    _VALID_URL = r'https?://open\.spotify\.com/(?:embed/)?track/(?P<id>\w+)'

    def _real_extract(self, url):
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
