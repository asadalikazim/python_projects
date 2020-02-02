""" 
Assignment 2: Bridges

The data used for this assignment is a subset of the data found in:
https://www.ontario.ca/data/bridge-conditions
"""

import csv
import math
from typing import List, TextIO

ID_INDEX = 0
NAME_INDEX = 1
HIGHWAY_INDEX = 2
LAT_INDEX = 3
LON_INDEX = 4
YEAR_INDEX = 5
LAST_MAJOR_INDEX = 6
LAST_MINOR_INDEX = 7
NUM_SPANS_INDEX = 8
SPAN_LENGTH_INDEX = 9
LENGTH_INDEX = 10
LAST_INSPECTED_INDEX = 11
BCIS_INDEX = 12

HIGH_PRIORITY_BCI = 60   
MEDIUM_PRIORITY_BCI = 70
LOW_PRIORITY_BCI = 100

HIGH_PRIORITY_RADIUS = 500  
MEDIUM_PRIORITY_RADIUS = 250
LOW_PRIORITY_RADIUS = 100

EARTH_RADIUS = 6371

####### BEGIN HELPER FUNCTIONS ####################

def read_data(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on csv_file.
    """ 

    lines = csv.reader(csv_file)
    data = list(lines)[2:]
    return data


def calculate_distance(lat1: float, lon1: float,
                       lat2: float, lon2: float) -> float:
    """Return the distance in kilometers between the two locations defined by   
    (lat1, lon1) and (lat2, lon2), rounded to the nearest meter.
    
    >>> calculate_distance(43.659777, -79.397383, 43.657129, -79.399439)
    0.338
    >>> calculate_distance(43.42, -79.24, 53.32, -113.30)
    2713.226
    """

    # This function uses the haversine function to find the
    # distance between two locations. You do NOT need to understand why it
    # works. You will just need to call on the function and work with what it
    # returns.
    # Based on code at goo.gl/JrPG4j

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = (math.radians(lon1), math.radians(lat1), 
                              math.radians(lon2), math.radians(lat2))

    # haversine formula t
    lon_diff = lon2 - lon1 
    lat_diff = lat2 - lat1 
    a = (math.sin(lat_diff / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    return round(c * EARTH_RADIUS, 3)


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

THREE_BRIDGES_UNCLEANED = [
    ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403', '43.167233',
     '-80.275567', '1965', '2014', '2009', '4',
     'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012', '72.3', '',
     '72.3', '', '69.5', '', '70', '', '70.3', '', '70.5', '', '70.7', '72.9',
     ''],
    ['1 -  43/', 'WEST STREET UNDERPASS', '403', '43.164531', '-80.251582',
     '1963', '2014', '2007', '4',
     'Total=60.4  (1)=12.2;(2)=18;(3)=18;(4)=12.2;', '61', '04/13/2012',
     '71.5', '', '71.5', '', '68.1', '', '69', '', '69.4', '', '69.4', '',
     '70.3', '73.3', ''],
    ['2 -   4/', 'STOKES RIVER BRIDGE', '6', '45.036739', '-81.33579', '1958',
     '2013', '', '1', 'Total=16  (1)=16;', '18.4', '08/28/2013', '85.1',
     '85.1', '', '67.8', '', '67.4', '', '69.2', '70', '70.5', '', '75.1', '',
     '90.1', '']
    ]

THREE_BRIDGES = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,
                  -80.275567, '1965', '2014', '2009', 4,
                  [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012',
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]],
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582,
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61.0, 
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,
                                 73.3]],
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958',
                  '2013', '', 1, [16.0], 18.4, '08/28/2013',
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]]
                ]

#################################################
def format_data(data: List[List[str]]) -> None:  
    """Modify data so that it follows the format outlined in the 
    'Data formatting' section of the assignment handout.
    
    >>> d = THREE_BRIDGES_UNCLEANED
    >>> format_data(d)
    >>> d == THREE_BRIDGES
    True
    """

    # Note: This function is more difficult that the rest of the
    # function in this assignment. Do not work on this function until
    # you have implemented the other functions below.
    
    major_list = [] # dummy accumulator essentially same as data (cleaned)
    id_id = 1
    
    for bridge in data:
        
        minor_list = ["", "", "", "", "", "", "", "", "", "", "", "", ""]
        
        #^ creates a dummy list for one bridge for us to work with which has 
        #13 elements
        
        minor_list[ID_INDEX] = id_id
        id_id += 1
        
        minor_list[NAME_INDEX] = bridge[1]
        
        minor_list[HIGHWAY_INDEX] = bridge[2]
        
        minor_list[LAT_INDEX] = float(bridge[3])
        
        minor_list[LON_INDEX] = float(bridge[4])
        
        minor_list[YEAR_INDEX] = bridge[5]
        
        minor_list[LAST_MAJOR_INDEX] = bridge[6]
        
        minor_list[LAST_MINOR_INDEX] = bridge[7]
        
        minor_list[NUM_SPANS_INDEX] = int(bridge[8])
        
        minor_list[SPAN_LENGTH_INDEX] = span_lengths(bridge[9])
        
        if bridge[10] != "":
            minor_list[LENGTH_INDEX] = float(bridge[10])
        else:
            minor_list[LENGTH_INDEX] = 0.0
        
        minor_list[LAST_INSPECTED_INDEX] = bridge[11]
        
        minor_list[BCIS_INDEX] = bci_list(bridge[13:])
        
        major_list.append(minor_list)
        
    #finally modify the original input parameter    
    data[:] = major_list
        
def span_lengths(text: str) -> List[float]:
    """helper function created for creating the list of span lengths for
    format_data function
    
    span lengths are extracted from text, converted to float and returned
    as a list
    
    >>>span_lengths("Total=64 (1)=12;(2)=19;(3)=21;(4)=12;")
    [12.0, 19.0, 21.0, 12.0]
    """
    #we have to extract the digits between = and ; except for the first =
    #these are the spans
    #convert these to floats as well
    #add the spans to the list
    
    equal_ids = []
    colon_ids = []
    list_of_spans = []
    
    for i in range(len(text)):
        if text[i] == '=':
            equal_ids.append(i)
        if text[i] == ';':
            colon_ids.append(i)
    
    equal_ids = equal_ids[1:]
    
    for j in range(len(equal_ids)):
        list_of_spans.append(float(text[(equal_ids[j]+1):colon_ids[j]]))
        
    return list_of_spans
    
def bci_list(list_1: List[str]) -> List[float]:
    """helper function created for format_data for creating list of bci floats
    
    returns a list of floats of all the non empty elements in list_1
    
    >>>bci_list(['85.1', '', '67.8', '', '67.4', '', '69.2', '70', '70.5', '',\
    '75.1', '', '90.1', ''])
    [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]
    """
    i = 0
    list_2 = []
    
    while i < len(list_1):
        if list_1[i] != "":
            list_2.append(float(list_1[i]))
        i += 1    
    
    return list_2
 
def get_bridge(bridge_data: List[list], bridge_id: int) -> list:
    """Return the data for the bridge with id bridge_id from bridge_data. If
    there is no bridge with the given id, return an empty list.  
    
    >>> result = get_bridge(THREE_BRIDGES, 1)
    >>> result == [1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, \
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]
    True
    """
    # TODO
    
    if 0 < bridge_id <= len(bridge_data):
        if bridge_data[bridge_id - 1][0] == bridge_id:
            return bridge_data[bridge_id - 1]
    return []


def get_average_bci(bridge_data: List[list], bridge_id: int) -> float:
    """Return the average BCI for the bridge with bridge_id from bridge_data.
    If there is no bridge with the id bridge_id, return 0.0. If there are no
    BCIs for the bridge with id bridge_id, return 0.0.
    
    >>> get_average_bci(THREE_BRIDGES, 1)   
    70.88571428571429
    """
    # TODO
    bridge = get_bridge(bridge_data, bridge_id)
    
    if bridge == [] or bridge[12] == []:
        return 0.0
    return sum(bridge[12]) / float(len(bridge[12]))
    


def get_total_length_on_highway(bridge_data: List[list], highway: str) -> float:
    """Return the total length of bridges in bridge_data on highway.
    Use zero for the length of bridges that do not have a length provided.
    If there are no bridges on highway, return 0.0.
    
    >>> get_total_length_on_highway(THREE_BRIDGES, '403')
    126.0
    >>> get_total_length_on_highway(THREE_BRIDGES, '401')
    0.0
    """
    #TODO
    total = 0.0
    for bridge in bridge_data:
        if bridge[2] == highway:
            total += bridge[10]
    return total


def get_distance_between(bridge1: list, bridge2: list) -> float:
    """Return the distance in kilometres, rounded to the nearest metre
    (i.e., 3 decimal places), between the two bridges bridge1 and bridge2.
        
    >>> get_distance_between(get_bridge(THREE_BRIDGES, 1), \
                                 get_bridge(THREE_BRIDGES, 2))
    1.968
    """
    # TODO
    # Hint: use the provided helper function calculate_distance.
    
    return calculate_distance(bridge1[3], bridge1[4], bridge2[3], bridge2[4])
    
def find_closest_bridge(bridge_data: List[list], bridge_id: int) -> int:
    """Return the id of the bridge in bridge_data that has the shortest
    distance to the bridge with id bridge_id.
    
    Precondition: a bridge with bridge_id is in bridge_data, and there are
    at least two bridges in bridge_data
    
    >>> find_closest_bridge(THREE_BRIDGES, 2)
    1
    """
    # TODO
    dist = 0
    min_dist = 100000000
    closest_bridge = []
    og_bridge = get_bridge(bridge_data, bridge_id)   #original bridge
    
    for bridge in bridge_data:
        #we do not want to check the original bridge itself
        if bridge != og_bridge:
            dist = get_distance_between(bridge, og_bridge)
            if dist < min_dist:
                min_dist = dist
                closest_bridge = bridge
    return closest_bridge[0]             #returns id of closest bridge


def find_bridges_in_radius(bridge_data: List[list], lat: float, long: float,
                           distance: float) -> List[int]:
    """Return the IDs of the bridges that are within radius distance
    from (lat, long).
    
    >>> find_bridges_in_radius(THREE_BRIDGES, 43.10, -80.15, 50)
    [1, 2]
    """
    # TODO
    in_range = []
    for bridge in bridge_data:
        #checks whether or not bridge within radius distance
        if calculate_distance(bridge[3], bridge[4], lat, long) <= distance:
            in_range.append(bridge[0])
    return in_range


def get_bridges_with_bci_below(bridge_data: List[list], bridge_ids: List[int],
                               bci_limit: float) -> List[int]:
    """Return the IDs of the bridges with ids in bridge_ids whose most
    recent BCIs are less than or equal to bci_limit.
    
    >>> get_bridges_with_bci_below(THREE_BRIDGES, [1, 2], 72)
    [2]
    """
    # TODO
    result = []
    for id_id in bridge_ids:
        bridge = get_bridge(bridge_data, id_id)
        if bridge[12][0] <= bci_limit:           #checks most recent bci
            result.append(id_id)
    return result


def get_bridges_containing(bridge_data: List[list], search: str) -> List[int]:
    """
    Return a list of IDs of bridges whose names contain search (case
    insensitive).
    
    >>> get_bridges_containing(THREE_BRIDGES, 'underpass')
    [1, 2]
    >>> get_bridges_containing(THREE_BRIDGES, 'Highway')
    [1]
    """
    # TODO
    result = []
    for bridge in bridge_data:
        if search.lower() in bridge[1].lower():       #case desensitized
            result.append(bridge[0])
    return result


def assign_inspectors(bridge_data: List[list], inspectors: List[List[float]],
                      max_bridges: int) -> List[List[int]]:
    """Return a list of bridge IDs to be assigned to each inspector in
    inspectors. inspectors is a list containing (latitude, longitude) pairs
    representing each inspector's location.
    
    At most max_bridges bridges should be assigned to an inspector, and each
    bridge should only be assigned once (to the first inspector that can
    inspect that bridge).
    
    See the "Assigning Inspectors" section of the handout for more details.
    
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 1)
    [[1]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 2)
    [[1, 2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 3)
    [[1, 2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [43.10, -80.15]], 1)
    [[1], [2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [43.10, -80.15]], 2)
    [[1, 2], []]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [45.0368, -81.34]], 2)
    [[1, 2], [3]]
    >>> assign_inspectors(THREE_BRIDGES, [[38.691, -80.85], [43.20, -80.35]], 2)
    [[], [1, 2]]
    """
    # TODO
    result = []                 #to be returned
    master_assgn = []           #keeps track of ALL the bridges assigned
    
    for inspector in inspectors:
        assigned = []         #keeps track of bridges assigned to this inspector
        
        #high priority bridges according to this inspector identified
        highp_radius_ids = find_bridges_in_radius(bridge_data,\
                                                          inspector[0],\
                                                   inspector[1],\
                                                   HIGH_PRIORITY_RADIUS)
        highp_bridges = get_bridges_with_bci_below(bridge_data, highp_radius_ids\
                                                   , HIGH_PRIORITY_BCI)
        
        #bridges assigned to this inspector if not already assigned
        i = 0
        while len(assigned) < max_bridges and i < len(highp_bridges):
            if highp_bridges[i] not in master_assgn:
                master_assgn.append(highp_bridges[i])
                assigned.append(highp_bridges[i])
            i += 1
                
        #medium priority bridges according to this inspector identified
        medp_radius_ids = find_bridges_in_radius(bridge_data,\
                                                          inspector[0],\
                                                   inspector[1],\
                                                   MEDIUM_PRIORITY_RADIUS)
        medp_bridges = get_bridges_with_bci_below(bridge_data, medp_radius_ids\
                                                   , MEDIUM_PRIORITY_BCI) 
        
        #bridges assigned to this inspector if not already assigned            
        i = 0
        while len(assigned) < max_bridges and i < len(medp_bridges):
            if medp_bridges[i] not in master_assgn:
                master_assgn.append(medp_bridges[i])
                assigned.append(medp_bridges[i])
            i += 1
                          
        #low priority bridges according to this inspector identified
        lowp_radius_ids = find_bridges_in_radius(bridge_data,\
                                                          inspector[0],\
                                                   inspector[1],\
                                                   LOW_PRIORITY_RADIUS)
        lowp_bridges = get_bridges_with_bci_below(bridge_data, lowp_radius_ids\
                                                   , LOW_PRIORITY_BCI) 
        
        #bridges assigned to this inspector if not already assigned            
        i = 0
        while len(assigned) < max_bridges and i < len(lowp_bridges):
            if lowp_bridges[i] not in master_assgn:
                master_assgn.append(lowp_bridges[i])
                assigned.append(lowp_bridges[i])
            i += 1
        
        #list of bridges assigned to this inspector added to result
        result.append(assigned)
        
    return result
            
    


def inspect_bridges(bridge_data: List[list], bridge_ids: List[int], date: str, 
                    bci: float) -> None:
    """Update the bridges in bridge_data with id in bridge_ids with the new
    date and BCI score for a new inspection.
    
    >>> bridges = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,\
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61, \
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,\
                                 73.3]], \
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958', \
                  '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                 ]
    >>> inspect_bridges(bridges, [1], '09/15/2018', 71.9)
    >>> bridges == [[1, 'Highway 24 Underpass at Highway 403', '403', \
                     43.167233, -80.275567, '1965', '2014', '2009', 4, \
                     [12.0, 19.0, 21.0, 12.0], 65, '09/15/2018', \
                     [71.9, 72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                     '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], \
                     61, '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, \
                                          70.3, 73.3]], \
                    [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, \
                     '1958', '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                     [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                   ]
    True
    """
    
    # TODO
    bridge = []
    for id_id in bridge_ids:                   #loops over each bridge inspected
        bridge = get_bridge(bridge_data, id_id)
        bridge[11] = date                      #updates date
        bridge[12].insert(0, bci)              #updates bci


def add_rehab(bridge_data: List[list], bridge_id: int, new_date: str, 
              is_major: bool) -> None:
    """
    Update the bridge with the id bridge_id to have its last rehab set to
    new_date. If is_major is True, update the major rehab date. Otherwise,
    update the minor rehab date.
    
    >>> bridges = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,\
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61, \
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,\
                                 73.3]], \
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958', \
                  '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                 ]
    >>> add_rehab(bridges, 1, '2018', False)
    >>> bridges == [[1, 'Highway 24 Underpass at Highway 403', '403', \
                     43.167233, -80.275567, '1965', '2014', '2018', 4, \
                     [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                     [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                     '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], \
                     61, '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, \
                                          70.3, 73.3]], \
                    [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, \
                     '1958', '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                     [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                   ]
    True
    """
    # TODO
    bridge = get_bridge(bridge_data, bridge_id)
    if is_major:                           #checks whether major or minor rehab
        bridge[6] = new_date               #updates major rehab
    else:
        bridge[7] = new_date               #updates minor rehab



if __name__ == '__main__':
    pass 

    ## To test your code with larger lists, you can uncomment the code below to
    ## read data from the provided CSV file.
    #bridges = read_data(open('bridge_data.csv'))
    #format_data(bridges)

    ## For example,
    #print(get_bridge(bridges, 3))
    #expected = [3, 'NORTH PARK STEET UNDERPASS', '403', 43.165918, -80.263791,
                #'1962', '2013', '2009', 4, [12.2, 18.0, 18.0, 12.2], 60.8,
                #'04/13/2012', [71.4, 69.9, 67.7, 68.9, 69.1, 69.9, 72.8]]
    #print('Testing get_bridge: ', \
         #get_bridge(bridges, 3) == expected)
