import json, unittest, datetime

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    # create new dictionary data
    new_data = {}
    new_data['deviceID'] = jsonObject.get('deviceID')
    new_data['deviceType'] = jsonObject.get('deviceType')
    new_data['timestamp'] = jsonObject['timestamp']
    # split string into list, each item is an location data
    location = jsonObject['location'].split('/')
    # assign location data from list
    new_data['location'] = {
          'country': location[0],
          'city': location[1],
          'area': location[2],
          'factory': location[3],
          'section' : location[4]
    }
    # use similar string key from json_file
    new_data['data'] = {
          'status' : jsonObject.get('operationStatus'),
          'temperature': jsonObject.get('temp')
          }

    return new_data


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    new_data = {}
        # use similar string key from json_file
    new_data['deviceID'] = jsonObject.get('device').get('id')
    new_data['deviceType'] = jsonObject.get('device').get('type')
   # use datetime module to convert date/time data from string to integer
    val = datetime.datetime.strptime(jsonObject.get('timestamp'), "%Y-%m-%dT%H:%M:%S.%fZ")
  # convert time data into millisecond by * 1000
    new_data['timestamp'] = val.timestamp() * 1000
      # use similar string key from json_file
    new_data['location'] = {
          'country': jsonObject['country'],
          'city': jsonObject['city'],
          'area': jsonObject['area'],
          'factory': jsonObject['factory'],
          'section': jsonObject['section']
    }
    new_data['data'] = jsonObject.get('data')
  
    return new_data


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
