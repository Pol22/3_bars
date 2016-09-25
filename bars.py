import json
import sys
import math
import os


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    max_seats = 0
    for json_line in data:
        if(json_line['Cells']['SeatsCount'] > max_seats):
            biggest_bar = json_line
            max_seats = biggest_bar['Cells']['SeatsCount']
    return biggest_bar


def get_smallest_bar(data):
    min_seats = float('inf')
    for json_line in data:
        if(json_line['Cells']['SeatsCount'] < min_seats):
            smallest_bar = json_line
            min_seats = smallest_bar['Cells']['SeatsCount']
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    distance_to_bar = float('inf')
    for json_line in data:
        bar_longitude = json_line['Cells']['geoData']['coordinates'][0]
        bar_latitude = json_line['Cells']['geoData']['coordinates'][1]
        json_line_distance_to_bar = math.sqrt((longitude-bar_longitude)**2 +
                                              (latitude-bar_latitude)**2)
        if(json_line_distance_to_bar < distance_to_bar):
            closest = json_line
            distance_to_bar = json_line_distance_to_bar
    return closest


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Input path to the json file second argument")
        exit()
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print("Incorrect path")
        exit()
    json_content = load_json_data(filepath)
    biggest_bar = get_biggest_bar(json_content)
    smallest_bar = get_smallest_bar(json_content)
    print("Biggest bar: \n\t",
          biggest_bar['Cells']['Name'].encode(
              sys.stdout.encoding,
              'ignore').decode(sys.stdout.encoding))
    print("Smallest bar: \n\t",
          smallest_bar['Cells']['Name'].encode(
              sys.stdout.encoding,
              'ignore').decode(sys.stdout.encoding))
    longitude = float(input("Input longitude: "))
    latitude = float(input("Input latitude: "))
    closest_bar = get_closest_bar(json_content, longitude, latitude)
    print("Closest bar: \n\t",
          closest_bar['Cells']['Name'].encode(
              sys.stdout.encoding,
              'ignore').decode(sys.stdout.encoding))
