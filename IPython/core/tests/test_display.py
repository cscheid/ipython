#-----------------------------------------------------------------------------
#  Copyright (C) 2010-2011 The IPython Development Team.
#
#  Distributed under the terms of the BSD License.
#
#  The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
import os

import nose.tools as nt

from IPython.core import display
from IPython.utils import path as ipath

def test_image_size():
    """Simple test for display.Image(args, width=x,height=y)"""
    thisurl = 'http://www.google.fr/images/srpr/logo3w.png'
    img = display.Image(url=thisurl, width=200, height=200)
    nt.assert_equal(u'<img src="%s" width="200" height="200"/>' % (thisurl), img._repr_html_())
    img = display.Image(url=thisurl, width=200)
    nt.assert_equal(u'<img src="%s" width="200"/>' % (thisurl), img._repr_html_())
    img = display.Image(url=thisurl)
    nt.assert_equal(u'<img src="%s"/>' % (thisurl), img._repr_html_())

def test_image_filename_defaults():
    '''test format constraint, and validity of jpeg and png'''
    tpath = ipath.get_ipython_package_dir()
    nt.assert_raises(ValueError, display.Image, filename=os.path.join(tpath, 'testing/tests/badformat.gif'),
                     embed=True)
    nt.assert_raises(ValueError, display.Image)
    nt.assert_raises(ValueError, display.Image, data='this is not an image', format='badformat', embed=True)
    imgfile = os.path.join(tpath, 'frontend/html/notebook/static/base/images/ipynblogo.png')
    img = display.Image(filename=imgfile)
    nt.assert_equal('png', img.format)
    nt.assert_is_not_none(img._repr_png_())
    img = display.Image(filename=os.path.join(tpath, 'testing/tests/logo.jpg'), embed=False)
    nt.assert_equal('jpeg', img.format)
    nt.assert_is_none(img._repr_jpeg_())
