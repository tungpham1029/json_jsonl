# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import bigjson


def print_hi():

    # Reads json file in streaming mode
    with open('/home/tungpham/Downloads/202106_19_full_profile', 'rb') as f:
    # with open('/home/tungpham/Downloads/202106_13_full_company', 'rb') as f:
        json_data = bigjson.load(f)

        # Open output file
        with open('/home/tungpham/Downloads/202106_19_full_profile.json', 'w') as outfile:
        # with open('/home/tungpham/Desktop/facebook_account.json', 'w') as outfile:
            # Iterates over input json
            for data in json_data:
                # Converts json to a Python dict
                dict_data = data.to_python()
                # Saves the output to output file
                outfile.write(json.dumps(dict_data) + "\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
