#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
try:
	# Python 3
    from urllib.request import Request, urlopen, URLError
except ImportError:
	# Python 2
    from urllib2 import Request, urlopen, URLError

page_id = 133531496686855
post_id = 1295249200515073
access_token = "EAACEdEose0cBAIVh53ZCoSzx2Qd37VAkVZAjw5WF693p0k9XLyO6TOaxNXs6p8GQZChvSaaZB52Cv6MU5rCuv98c1OcWwvKpChajvwp4rLSPdu2oZAqIX98xBGDrCCQLUHC8ZCtFjdraAkmUXKN6MSinYYHlMZBu5eLSZCG45h9dXiflZAL7ZCLvrVJXV3ZCirn3pgZD"

def facebook_post(page_id, post_id, access_token=access_token):
	q = Request('https://graph.facebook.com/v2.8/%s_%s?fields=created_time,message,link,attachments,comments.limit(40){from,created_time,message,attachment,comments{from,created_time,message,attachment}}&access_token=%s' % (page_id, post_id, access_token))
	try:
		data = urlopen(q).read()
	except URLError as err:
		#print(err.info())
		#raise err  # Use when part of larger app, or don't to render error message that could contain the token!
		return str(err.read(), 'utf8')
	jso = json.loads(str(data, 'utf8'))
	#print("<pre><code>%s</code></pre>" % json.dumps(jso, indent=4, sort_keys=False))

	# Optional fancy templating
	return """<ul>
		<li>
			<p>{nice_time}</p>
			<p>{message}</p>
			<p>{attachments}</p>
			<p>Comments:</p>
			<ul>
				<li><pre><code>{pretty_comments}</code></pre></li>
			</ul>
		</li>
	</ul>
	""".format(nice_time=jso['created_time'].replace('T', ' '), pretty_comments=json.dumps(jso['comments'], indent=4, sort_keys=False), **jso)

#print(facebook_post(page_id, post_id, access_token))