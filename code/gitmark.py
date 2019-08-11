from ctypes import *
import os
import sys
import platform

sysname = platform.system()

if sysname == 'Darwin':
    libname = "libcmark-gfm.dylib"
elif sysname == 'Windows':
    libname = "cmark.dll"
else:
    libname = "libcmark.so"
file_path = os.path.join('cmark-gfm', 'build', 'src', libname)
cmark = CDLL(file_path)

markdown = cmark.cmark_markdown_to_html
markdown.restype = c_char_p
markdown.argtypes = [c_char_p, c_long, c_long]

opts = 0 # defaults


class CMarkGFM:

    @staticmethod
    def md2html(text):
        if sys.version_info >= (3,0):
            textbytes = text.encode('utf-8')
            textlen = len(textbytes)
            retval = markdown(textbytes, textlen, opts).decode('utf-8')
            return cast(retval, c_char_p).value
        else:
            textbytes = text
            textlen = len(text)
            retval = markdown(textbytes, textlen, opts)
            return cast(retval, c_char_p).value


sys.stdout.write(CMarkGFM.md2html(sys.stdin.read()))
