#!/usr/bin/env python

import warnings
warnings.filterwarnings('ignore')

from sys import path, stderr
from os.path import abspath
path.insert(0, abspath('src'))

from shutil import move, rmtree
from os import makedirs

from distutils.core import setup
from distutils.command.build import build as _build

from subprocess import Popen

import controlsystems

class build(_build):
    
    def run(self):
        """Build documentation for this package, using epydoc,
        if installed.
        
        """
        
        # dirty hack to hide warnings
        devnull = open('/dev/null', 'w')
        
        html_cmd = []
        html_cmd.append('--name="%s"' % controlsystems.__name__)
        html_cmd.append('-q')
        html_cmd.append(abspath('src/%s' % controlsystems.__name__))
        
        pdf_cmd = html_cmd[:]
        
        html_cmd.insert(2, '--html')
        html_cmd.insert(3, '--no-frames')
        html_cmd.insert(4, '-o%s' % abspath('doc/html'))
        
        print 'building html doc'
        
        try:
            makedirs('doc/html')
        except:
            pass
        
        try:
            child = Popen(html_cmd, executable='epydoc', stdout=devnull)
        except:
            print >> stderr, 'epydoc don\'t installed.'
        else:
            
            ret = child.wait()
            
            if ret:
                print >> stderr, 'failed to build html doc.'
            
            pdf_cmd.insert(2, '--pdf')
            pdf_cmd.insert(3, '-o%s' % abspath('doc/tmp'))
            
            print 'building pdf doc'
            
            try:
                makedirs('doc/tmp')
            except:
                pass
            
            child = Popen(pdf_cmd, executable='epydoc', stdout=devnull)
            ret = child.wait()
        
            if ret:
                print >> stderr, 'failed to build pdf doc.'
            else:
                try:
                    move('doc/tmp/api.pdf', 'doc/%s.pdf' % \
                        controlsystems.__name__)
                except:
                    pass
            
                rmtree('doc/tmp')
        
        _build.run(self)
        

setup(
    cmdclass={'build': build},
    name=controlsystems.__name__,
    version=controlsystems.__version__,
    license=controlsystems.__license__,
    description=controlsystems.__description__,
    author=controlsystems.__author__,
    author_email=controlsystems.__email__,
    url=controlsystems.__url__,
    packages=[controlsystems.__name__],
    package_dir={
        controlsystems.__name__: 'src/%s' % controlsystems.__name__
    },
)
