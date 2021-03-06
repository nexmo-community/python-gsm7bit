__version__ = '0.9'


class CharError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class Converter():
	def __init__(self):
		self.encode_table = {'937': '15', '67': '43', '102': '66', '232': '4', '93': '1B3E', '923': '14', '167': '5F', '191': '60', '92': '1B2F', '926': '1A', '62': '3E', '35': '23', '86': '56', '79': '4F', '115': '73', '65': '41', '113': '71', '223': '1E', '57': '39', '42': '2A', '54': '36', '74': '4A', '109': '6D', '98': '62', '37': '25', '87': '57', '114': '72', '94': '1B14', '40': '28', '101': '65', '45': '2D', '915': '13', '112': '70', '196': '5B', '44': '2C', '68': '44', '89': '59', '91': '1B3C', '121': '79', '73': '49', '60': '3C', '252': '7E', '165': '3', '936': '17', '117': '75', '85': '55', '124': '1B40', '70': '46', '110': '6E', '50': '32', '916': '10', '34': '22', '241': '7D', '38': '26', '36': '2', '64': '0', '72': '48', '122': '7A', '53': '35', '928': '16', '224': '7F', '76': '4C', '119': '77', '198': '1C', '216': '0B', '8364': '1B65', '105': '69', '71': '47', '116': '74', '41': '29', '48': '30', '69': '45', '220': '5E', '126': '1B3D', '229': '0F', '228': '7B', '58': '3A', '97': '61', '61': '3D', '82': '52', '95': '11', '100': '64', '99': '63', '931': '18', '209': '5D', '201': '1F', '199': '9', '33': '21', '80': '50', '934': '12', '103': '67', '920': '19', '233': '5', '49': '31', '43': '2B', '77': '4D', '88': '58', '32': '20', '230': '1D', '236': '7', '55': '37', '47': '2F', '123': '1B28', '242': '8', '108': '6C', '107': '6B', '163': '1', '81': '51', '46': '2E', '104': '68', '51': '33', '106': '6A', '39': '27', '125': '1B29', '56': '38', '120': '78', '214': '5C', '164': '24', '84': '54', '111': '6F', '118': '76', '63': '3F', '59': '3B', '75': '4B', '52': '34', '248': '0C', '66': '42', '78': '4E', '197': '0E', '161': '40', '249': '6', '246': '7C', '83': '53', '90': '5A'}
		self.decode_table = {'00': '64', '01': '163', '02': '36', '03': '165', '04': '232', '05': '233', '06': '249', '07': '236', '08': '242', '09': '199', '0B': '216', '0C': '248', '0E': '197', '0F': '229', '10': '916', '11': '95', '12': '934', '13': '915', '14': '923', '15': '937', '16': '928', '17': '936', '18': '931', '19': '920', '1A': '926', 'B0A': '49', '1B14': '94', '1B28': '123', '1B29': '125', '1B2F': '92', '1B3C': '91', '1B3D': '126', '1B3E': '93', '1B40': '124', '1B65': '8364', '1C': '198', '1D': '230', '1E': '223', '1F': '201', '20': '32', '21': '33', '22': '34', '23': '35', '24': '164', '25': '37', '26': '38', '27': '39', '28': '40', '29': '41', '2A': '42', '2B': '43', '2C': '44', '2D': '45', '2E': '46', '2F': '47', '30': '48', '31': '49', '32': '50', '33': '51', '34': '52', '35': '53', '36': '54', '37': '55', '38': '56', '39': '57', '3A': '58', '3B': '59', '3C': '60', '3D': '61', '3E': '62', '3F': '63', '40': '161', '41': '65', '42': '66', '43': '67', '44': '68', '45': '69', '46': '70', '47': '71', '48': '72', '49': '73', '4A': '74', '4B': '75', '4C': '76', '4D': '77', '4E': '78', '4F': '79', '50': '80', '51': '81', '52': '82', '53': '83', '54': '84', '55': '85', '56': '86', '57': '87', '58': '88', '59': '89', '5A': '90', '5B': '196', '5C': '214', '5D': '209', '5E': '220', '5F': '167', '60': '191', '61': '97', '62': '98', '63': '99', '64': '100', '65': '101', '66': '102', '67': '103', '68': '104', '69': '105', '6A': '106', '6B': '107', '6C': '108', '6D': '109', '6E': '110', '6F': '111', '70': '112', '71': '113', '72': '114', '73': '115', '74': '116', '75': '117', '76': '118', '77': '119', '78': '120', '79': '121', '7A': '122', '7B': '228', '7C': '246', '7D': '241', '7E': '252', '7F': '224'}
	def encode(self, msg):
		data = list(msg)
		resp = []
		for d in data:
			x =str(ord(d))
			if x not in self.encode_table:
				raise CharError("Character {} Not in GSM 7 Bit Alphabet".format(d))
			c = self.encode_table[x]
			resp.append(c)
		return ''.join(resp)
	def decode(self, msg):
		data = [msg[i:i + 2] for i in range(0, len(msg), 2)]
		resp = []
		while len(data) != 0:
			code = data.pop(0)
			if code == '1B':
				code += data.pop()
			if code not in self.decode_table:
				raise CharError("Unknow Character {} ".format(code))
			x = self.decode_table[code]
			c = chr(int(x))
			resp.append(c)
		return ''.join(resp)
		
		
