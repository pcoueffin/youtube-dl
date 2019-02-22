from __future__ import unicode_literals

from .common import InfoExtractor

import re

class OHentaiIE(InfoExtractor):
    _VALID_URL = r'https?://ohentai.org/detail.php\?vid=(?P<id>.+)'
    _TEST = {
        'url': 'https://ohentai.org/detail.php?vid=MTQyNQ==',
        'only_matching': True,
    }

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')

        self.report_extraction(video_id)
        webpage = self._download_webpage(url, video_id)
        #print(webpage)

        vidurl=self._html_search_regex(r'sources: \[{"file":"(https?://.*)"}', webpage, u'Video MP4 Source')

        title = self._og_search_title(webpage)

        if self._downloader.params.get('verbose', False):
        #     self._downloader.to_screen(
        #         '[debug] iframe URL: %s' % (iframe_url))
            self._downloader.to_screen(
                '[debug] Video Source: %s' %(vidurl))
            self._downloader.to_screen(
                '[debug] Title: %s' %(title))

        # iframe=self._download_webpage(iframe_url, video_id)
        # #print(iframe)
        # if (vidsrc == "playbbme.gogoanime.to"):
        #     vidurl=self._html_search_regex(r'var url *= *\'(.*)\' *;', iframe, u'video URL')
        # elif(vidsrc == "playpandanet.gogoanime.to"):
        #     vidurl=self._html_search_regex(r'url: *\'(.*)\',', iframe, u'Video URL')
        # elif(vidsrc == "videozoome.gogoanime.to"):
        #     vidurl=self._html_search_regex(r'file: *"(http.*)",', iframe, u'Video URL')
        # else:
        #     self.report_error("I don't know what to do with vidsrc = %s" % (vidsrc))
        #     print(iframe)
        
        # vidurl=vidurl+"&start=0"
        # if self._downloader.params.get('verbose', False):
        #     self._downloader.to_screen(
        #         '[debug] Video URL: %s' %(vidurl))

        
        return {
            'id': video_id,
            'title': title,
            'url': vidurl
        }


