import requests
import pandas as pd
import util_functions as uf


def pull_dc_clusters_info():
    # Load CaBI region information from API
    dc_clusters_url = "https://opendata.arcgis.com/datasets/f6c703ebe2534fc3800609a07bad8f5b_17.geojson"
    dc_clusters = requests.get(dc_clusters_url).json()
    feature_df_list = []
    for enum, feature in enumerate(dc_clusters['features']):
        properties_df = pd.DataFrame(feature['properties'], index=[enum])
        geometry_df = pd.DataFrame(feature['geometry'], index=[enum]).drop(['type'], axis=1)
        feature_df = pd.concat([properties_df, geometry_df], axis=1)
        feature_df_list.append(feature_df)
    dc_clusters_df = pd.concat(feature_df_list, axis=0)
    return dc_clusters_df


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Pull CaBi System Regions
    dc_clusters_df = pull_dc_clusters_info()
    print(dc_clusters_df['coordinates'].map(len).max())
    # Output dataframe as CSV
    outname = "DC_NGH_Clusters"
    dc_clusters_df.to_csv(outname + ".csv", index=False, sep='|')
    # Load to Database
    uf.aws_load(outname, "dc_ngh_clusters", cur)
    # Commit changes to database
    conn.commit()
