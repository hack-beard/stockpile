from base64 import b64encode

from app.utility.base_world import BaseWorld


class Obfuscation(BaseWorld):

    def __init__(self, agent):
        self.agent = agent

    def run(self, cmd):
        if self.agent.platform == 'windows':
            return self.psh(cmd)
        return self.bash(cmd)

    def psh(self, code):
        recoded = b64encode(self.decode_bytes(code).encode('UTF-16LE'))
        return 'powershell -Enc %s' % recoded.decode('utf-8')

    @staticmethod
    def bash(code):
        return 'eval "$(echo %s | base64 --decode)"' % str(code.encode(), 'utf-8')
