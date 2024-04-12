import pandas as pd
from seoul_city_extractor import SeoulExtractor

from private import SeoulPrivate
from assets import area_cds

if __name__ == "__main__":
    seoul_extractor = SeoulExtractor(SeoulPrivate.api_key)

    pptln = list()
    road_traffic_meta = list()
    road_traffic_detail = list()

    for area_cd in area_cds:
        seoul_extractor.load_resp(area_cd)

        pptln.append(seoul_extractor.get_pptln_df())
        road_traffic_meta.append(seoul_extractor.get_road_traffic_meta_df())
        road_traffic_detail.append(
            seoul_extractor.get_road_traffic_detail_df()
        )
    pd.concat(pptln, axis=0).to_csv("./pptln_df.csv")
    pd.concat(road_traffic_meta, axis=0).to_csv("./road_traffic_meta_df.csv")
    pd.concat(road_traffic_detail, axis=0).to_csv("./road_traffic_detail_df.csv")
