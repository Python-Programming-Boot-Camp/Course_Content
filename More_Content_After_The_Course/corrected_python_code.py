from datetime import datetime
def miles_run_per_day(name : str, miles_run : float) -> float:
    """
        This function calculates the number of miles someone
        has run per day this year
        Parameters:
        name(str): the persons name
        miles_run(float): the miles someone has run this year
        Returns:
        avg_miles_run: the average miles someone has run per day this year
    """
    print(f"Hello {name} you have run {miles_run} miles this year")
    day_of_year = datetime.now().timetuple().tm_yday
    avg_miles_run = round(miles_run / day_of_year, 2)
    print(f"That's an average of {avg_miles_run} miles per day")
    return avg_miles_run

if __name__ == "__main__":
    name = "Jonathan"
    current_miles = 794
    miles_run_per_day(name,current_miles)
    activities = ["running", "walking", "biking"]
    print("List of activities:", end = " ")
    for activity in activities:
        print(activity, end = " ")
    print()