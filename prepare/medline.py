# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import utils

"""
* download from
 http://www.nlm.nih.gov/bsd/sample_records_avail.html
* ftp site
 ftp://ftp.nlm.nih.gov/nlmdata/sample/medline/

python ftplib doesn't support ftp, so download from small sample file.
so if data is not enough, please download from ftp and run parse_xml function.
"""

MEDLINE_FTP = "http://www.nlm.nih.gov/databases/dtd/medsamp2014.xml"
MEDLINE_XML = "madline.xml"
MEDLINE_TXT = "medline.txt"


def main():
    path = utils.DATASET_HOME + MEDLINE_XML
    utils.download(MEDLINE_FTP, path)
    write_xml(path)


def write_xml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    abstracts = root.findall(".//AbstractText")
    texts = []
    for el in abstracts:
        texts.append([el.text])

    utils.write_file(MEDLINE_TXT, texts)


if __name__ == "__main__":
    main()