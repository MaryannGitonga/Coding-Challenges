class RESP():
    def deserialize(self, message):
        if message[0] == '+':
            return message[1:].strip()
        elif message[0] == '-':
            return 'error'
        elif message[0] == ':':
            return 'integer'
        elif message[0] == '$':
            return 'bulk string'
        elif message[0] == '*':
            return 'array'
    