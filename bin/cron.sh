#!/usr/bin/env bash

curl -s "http://feeds.technorati.com/search/http%3A%2F%2Fmichilu.com" >static/temp/technorati
curl -s "http://del.icio.us/rss/MiCHiLU" >static/temp/delicious
curl -s "http://api.flickr.com/services/feeds/photos_public.gne?id=66294481@N00" >static/temp/flickr
curl -s "http://michilu.vox.com/library/books/atom.xml" >static/temp/vox
curl -s -A Mozilla  "http://www.amazon.co.jp/gp/richpub/listmania/fullview/R15CIMMN69Q00N" >static/temp/gadgets_
iconv -f SJIS -t UTF8 static/temp/gadgets_ >static/temp/gadgets
