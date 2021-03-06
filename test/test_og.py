import osm2gmns as og
import os

map_folder = r'..\maps\asu'

net = og.getNetFromOSMFile(os.path.join(map_folder,'asu.osm'),network_type=('auto','railway','aeroway'),POIs=True,default_lanes=True,default_speed=True)
og.connectPOIWithNet(net)
og.outputNetToCSV(net, output_folder=map_folder)
