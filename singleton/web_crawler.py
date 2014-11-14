#!/usr/bin/python

import httplib2
import os
import re
import threading
import urllib
from urlphase import urlparse, urljoin
from BeautifulSoup import BeautifulSoup

class Singleton(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance


# Then we create a class for creating a thread, in this thread we will download images

class ImageDownloaderThread(threading.Thread):
	"""A thread for downloading images in parallel"""
	def __init__(self, thread_id, name, counter):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		print 'Starting thread ', self.name
		download_images(self.name)
		print 'Finished thread ', self.name

	def traverse_site(max_links = 10):
		link_parser_singleton = Singleton()

		# While we have pages to parse in the queue.
		while link_parser_singleton.queue_to_parse:
			if len(link_parser_singleton.to_visit) == max_links:
				return
			url = link_parser_singleton.queue_to_parse.pop()
			http = httplib2.Http()
			try:
				status, response = http.request(url)
			except Exception:
				continue
			if status.get('content-type') != 'text/html':
				continue

			# Add the link to the queue for downloading images.

			link_parser_singleton.to_visit.add(url)
			print 'Added', url, 'to queue'

			bs = BeautifulSoup(response)

			for link in BeautifulSoup.findAll(bs, 'a'):
				link_url = link.get('href')
				# image tag may not contain the href attribute
				if not link_url:
					continue

				parsed = urlparse(link_url)

				# If link follows to external webpage, then skip ImageDownloaderThread

				if parsed.netloc and parsed.netloc != parsed_root.netloc:
					continue

				link_url = (parsed.scheme or parsed_root.scheme) + '://' + (parsed.netloc or parsed_root.netloc) + parsed.path or ''

				if link_url in link_parser_singleton.to_visit:
					continue

				link_parser_singleton.queue_to_parse = [link_url] + link_parser_singleton.queue_to_parse

	def download_images(thread_name):
		singleton = Singleton()
		while singleton.to_visit:
			url = singleton.to_visit.pop()

			http = httplib2.Http()
			print thread_name, 'Starting downloading images from', url

			try:
				status, response = http.request(url)
			except Exception:
				continue

			bs = BeautifulSoup(response)

			# Find all images tag

			images = BeautifulSoup.findAll(bs, 'img')

			for image in images:
				src = image.get('src')
				# Construct the full url
				src = urljoin(url, src)

				basename = os.path.basename(src)

				if src not in singleton.downloaded:
					singleton.downloaded.add(src)
					print 'Downloading', src

				urllib.urlretrieve(src, os.path.join('images', basename))
			print thread_name, 'finished downloading images from', url

# Client code

if __name__ == '__main__':tp://python.org

parsed_root = urlphase(root)

singleton = Singleton()
singleton.queue_to_parse = [root]

singleton.to_visit = set()
singleton.downloaded = set()

traverse_site()

if not os.path.exists('iamges'):
	os.makedirs('images')

thread1 = ImageDownloaderThread(1, "Thread-1", 1)
thread2 = ImageDownloaderThread(2, "Thread-2", 2)

# Start new threads

thread1.start()
thread2.start()
