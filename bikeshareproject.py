#This is the optimized code
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print(f"\nThe most popular month is: {popular_month}")

    popular_day = df['day_of_week'].mode()[0]
    print(f"\nThe most popular day is: {popular_day} (Where Sun:0, Mon:1, Tue:2, etc.)")

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"\nThe most popular start hour is: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    com_start_station = df['Start Station'].mode()[0]
    print("\nThe most popular start station is: {}".format(com_start_station))

    com_end_station = df['End Station'].mode()[0]
    print("\nThe most popular end station is: {}".format(com_end_station))

    com_stations = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"\nThe most frequent start and end station trip combination is: {com_stations}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print(f"\nTotal trip duration is: {hour} hour(s), {minute} minute(s) and {second} second(s).")

    mean_duration = round(df['Trip Duration'].mean())
    mean_minute, mean_second = divmod(mean_duration, 60)
    mean_hour, mean_minute = divmod(mean_minute, 60)
    print(f"\nThe average trip duration is {mean_hour} hour(s), {mean_minute} minute(s) and {mean_second} second(s).")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print("Gender data not available for this city.")

    if 'Birth Year' in df.columns:
        earliest_byr = int(df['Birth Year'].min())
        print("\nThe earliest birth year is:", earliest_byr)
        recent_byr = int(df['Birth Year'].max())
        print("\nThe most recent birth is:", recent_byr)
        common_byr = int(df['Birth Year'].mode()[0])
        print("\nThe most common birth year is:", common_byr)
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    i = 0
    raw = input("\nWould you like to view 5 rows of raw data? Type 'yes' or 'no': ").lower()
    pd.set_option('display.max_columns', 200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])
            raw = input("\nWould you like to view more data? Type 'yes' or 'no': ").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no': ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no: ').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
