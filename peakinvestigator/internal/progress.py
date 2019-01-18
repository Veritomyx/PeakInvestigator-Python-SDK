## -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2018, Veritomyx, Inc.
#
# This file is part of the Python SDK for PeakInvestigator
# (http://veritomyx.com) and is distributed under the terms
# of the BSD 3-Clause license.
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