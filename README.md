# PDF-Utility-CLI

A PDF utility tool that uses Ghostscript to manipulate PDFs. 

## Features
1. PDF compression

More features will be added.

## Installation

Install Ghostscript [Download Ghostscript](https://www.ghostscript.com/download/gsdnld.html)
Add Ghostscript to path

Run: `pip install .`

Check installation by using `pdfutilc -v`

## Usage

Run help to see commands:
`pdfutilc -h`

`Thank you for using this PDF Utility tool
This is created by Chinmay
usage: pdfutilc [-h] [--output OUTPUT] [--complevel {0,1,2,3,4}] [--version]
                input

positional arguments:
  input                 Input pdf/ps(postscript) file

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file name/path. [Default = pdfutilc_output.pdf]
  --complevel {0,1,2,3,4}
                        Choose the compression level.(default=)0: /default 1:
                        /screen 2: /ebook 3: /printer 4: /prepress
  --version, -v         show program's version number and exit`



