# -*- coding: utf-8 -*-
from __future__ import absolute_import
from konlpy import utils

import os


class CorpusLoader():
    """Loader for corpora.
    For a complete list of corpora available in KoNLPy,
    refer to :ref:`corpora`.

    .. code-block:: python

        >>> from konlpy.corpus import kolaw
        >>> fids = kolaw.fileids()
        >>> fobj = kolaw.open(fids[0])
        >>> print fobj.read(140)
    """

    def abspath(self, filename=None):
        """Absolute path of corpus file.
        If ``filename`` is *None*, returns absolute path of corpus.

        :param filename: Name of a particular file in the corpus.
        """
        basedir = '%s/data/corpus/%s' % (utils.installpath, self.name)
        if filename:
            return '%s/%s' % (basedir, filename)
        else:
            return '%s/' % basedir

    def fileids(self):
        """List of file IDs in the corpus."""
        return os.listdir(self.abspath())

    def open(self, filename):
        """Method to open a file in the corpus.
        Returns a file object.

        :param filename: Name of a particular file in the corpus.
        """
        return utils.load_txt(self.abspath(filename))

    def __init__(self, name=None):
        if not name:
            raise Exception("You need to input the name of the corpus")
        else:
            self.name = name


kolaw = CorpusLoader('kolaw')
kobill = CorpusLoader('kobill')
