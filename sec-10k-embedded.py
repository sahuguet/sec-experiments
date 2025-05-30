from lxml import etree
import json
import sys

try:
    xml_file = 'data_10k/pep-20250322.html'
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(xml_file, parser)
    root = tree.getroot()
    nsmap = root.nsmap
    # We fix the nsmap. The default namespace is not handled well by lxml.
    nsmap['d'] = nsmap.pop(None)
    
    FACTS = [ r"ix:nonnumeric[@name='dei:EntityRegistrantName']",
             r"xbrli:identifier[@scheme='http://www.sec.gov/CIK']"
             ]

    for f in FACTS:
        print(root.xpath(f"(//{f}/text())[1]", namespaces=nsmap)[0])

    """Other stuff to extract
    - r'//ix:nonfraction[@name="us-gaap:PropertyPlantAndEquipmentNet"]
    - r'//xbrli:context[@id="c-18"]'
    - root.xpath(r'//xbrli:context[@id="c-18"]//xbrli:instant/text()', namespaces=nsmap)
    """


    //ix:nonfraction[@name="us-gaap:PropertyPlantAndEquipmentNet"] 

    # Now you can work with the parsed HTML
    # For example, you can find elements using XPath:
    # elements = root.xpath('//div[@class="some-class"]')
    
except etree.XMLSyntaxError as e:
    print(f"XML Syntax Error: {e}")
    sys.exit(1)
except FileNotFoundError:
    print(f"File not found: {xml_file}")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)

