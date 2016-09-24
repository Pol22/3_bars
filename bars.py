import json
import sys
import math

def load_data(filepath):
    data=json.loads(open(filepath,encoding='utf-8').read())
    return data


def get_biggest_bar(data):
    maxSeats=0
    for line in data:
        if(line['Cells']['SeatsCount']>maxSeats):
            max=line
            maxSeats=max['Cells']['SeatsCount']
    return max

def get_smallest_bar(data):
    minSeats=float('inf')
    for line in data:
        if(line['Cells']['SeatsCount']<minSeats):
            min=line
            minSeats=min['Cells']['SeatsCount']
    return min

def get_closest_bar(data, longitude, latitude):
    rast=float('inf')
    for line in data:
        x=line['Cells']['geoData']['coordinates'][0]
        y=line['Cells']['geoData']['coordinates'][1]
        line_rast=math.sqrt((longitude-x)**2+(latitude-y)**2)
        if(line_rast<rast):
            closest=line
            rast=line_rast
    return closest

if __name__ == '__main__':
    file=load_data('data.json')
    big_bar=get_biggest_bar(file)
    small_bar=get_smallest_bar(file)
    print("Biggest bar in Moscow: ", big_bar['Cells']['Name'].encode(sys.stdout.encoding,'ignore').decode(sys.stdout.encoding), big_bar['Cells']['SeatsCount'])
    print("Smallest bar in Moscow: ", small_bar['Cells']['Name'].encode(sys.stdout.encoding,'ignore').decode(sys.stdout.encoding), small_bar['Cells']['SeatsCount'])
    x=float(input("Input longitude: "))
    y=float(input("Input latitude: "))
    closest_bar=get_closest_bar(file, x, y)
    print("Nearest bar: ", closest_bar['Cells']['Name'].encode(sys.stdout.encoding,'ignore').decode(sys.stdout.encoding), closest_bar['Cells']['geoData']['coordinates'][0], closest_bar['Cells']['geoData']['coordinates'][1])