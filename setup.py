from distutils.core import setup
import py2exe
import numpy

setup(name='YeragoPersonalColorExec',
      version='0.1',
      windows=[{'script': r'mainModule.py'}],
      options={
          'py2exe': {
              # 'packages': ['cv2'],
              'includes': ['numpy',
                           'cv2',
                           'Tkinter'],
    }
})