class RESP():
    def deserialize(self, message):
        if message[0] == '+':
            return message[1:].strip()
        elif message[0] == '-':
            return message[1:].strip()
        elif message[0] == ':':
            if message[1] == '+':
                return int(message[2:].strip())
            else:
                return int(message[1:].strip())
        elif message[0] == '$':
            return 'bulk string'
        elif message[0] == '*':
            return 'array'
    