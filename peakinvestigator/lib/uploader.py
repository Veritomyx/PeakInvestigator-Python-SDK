## -*- coding: utf-8 -*-
#
# Copyright (c) 2016, Veritomyx, Inc.
#
# This file is part of the Python SDK for PeakInvestigator
# (http://veritomyx.com) and is distributed under the terms
# of the BSD 3-Clause license.
from peakinvestigator.lib import *

class Uploader(object):

    def __init__(self, host, token, progress_factory, log_level=logging.WARNING):
        self.logger = logging.getLogger('Uploader')
        self.logger.setLevel(log_level)
        self.progress_factory = progress_factory
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ssl_sock = ssl.wrap_socket(self.sock)
        server_address = (socket.gethostbyname(host), 9999)

        self.ssl_sock.connect(server_address)
        self.ssl_sock.sendall(token.encode('utf-8'))
        response = self.ssl_sock.recv(4096)
        self.logger.info('Server response:', response)

        if response != 'Authorized'.encode('utf-8'):
            raise Exception('Client not authorized')

        self.buffer = bytearray(4096)

        global Progress
        Progress = eval(progress_factory)

    def upload_filehandle(self, num, filetype, size, handle, progress=None):
        self.ssl_sock.sendall(struct.pack('>I', num))
        self.ssl_sock.sendall(struct.pack('b', filetype))
        self.ssl_sock.sendall(struct.pack('>I', size))

        count = handle.readinto(self.buffer)
        while count > 0:
            self.ssl_sock.sendall(self.buffer[:count])
            if progress:
                progress.update(count)
            count = handle.readinto(self.buffer)

        response = self.ssl_sock.recv(4096)
        if response != 'OK'.encode('utf-8'):
            self.close()
            raise Exception('Problem sending file #{}: {}'.format(num, response))

    def upload_file(self, filename, num, with_progress=True):
        size = os.path.getsize(filename)
        filetype = 0 if filename[-4:] == '.bin' else 1
        progress = Progress(total=size, unit='bytes') if with_progress else None

        with io.open(filename, 'rb') as f:
            self.upload_filehandle(num, filetype, size, f, progress)

        if with_progress:
            progress.close()

    def upload_files(self, filenames, start=0):
        progress = Progress(total=len(filenames))
        for i, filename in enumerate(filenames, start):
            self.upload_file(filename, i, False)
            progress.update(1)
        progress.close()

    def upload_tarfile(self, filename):
        with tarfile.open(filename) as f:
            members = list(filter(lambda x: x.isfile(), f.getmembers()))
            progress = Progress(total=len(members))

            for i, member in enumerate(members):
                filetype = 0 if member.name[-4:] == '.bin' else 1
                self.upload_filehandle(i, filetype, member.size, f.extractfile(member), None)
                progress.update(1)

            progress.close()

    def upload_zipfile(self, filename):
        with zipfile.ZipFile(filename) as f:
            members = list(filter(lambda x: not x.is_dir(), f.infolist()))
            progress = Progress(total=len(members))

            for i, member in enumerate(members):
                filetype = 0 if member.filename[-4:] == '.bin' else 1
                with f.open(member) as entry:
                    self.upload_filehandle(i, filetype, member.file_size, entry, None)
                progress.update(1)

            progress.close()

    def close(self):
        self.ssl_sock.close()
