from yt_dlp.extractor.spotify import SpotifyBaseIE
from yt_dlp.networking import Request
from yt_dlp.utils import traverse_obj

from yt_dlp_plugins.extractor.protos.canvas_pb2 import EntityCanvazRequest, EntityCanvazResponse


class SpotifyCanvasIE(SpotifyBaseIE):
    _VALID_URL = r'https?://open\.spotify\.com/(?:embed/)?track/(?P<id>\w+)'

    def _real_extract(self, url):
        track_id = self._match_id(url)
        canvas_request = EntityCanvazRequest()
        canvas_request_entities = canvas_request.entities.add()
        canvas_request_entities.entity_uri = 'spotify:track:' + track_id
        req = Request(
            'https://gew1-spclient.spotify.com/canvaz-cache/v0/canvases',
            headers={
                'Content-Type': 'application/x-protobuf',
                'Authorization': f'Bearer {self._ACCESS_TOKEN}'
            },
            data=canvas_request.SerializeToString(),
        )
        urlh = self._request_webpage(req, track_id)
        assert urlh
        content = urlh.read()
        print(type(content))

        canvas_response = EntityCanvazResponse()
        canvas_response.ParseFromString(content)
        print(canvas_response)

        if(len(canvas_response.canvases) == 0):
            self.raise_no_formats('No formats are available', expected=True, video_id=track_id)

        req = Request(
            f'https://api.spotify.com/v1/tracks/{track_id}',
            headers={
                'Authorization': f'Bearer {self._ACCESS_TOKEN}'
            },
        )
        track_info = self._download_json(req, track_id)
        #print(track_info)

        formats = tuple({'url': canvas.url} for canvas in canvas_response.canvases)
        print(traverse_obj(track_info, ('album', 'artists', ..., 'name')))

        track = track_info.get('name')
        artists = traverse_obj(track_info, ('artists', ..., 'name'))

        # For convenience
        title = None
        if artists and track:
            artist = ', '.join(artists)
            title = f'{artist} - {track} (Canvas)'
            
        return {
            'id': track_id,
            'title': title,
            'track': track,
            'track_number': track_info.get('track_number'),
            'track_id': track_info.get('id'),
            'artists': artists,
            'album_artists': traverse_obj(track_info, ('album', 'artists', ..., 'name')),
            'disc_number': track_info.get('disc_number'),
            'formats': formats,
        }

