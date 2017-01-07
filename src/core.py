import os
import time
import urllib
import hashlib
import unittest
from torrent import Torrent

# Client information
CLIENT_ID_STRING = "CO"
CURRENT_VERSION = "0001"

# Networking
LISTENING_PORT_MIN = 6881
LISTENING_PORT_MAX = 6889
MAX_CONNECTIONS = 4
"""
This is the core of the torrent client.
"""
class Core:
	def __init__(self):
		"""
		Dictionary of active torrents
		
		Key value is the name of the torrent file
		Value is a Torrent object
		"""
		self._active_torrents = {}
		self._peer_id = self.generate_peer_id()

	"""
	Outputs a unique 20-byte urlencoded string used as the client identifier

	Uses Azureus-style encoding:
		'-' + (2-char client ID ascii) + (4-char integer version number) + '-'
	"""
	def generate_peer_id(self):
		seed_string = "{}{}{}".format(os.getpgid(0), os.getcwd(), os.getlogin())
		pre_versioned_peer_id = hashlib.sha1(seed_string).hexdigest()
		peer_id_sub = pre_versioned_peer_id[28:]
		
		return "-{}{}-{}".format(CLIENT_ID_STRING,CURRENT_VERSION,peer_id_sub)

"""
Tests
"""

class TestClient(unittest.TestCase):
	def test_peer_id_generation(self):
		test_client = Core()
		test_client.generate_peer_id()
		self.assertEquals(20, len(test_client._peer_id))

if __name__ == "__main__":
	unittest.main()





