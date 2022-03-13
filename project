
import time
import numpy as np
import pandas as pd



CITY_DATA = {'Chicago': 'chicago.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def get_month(filters):
    """
        Asks user to enter name of month if filters is not 'none' or 'day'.

        :param:
            (str) filters - Name of the filter applied, none, both, month or day.

        :return:
            (str) month - Month from 'january' to 'july' to filter data.
                         'All' if user does not want to filter by month.
        """

    if filters == 'None' or filters == 'Day':
        return 'All'

    while True:
        month = input('\nChoose the month by which you want to filter the data:\n1) January' +
                      '\n2) February\n3) March\n4) April\n5) May\n6) June\nPlease input numbers only(1-6):\n')
        month = month.title()
        months = ['January', 'February', 'March', 'April', 'May', 'June']

        # Attempting to decode mnemonic input else prompt for input again
        if month not in months:
            if month == '1':
                month = 'January'
            elif month == '2':
                month = 'February'
            elif month == '3':
                month = 'March'
            elif month == '4':
                month = 'April'
            elif month == '5':
                month = 'May'
            elif month == '6':
                month = 'June'
            else:
                print('Please select any option from (1-7):')
                continue
        break
    return month


def get_day(filters):
    """
    Asks user to enter name of day if filters is not 'none' or 'month'.

    :param:
        (str) filters - Name of the filter applied, none, both, month or day.

    :return:
        (str) day - Day of week to filter data. 'All' if user does not want to filter by day
    """

    if filters == 'None' or filters == 'Month':
        return 'All'

    while True:
        day = input('1) Sunday\n2) Monday\n3) Tuesday\n4) Wednesday\n5) Thursday\n6) Friday' +
                    '\n7) Saturday\nPlease input number (1-7):\n')
        day = day.title()
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        # Attempting to decode mnemonic input else prompt for input again
        if day not in days:
            if day == '1' :
                day = 'Sunday'
            elif day == '2':
                day = 'Monday'
            elif day == '3':
                day = 'Tuesday'
            elif day == '4':
                day = 'Wednesday'
            elif day == '5':
                day = 'Thursday'
            elif day == '6':
                day = 'Friday'
            elif day == '7':
                day = 'Saturday'
            else:
                print('Please select any option from (1-7):')
                continue
        break
    return day


def get_filters():
    """
    Asks user to enter the name of city and select filters from month, day, both or none.

    Calls:
        get_month(filters) - Returns name of month to filter data,
                             or 'All' if no month filter is chosen.
        get_day(filters) - Returns name of day to filter data,
                           or 'All' if no day filter is chosen.

    :returns:
        (str) city - Name of the city to analyze.
        (str) filter - Name of the filters: month, day, both, or none.
        (str) month - Name of the month to filter by, or 'All' to apply no month filter.
        (str) day - Name of the day to filter by, or 'All' to apply no day filter.
    """
    print('Hello! Let\'s explore some US bike-share data.\n')

    # Gets city to filter data
    while True:
        city = input('Choosethe city:\n1) Chicago\n2) New York\n3) Washington\n')
        city = city.title()

        # Decoding mnemonic inputs
        if city == '1':
            city = 'Chicago'
        elif city == '2':
            city = 'New York'
        elif city == '3':
            city = 'Washington'

        # Asking user to input again if unexpected input else continue
        if city == 'Chicago' or city == 'New York' or city == 'Washington':
            print('\nnow we are going to: ', city)
            break
        else:
            print('Please select the fight city .')

    print('----------------------------------------------')
    # Asking user which filter to apply and accepting required values
    while True:
        filters = input('\n1) Month\n2) Day \n3) Both or\n4) None' +
                        '\nChoose filter(1 - 4):\n')
        filters = filters.title()

        options = ['1', '2', '3', '4', 'Month', 'Day', 'Both', 'None']

        # Taking care of invalid filters else getting required values of filters
        if filters not in options:
            print('Please select from  filters')
        else:
            # Decoding mnemonic inputs
            if filters not in options[4:8]:
                if filters == '1':
                    filters = 'Month'
                elif filters == '2':
                    filters = 'Day'
                elif filters == '3':
                    filters = 'Both'
                elif filters == '4':
                    filters = 'None'

            # Providing feedback to users
            print('----------------------------------------------')

            # Getting values for month and day according to selected filter
            month = get_month(filters)
            day = get_day(filters)
            break

    # Displaying the filters to data:

    return city, month, day, filters


def common_month(df):
    """
    :param:
        (data-frame) dataframe - Pandas data-frame containing the travel data points

    :return:
        (str) month - The month which has maximum travel.
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    month = df['Month'].mode()[0]

    month = months[month-1]
    popular_month_count = (df['Month'] == months.index(month) + 1).sum()

    return month, popular_month_count
    

def common_day(df):
    """
    :param:
        (data-frame) dataframe - Pandas data-frame containing the travel data points

    :return:
        (str) day - The day which has maximum travel.
    """
    day = df['Day'].mode()[0]
    popular_day = (df['Day'] == day).sum()

    return day, popular_day


def get_day_number(day):
    """Returns the day number corresponding to day name"""
    day_dict = {
        'Sunday': 0,
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6
    }
    return day_dict[day]


def get_day_name(day_number):
    """Returns the day name corresponding to day number"""
    day_dict = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return day_dict[day_number]


def load_data(city, month, day, filters):
    """
    Loads data and applies the filters

    Displays:
            Some statistics on whole data set before applying filter.
            Most popular month: If filter is 'Month'
            Most popular day: If filter is 'Day'
            Most popular month and day: If filter is 'Both'

    :param:
        (str) city - City whose statistics user want to see.
        (str) month - Month whose statistics user want to see.
        (str) day- Day whose statistics user want to see.
        (str) filters - The filters which user want to apply on data.

    :return:
        (data-frame) dataframe - Data frame containing relevant data after filters are applied.
    """
    print('\n\n*****************LOADING **********************')
    start_time = time.time()

    df = pd.read_csv(CITY_DATA[city])
    print('City: ', city)
    print('Total data points found: ', len(df))

    # Changing start time to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Day'] = df['Start Time'].dt.weekday
    df['Month'] = df['Start Time'].dt.month
    df['Hour'] = df['Start Time'].dt.hour

    # Displaying statistics for whole data
    if filters == 'Month':
        popular_month, count_popular_month = common_month(df)
        print('Most popular month for travelling: ', popular_month)
        print('Counts: ', count_popular_month)

    elif filters == 'Day':
        popular_day, count_popular_day = common_day(df)
        print('Most popular day for travelling: ', get_day_name(popular_day))
        print('Counts: ', count_popular_day)

    elif filters == 'Both':
        popular_month, count_popular_month = common_month(df)
        popular_day, count_popular_day = common_day(df)
        print('\nMost popular month for travelling: ', popular_month)
        print('Counts: ', count_popular_month)
        print('Counts: ', count_popular_day)

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('----------------------------------------------')

    
    start_time = time.time()
    months = ['January', 'February', 'March', 'April', 'May', 'June']

    if filters == 'Month':
        print('Filter:\n        Month = ', month.title())
        df = df[df['Month'] == months.index(month) + 1]
    elif filters == 'Day':
        print('Filter: Day = ', day)
        df = df[df['Day'] == get_day_number(day)]
    elif filters == 'Both':
        print('Filter:\n        Month =  {}\n        Day = {}'.format(month.title(), day))
        df = df[df['Month'] == months.index(month) + 1]
        df = df[df['Day'] == get_day_number(day)]
    else:
        print('Filter: ', filters)

    print('Total data points after applying filter: ', len(df))
    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('----------------------------------------------')

    return df


def time_stats(df, filters):
    """
    Displays statistics of most frequent times of travel.

    :param:
        (data frame) dataframe - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
    """

    print('----------------------------------------------')
    print('  Calculating Most Frequent Times Of Travel')
    
    

    start_time = time.time()
    popular_month, count_popular_month = common_month(df)
    popular_day, count_popular_day = common_day(df)
    popular_hour = df['Hour'].mode()[0]
    count_popular_hour = (df['Hour'] == popular_hour).sum()

    if filters == 'None':
        print('\nMost popular month for travelling: ', popular_month)
        print('Counts: ', count_popular_month)
        print('\nMost popular day for travelling: ', get_day_name(popular_day))
        print('Counts: ', count_popular_day)
        print('\nMost popular hour of day for travelling: ', popular_hour)
        print('Counts: ', count_popular_hour)
    elif filters == 'Both':
        print('\nMost popular hour of day for travelling: ', popular_hour)
        print('Counts: ', count_popular_hour)
    elif filters == 'Month':
        print('\nMost popular day for travelling: ', get_day_name(popular_day))
        print('Counts: ', count_popular_day)
        print('\nMost popular hour of day for travelling: ', popular_hour)
        print('Counts: ', count_popular_hour)
    elif filters == 'Day':
        print('\nMost popular month for travelling: ', popular_month)
        print('Counts: ', count_popular_month)
        print('\nMost popular hour of day for travelling: ', popular_hour)
        print('Counts: ', count_popular_hour)

    print('\nThis took about {} seconds'. format(time.time() - start_time))
    print('----------------------------------------------')


def station_stats(df, filters):
    """
    Displays statistics on most popular station and trip.

    :param:
        (data frame) dataframe - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
    """
    
    print('  Calculating Most Popular Stations & Trips')
    print('----------------------------------------------')
    start_time = time.time()

    print('Most Commonly Used Start Station: ', df['Start Station'].mode()[0])
    print('Counts: ', df['Start Station'].value_counts()[0])
    print('\nMost Commonly Used End Station: ', df['End Station'].mode()[0])
    print('Counts: ', df['End Station'].value_counts()[0])
    print('\nMost Popular Trip: ')

    # Calculating most popular combination of Start and End Stations
    grouped_data = df.groupby(['Start Station',
                               'End Station']).size().to_frame('number').reset_index()
    popular_trip_location_index = grouped_data['number'].idxmax()

    start_station = grouped_data.loc[popular_trip_location_index]['Start Station']
    end_station = grouped_data.loc[popular_trip_location_index]['End Station']
    count = grouped_data['number'].max()

    print('Start Station: {}\nEnd Station: {}\nCounts: {}'.format(start_station,
                                                                  end_station, count))
    print('\nThis took about {} seconds.'.format(time.time() - start_time))
    print('----------------------------------------------')


def trip_duration_stats(df, filters):
    """
    Displays statistics on total and average and total trip duration.

    :param:
        (data frame) dataframe - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
    """

    
    print('          Calculating Trip Duration')
    print('----------------------------------------------')
    start_time = time.time()

    # Calculating trip duration
    total_trip_duration = df['Trip Duration'].sum()
    average_trip_duration = df['Trip Duration'].mean()

    # Displaying total time
    print('Total Duration: {} seconds'.format(total_trip_duration))
    print('Counts: ', df['Trip Duration'].count())

    # Displaying average duration
    print('\nAverage Duration: {} seconds'.format(average_trip_duration))
    print('\nThis took about {} seconds.'.format(time.time() - start_time))
    print('----------------------------------------------')


def user_stats(df, filters):
    """
    Displays statistics on types of users, gender, most recent and most common year of birth.

    :param:
        (data frame) dataframe - The data frame after applying filters
        (str) filters - Filters chosen: Month, Day, Both, or None
    """
    
    print('          Calculating User Statistics')
    print('----------------------------------------------')
    start_time = time.time()

    # Calculating count on user types
    unique_user = df['User Type'].unique()
    unique_user_count = df['User Type'].value_counts()
    total_counted_user = unique_user_count[0] + unique_user_count[1]
    actual_user_count = len(df)

    # Displaying statistics on user types
    print('\n\n------------ User-Type Statistics ------------')
    print('{} : {} or {:.3f} %'.format(unique_user[0], unique_user_count[0],
                                       unique_user_count[0]*100/actual_user_count))
    print('{} : {} or {:.3f} %'.format(unique_user[1], unique_user_count[1],
                                       unique_user_count[1]*100/actual_user_count))

    # Displaying statistics for unknown user type
    if len(unique_user) == 3 and len(unique_user_count) == 3:

        if unique_user[2] == 'Dependent':
            print('{} : {} or {:.3f} %'.format(unique_user[2], unique_user_count[2],
                                               unique_user_count[2]*100/actual_user_count))
        else:
            print('Unknown : {} or {:.3f} %'.format(unique_user_count[2],
                                                    unique_user_count[2]*100/actual_user_count))

    elif len(unique_user) == 3 and len(unique_user_count) != 3:
        other_user_count = actual_user_count - total_counted_user

        if unique_user[2] == 'Dependent':
            print('{} : {} or {:.3f} %'.format(unique_user[2],
                                               other_user_count,
                                               other_user_count*100/actual_user_count))
        else:
            print('Unknown : {} or {:.3f} %'.format(other_user_count,
                                                    other_user_count*100/actual_user_count))

    print('----------------------------------------------')

    # Calculating and displaying statistics on gender
    print('\n\n-------------- Gender Statistics -------------')
    if 'Gender' not in df.columns:
        print('No Gender is found .')
    else:
        counts_of_Genders = df['Gender'].value_counts()
        print('counts of Genders',counts_of_Genders)

    print('----------------------------------------------')

    # Calculating statistics on earliest, most-recent and most common year of birth
    print('\n\n------------ Birth Year Statistics -----------')

    if 'Birth Year' not in df.columns:
        print('No Data is found for Birth Year.')
    else:
        most_earliest_birth_year = int(df.loc[df['Birth Year'].idxmin()]['Birth Year'])
        most_recent_birth_year = int(df.loc[df['Birth Year'].idxmax()]['Birth Year'])
        most_common_birth_year =int(df['Birth Year'].mode()[0])
        most_common_birth_year_counts =(df['Birth Year'] == most_common_birth_year).sum()

        print('Most earliest birth year: ', most_earliest_birth_year)
        print('Most recent birth year: ', most_recent_birth_year)
        print('Most common birth year: ', most_common_birth_year)
        print('Counts: ', most_common_birth_year_counts)

    print('----------------------------------------------')
    print('\nThis took about {} seconds.'.format(time.time() - start_time))
    print('----------------------------------------------')

def show_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 5 (show_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1    # use index values for rows

    print('do you like to see some data ?')
    while True:
        show = input('  1)yes 2)no:  ')
        if show.lower() == 'y'or show =='1':
            # display show_rows number of lines, but display to user as starting from row as 1
            # e.g. if rows_start = 0 and rows_end = 4, display to user as "rows 1 to 5"
            print('\n   show will start from row {} to {}:'.format(rows_start + 1, rows_end + 1))

            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows

            
            print('\n    Would you like to see the next {} rows?'.format(show_rows))
            continue
        else:
            break



def main():
    """
    Main function to call other functions to get data, filters,
    and for showing and visualizing different statistics.
    """
    while True:
        city, month, day, filters = get_filters()
        df = load_data(city, month, day, filters)

        print('\n\n************DISPLAYING STATISTICS*************')
        time_stats(df, filters)
        station_stats(df, filters)
        trip_duration_stats(df, filters)
        user_stats(df, filters)
        show_data(df)

        # To restart or quit program
        restart = input('\nWould you like to restart? Enter 1)yes 2)no.\n')
        if restart.lower() != 'yes' or restart !='1':
            print('thank you we hope to see you soon \n           goodbye sur')
            break


if __name__ == '__main__':
    main()
