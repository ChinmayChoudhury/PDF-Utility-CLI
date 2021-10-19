import sys
import argparse
import subprocess
from . import __version__

'''
Compression Levels

0:  /default selects output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file. 
1:  /screen selects low-resolution output similar to the Acrobat Distiller (up to version X) "Screen Optimized" setting.
2:  /ebook selects medium-resolution output similar to the Acrobat Distiller (up to version X) "eBook" setting.
3:  /printer selects output similar to the Acrobat Distiller "Print Optimized" (up to version X) setting.
4:  /prepress selects output similar to Acrobat Distiller "Prepress Optimized" (up to version X) setting.

source: https://www.ghostscript.com/doc/current/VectorDevices.htm 
'''


def main():
    print("Thank you for using this PDF Utility tool")
    print("This is created by Chinmay")
    print("Github: https://github.com/ChinmayChoudhury/PDF-Utility-CLI")

    # comphelp = "0:  /default selects output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file.\n1:  /screen selects low-resolution output similar to the Acrobat Distiller (up to version X) \"Screen Optimized\" setting.\n2:  /ebook selects medium-resolution output similar to the Acrobat Distiller (up to version X) \"eBook\" setting.\n3:  /printer selects output similar to the Acrobat Distiller \"Print Optimized\" (up to version X) setting.\n4:  /prepress selects output similar to Acrobat Distiller \"Prepress Optimized\" (up to version X) setting."
    comphelp = "(default=)0:  /default 1:  /screen 2:  /ebook 3:  /printer 4:  /prepress"

    parser = argparse.ArgumentParser()
    parser.add_argument("input",help="Input pdf/ps(postscript) file")
    parser.add_argument("--output",'-o',default="pdfutilc_output.pdf",help="Output file name/path. [Default = pdfutilc_output.pdf]")
    parser.add_argument("--complevel",type=int,choices=[0,1,2,3,4], default=0, help="Choose the compression level."+comphelp)
    parser.add_argument("--version","-v",action="version",version='pdfutilc v{}'.format(__version__))

    args = parser.parse_args()
    
    print("Input file name:",args.input)
    print("Output file name:",args.output)
    print("Compression level:",args.complevel)

    complevels = {
        0: '/default', 1: '/screen', 2:'/ebook', 3:'/printer', 4:'/prepress'
    }
    # subprocess.call(['gswin64c.exe', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
    #                 '-dPDFSETTINGS={}'.format(complevels[args.complevel]),
    #                 '-dNOPAUSE', '-dQUIET', '-dBATCH',
    #                 "-sOutputFile={}".format(args.output),"'{}'".format(args.input)])
    isgsavail = subprocess.run('gswin64c.exe -v',shell=True, capture_output=True, text=True)
    if isgsavail.returncode == 1:
        print("Cannot find GhostScript, kindly install/repair GhostScript.")
        print("If already installed check if gs is added to path")
        exit()
    else:
        print("GhostScript available on system. Program can proceed")
    subprocess.call(['gswin64c.exe', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(complevels[args.complevel]),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    "-sOutputFile={}".format(args.output),args.input])