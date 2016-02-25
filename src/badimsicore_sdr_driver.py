#!/usr/bin/python3.4

"""
    BadIMSICoreSdrDriver is an interface providing only one method :
    init_bts(). This method realizes SDR initialization.
"""

__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team" 


class BadIMSICoreSdrDriver:

    def init_bts(self):
        """
        You should override this method when you subclass BadIMSICoresSdrDriver
        """

