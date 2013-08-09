from metadown.collectors.thredds import ThreddsCollector
from metadown.downloader import XmlDownloader

import os
import sys

def main(base_download_path):

    # selects: The ID in THREDDS needs to contain one of these strings to be identified.
    # skips: The LINK path in the actual thredds catalog webpage can't be equal to any of these strings
    
    # We only want the Agg selects
    selects = [".*SST-Agg", "SST-.*-Agg"]
    isos = ThreddsCollector("http://tds.maracoos.org/thredds/SST.html", selects=selects, debug=True).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)

    # We only want the Agg selects
    selects = [".*MODIS-Agg", ".*MODIS-.*-Agg"]
    isos = ThreddsCollector("http://tds.maracoos.org/thredds/MODIS.html", selects=selects, debug=True).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)

    # We only want the Agg selects
    selects = [".*Forecast_Aggregation_Collection_best.ncd"]
    isos = ThreddsCollector("http://tds.maracoos.org/thredds/Weatherflow.html", selects=selects, debug=True).run()
    download_path = os.path.join(base_download_path, "Models", "Weatherflow")
    XmlDownloader.run(isos, download_path)

    # We only want the all year best selects
    selects = ["Rutgers_WRF_.*"]
    isos = ThreddsCollector("http://tds.maracoos.org/thredds/RUCOOL.html", selects=selects, debug=True).run()
    download_path = os.path.join(base_download_path, "Models", "RUWRF")
    XmlDownloader.run(isos, download_path)

    # We want everything that isn't skipped
    selects = [".*"]
    skips = ThreddsCollector.SKIPS
    isos = ThreddsCollector("http://colossus.dl.stevens-tech.edu/thredds/catalog.html", selects=selects, skips=skips, debug=True).run()
    download_path = os.path.join(base_download_path, "Models", "NYHOPS")
    XmlDownloader.run(isos, download_path)
    
    # We want everything that isn't skipped
    selects = [".*"]
    skips = [".*Forcing Files.*"] + ThreddsCollector.SKIPS
    isos = ThreddsCollector("http://tds.marine.rutgers.edu/thredds/roms/espresso/catalog.html", selects=selects, skips=skips, debug=True).run()
    download_path = os.path.join(base_download_path, "Models", "ESPRESSO")
    XmlDownloader.run(isos, download_path)

    # We want everything that isn't skipped
    selects = [".*"]
    skips = ThreddsCollector.SKIPS
    isos = ThreddsCollector("http://aqua.smast.umassd.edu:8080/thredds/catalog/pe_tnbc/fmrc/catalog.html", selects=selects, skips=skips, debug=True).run()
    download_path = os.path.join(base_download_path, "Models", "HOPS_TNBC")
    XmlDownloader.run(isos, download_path)
    
    # We want everything that isn't skipped
    selects = [".*"]
    skips = ThreddsCollector.SKIPS
    isos = ThreddsCollector("http://aqua.smast.umassd.edu:8080/thredds/catalog/pe_shelf_ass/fmrc/catalog.html", selects=selects, skips=skips, debug=True).run()
    download_path = os.path.join(base_download_path, "Models", "HOPS_PESHELF_ASS")
    XmlDownloader.run(isos, download_path)

    # We want the Best datasets
    selects = [".*best.ncd"]
    isos = ThreddsCollector("http://geoport.whoi.edu/thredds/COAWST_catalog.html", selects=selects, debug=True).run()
    download_path = os.path.join(base_download_path, "Models", "COAWST")
    XmlDownloader.run(isos, download_path)

    # We want everything that isn't skipped
    selects = ["macoora6km_codar_archive", ".*best.ncd"]
    isos = ThreddsCollector("http://tds.marine.rutgers.edu/thredds/cool/codar/cat_totals.html", selects=selects, debug=True).run()
    download_path = os.path.join(base_download_path, "Hfradar")
    XmlDownloader.run(isos, download_path)


main(sys.argv[1])

exit(0)
