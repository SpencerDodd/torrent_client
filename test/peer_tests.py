import unittest
from bitarray import bitarray

from coast.peer import Peer
from coast.piece import Piece
from coast.messages import BitfieldMessage
from coast.helpermethods import convert_hex_to_int
from test.test_data import test_bitfield, test_peer_chunk, test_torrent, test_piece_message


class TestPeer(unittest.TestCase):
	def test_initialization(self):
		test_peer = Peer(test_torrent, test_peer_chunk)
		expected_peer_ip = "78.230.205.50"
		expected_peer_port = 50500
		self.assertEqual(expected_peer_ip, test_peer.ip)
		self.assertEqual(expected_peer_port, test_peer.port)

	def test_bitfield(self):
		print ("-"*60)
		print ("-"*60)
		print ("TESTS FOR `test_bitfield`")
		print ("-"*60)
		print ("-"*60)
		test_peer = Peer(test_torrent, test_peer_chunk)
		test_peer.peer_id = "test_bitfield"

		test_peer.process_bitfield_message(BitfieldMessage(data=test_bitfield))
		self.assertEqual(test_peer.bitfield, bitarray("1"*(380*8)))

	def test_get_next_messages_outgoing_message_removal(self):
		print ("-"*60)
		print ("-"*60)
		print ("TESTS FOR `test_get_next_messages_outgoing_message_removal`")
		print ("-"*60)
		print ("-"*60)
		test_peer = Peer(test_torrent, test_peer_chunk)
		test_peer.peer_id = "test_outgoing_messages"
		print (test_peer.status())
		test_peer.get_next_messages()
		test_peer.process_bitfield_message(BitfieldMessage(test_bitfield))
		test_piece = Piece(
			piece_length=test_torrent.metadata["piece_length"],
			index=0,
			hash=test_torrent.pieces_hashes[0],
			download_location=test_torrent.download_root
		)
