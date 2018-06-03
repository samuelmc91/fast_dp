import os

class _writer:
    '''A specialist class to write to the screen and fast_dp.log.'''

    def __init__(self):
        self._fout = None
        return

    def __del__(self):
        if self._fout:
            self._fout.close()
        self._fout = None
        return

    def __call__(self, record):
        self.write(record)

    def write(self, record):
        if not self._fout:
            self._fout = open('fast_dp_pro.log', 'w')

        self._fout.write('%s\n' % record)
        print record
        return

write = _writer()
