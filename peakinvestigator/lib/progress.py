## -*- coding: utf-8 -*-
#
# Copyright (c) 2016, Veritomyx, Inc.
#
# This file is part of the Python SDK for PeakInvestigator
# (http://veritomyx.com) and is distributed under the terms
# of the BSD 3-Clause license.
import logging
import time

logging.info('Progress')
class Progress_Factory(object):

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

