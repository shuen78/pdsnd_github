import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('Would you like to see data for New York City, Chicago, or Washington?\n').lower()

    while city not in CITY_DATA:
        print('Sorry that is not a valid input. Please try again.')
        city = input('Would you like to see data for New York City, Chicago, or Washington?\n').lower()

    valid_month_responses = ['jan','feb','mar','apr','may','jun','all']

    month = input('Which month would you like to view data for? Please enter: Jan, Feb, Mar, Apr, May, Jun, or All.\n').lower()

    while month not in valid_month_responses:
        print('Sorry that is not a valid input. Please Try again.')
        month = input('Which month would you like to view data for? Please enter: Jan, Feb, Mar, Apr, May, Jun, or All.\n').lower()

    valid_day_responses = ['mon','tue','wed','thu','fri','sat','sun', 'all']

    day = input('Which day would you like to view data for? Please enter: Mon, Tue, Wed, Thu, Fri, Sat, Sun, or All.\n').lower()

    while day not in valid_day_responses:
        print('Sorry that is not a valid input. Please Try again.')
        day = input('Which day would you like to view data for? Please enter: Mon, Tue, Wed, Thu, Fri, Sat, Sun, or All.\n').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:

    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:
    df - Pandas DataFrame containing city data filtered by month and day
    """


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':

    # use the index of the months list to get the corresponding int
        months = ['jan','feb','mar','apr','may','jun','all']
        month = months.index(month) + 1

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    # """Displays statistics on the favourite times of travel."""

    print('\nCalculating Bikeshare Customer\'n Favourite Times of Travel...\n')
    start_time = time.time()

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # TO DO: display the most common month

    #  convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create month column
    df['month'] = df['Start Time'].dt.month

    # most popular month
    pop_month = df['month'].mode()[0]
    print('Most Popular Month:', pop_month)

    # TO DO: display the most common day of week

    #  convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create a week column
    df['week'] = df['Start Time'].dt.week

    # most popular week
    pop_week = df['week'].mode()[0]
    print('Most Popular Week:', pop_week)

    # TO DO: display the most common start hour

    #  convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # most popular hour
    pop_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', pop_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # most popular start station
    pop_start_station = df['Start Station'].mode()[0]
    print('Most Popular Month:', pop_start_station)

    # TO DO: display most commonly used end station

    # most popular end station
    pop_end_station = df['End Station'].mode()[0]
    print('Most Popular Month:', pop_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['pop_route'] = df['Start Station','End Station'].mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

    # TO DO: display mean travel time
    mean_travel= df['Trip Duration'].mean()
    print("The average trip duration is:", mean_travel)

    # TO DO: display total travel time
    total_travel= df['Trip Duration'].sum()
    print("The total of trip duration is:", total_travel)

    total_travel= df['Trip Duration'].min()
    print("The shortest trip duration is:", least_travel)

    total_travel= df['Trip Duration'].max()
    print("The longest trip duration is:", most_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].count_values()
    print("The number of types of users are:", counts_user_types)

    # TO DO: Display counts of gender
    counts_gender = df['Gender'].count_values()
    print("The gender counts are:", counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    min_year = df['Birth Year'].min()
    print("Earliest birth year is:", min_year)

    max_year = df['Birth Year'].max()
    print("Most recent birth year is:", max_year)

    pop_year = df['Birth Year'].mode()[0]
    print("Most common Birth year is:", pop_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # df = pd.read_csv(CITY_DATA[city, month, day])

        while True:
            proceed = input('\nDo you want to view data? Please enter yes or no, \n')
            if proceed.lower() == 'yes' :
                df += df[df.iloc[5, :]]
                continue
            elif proceed.lower() == 'no':
                break

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':


        if __name__ == "__main__":
            main()

main()
