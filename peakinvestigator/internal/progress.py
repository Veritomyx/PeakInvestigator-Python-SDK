## -*- coding: utf-8 -*-
#
<<<<<<< HEAD
# Copyright (c) 2016, Veritomyx, Inc.
=======
# Copyright (c) 2016-2018, Veritomyx, Inc.
>>>>>>> uploader_19jan18
#
# This file is part of the Python SDK for PeakInvestigator
# (http://veritomyx.com) and is distributed under the terms
# of the BSD 3-Clause license.
<<<<<<< HEAD
import logging
import time

logging.info('Progress')
class LoggerProgress(object):

    def __init__(self, total, unit='scans'):

        self.total = total
        self.unit = unit
        self.count = 0
        self.clock = time.time()
        self.logger = logging.getLogger('Progress')
        self.logger.setLevel(logging.INFO)
        self.logger.info('Starting upload of {} {}'.format(total, unit))

    def update(self, update):
        self.count += update
        current = time.time()
        if current - self.clock > 30:
            self.logger.info('Finished uploading {} of {} {}.'.format(self.count, self.total, self.unit))
            self.clock = current

    def close(self):
        self.logger.info('Finished upload of {} {}'.format(self.count, self.unit))
=======
from abc import ABC, ABCMeta, abstractmethod

class ProgressFactory(ABC):
    @abstractmethod
    def create(self, total, unit):
        """return an implementation of progress"""
        print("Not implemented")

class Progress(ABC):
    @abstractmethod
    def update(self, update):
        """return an implementation of progress update"""
        print("Not impelemnted")

    @abstractmethod
    def close(self):
        """return an implementation of close progress"""
        print("Not implemented")
>>>>>>> uploader_19jan18
