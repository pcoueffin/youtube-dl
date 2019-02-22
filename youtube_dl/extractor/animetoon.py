from __future__ import unicode_literals

from .common import InfoExtractor

import re

class AnimeToonIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?animetoon\.org/(?P<id>.+)'
    _TEST = {
        'url': 'http://www.animetoon.org/high-school-dxd-episode-10',
        'only_matching': True,
    }

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')

        webpage = self._download_webpage(url, video_id)
        self.report_extraction(video_id)
        iframe_url = self._html_search_regex(r'<div class="vmargin"><div><span class="playlist">Playlist [0-9]*</span></div><div><iframe src="([^"]+)"', webpage, u'iframe URL')

        vidsrc=self._html_search_regex(r'https?://([^/]+)/', iframe_url, u'Video Source')
        
        if self._downloader.params.get('verbose', False):
            self._downloader.to_screen(
                '[debug] iframe URL: %s' % (iframe_url))
            self._downloader.to_screen(
                '[debug] Video Source: %s' %(vidsrc))

        iframe=self._download_webpage(iframe_url, video_id)
        #print(iframe)
        if (vidsrc == "playbbme.gogoanime.to"):
            vidurl=self._html_search_regex(r'var url *= *\'(.*)\' *;', iframe, u'video URL')
        elif(vidsrc == "playpandanet.gogoanime.to"):
            vidurl=self._html_search_regex(r'url: *\'(.*)\',', iframe, u'Video URL')
        elif(vidsrc == "videozoome.gogoanime.to"):
            vidurl=self._html_search_regex(r'file: *"(http.*)",', iframe, u'Video URL')
        else:
            self.report_error("I don't know what to do with vidsrc = %s" % (vidsrc))
            print(iframe)
        
        vidurl=vidurl+"&start=0"
        if self._downloader.params.get('verbose', False):
            self._downloader.to_screen(
                '[debug] Video URL: %s' %(vidurl))
        
        return {
            'id': video_id,
            'title': video_id,
            'url': vidurl
        }


