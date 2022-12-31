import pandas as pd

def join_data(data_path_1, data_path_2, labl_1=None, labl_2=None, labl_3=None):
    """
        Merges and processes two dataframes with neighborhood information.

        Parameters:
        data_path_1 (str): Path to the first CSV file.
        data_path_2 (str): Path to the second CSV file.
        labl_1 (str, optional): New name for the 'label' column in the first dataframe.
        labl_2 (str, optional): New name for the 'label_x' column in the first dataframe.
        labl_3 (str, optional): New name for the 'label_y' column in the second dataframe.

        Returns:
        None
        """
    # Load the data
    df = pd.read_csv(data_path_1)
    df2 = pd.read_csv(data_path_2)

    #check if the dataframe has column cluster and remove it if exists
    df.drop(columns=['cluster'], inplace=True, errors='ignore')
    df2.drop(columns=['cluster'], inplace=True, errors='ignore')

    # merge the data frames and column name from the second data frame should have the name of tha table
    df = df.merge(df2, on=['district_code','neighbourhood_code'], how='outer')

    #if district_name_y and neighbourhood_name_y exist, drop them
    df.drop(columns=['district_name_y', 'neighbourhood_name_y', 'district_name', 'neighbourhood_name'], inplace=True, errors='ignore')

    # check if label_x and label_y columns exist and rename the column name lable_x and lable_y to lable_1 and lable_2
    df.rename(columns={'label': 'label_' + str(labl_1)}, inplace=True, errors='ignore')
    df.rename(columns={'label_x': 'label_' + str(labl_2)}, inplace=True, errors='ignore')
    df.rename(columns={'label_y': 'label_' + str(labl_3)}, inplace=True, errors='ignore')

    # Save the result
    df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv', index=False)

if __name__ == '__main__':

    # 1: accidents & avg_occup
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_2021_accidents.csv',
    #          '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_2022_avg_occup_homes.csv',
    #          labl_2= 'accidents', labl_3='avg_occ')

    # 2: 1 & above_65
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    #         '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_above_65t.csv',
    #          labl_1='above_65')

    # 3: 2 & academic_level
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    #           '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_academic_level.csv',
    #           labl_1='academic_level')

    # 4: 3 & between_18_64
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    #           '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_between_18_64.csv',
    #           labl_1='between_18_65')

    # 5: 4 & bus_stops
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    #           '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_bus_stops.csv',
    #           labl_1='bus_stops')

    # 6: 5 & children_play_area
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    #           '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_children_play_areas.csv',
    #           labl_1='children_play_areas')

    # 7: 6 & cinema_theatre
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    # '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_cinema_theater_concerts.csv',
    # labl_1='cinema_theatre_concerts')

    # 8: 7 & cultural_leisure
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    # '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_culture_leisure_spaces.csv',
    # labl_1='cultural_leisure_spaces')

    # 9: 8 & library_studyroom
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    # '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_library_studyroom_museum_spaces.csv',
    # labl_1='library_studyroom')

    # 10: 9 & rent_price
    # join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
    # '/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_rent_price.csv',
    # labl_1='rent_price')

     # 11: 10 & sport_facilities
     #join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
     #'/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labeled_sport_facilities.csv',
     #labl_1='sport_facilities')

     # 12: 11 & tourists_points
     #join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
     #'/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labeled_tourists_points.csv',
     #labl_1='tourists_points')

     # 13: 12 & transportation
     #join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
     #'/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labeled_transportation.csv',
     #labl_1='transportation')

    # 14: 13 & street_markets
     #join_data('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv',
     #'/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/clustering/labled/labled_temporaray_exhibitions.csv',
     #labl_1='street_markets_and_fairs')



    # df = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv')
    # df = df.drop(columns=['label_cat'])
    # df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv', index=False)