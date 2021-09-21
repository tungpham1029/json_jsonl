# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import bigjson


def print_hi():

    # Reads json file in streaming mode
    # with open('/home/tungpham/Downloads/public_company_202109_20', 'rb') as f:
    # with open('/home/tungpham/Downloads/job_posting_202109_18', 'rb') as f:
    # with open('/home/tungpham/Downloads/202109_18', 'rb') as f:
    with open('/home/tungpham/Downloads/202109_20_full_profile', 'rb') as f:
    # with open('/home/tungpham/Downloads/profile', 'rb') as f:
    # with open('/home/tungpham/Downloads/202106_13_full_company', 'rb') as f:
        json_data = bigjson.load(f)

        # Open output file
        # with open('/home/tungpham/Downloads/public_company_202109_20.json', 'w') as outfile:
        # with open('/home/tungpham/Downloads/job_posting_202109_18.json', 'w') as outfile:
        # with open('/home/tungpham/Downloads/202109_18.json', 'w') as outfile:
        with open('/home/tungpham/Downloads/202109_20_full_profile.json', 'w') as outfile:
        # with open('/home/tungpham/Downloads/profile.json', 'w') as outfile:
        # with open('/home/tungpham/Desktop/facebook_account.json', 'w') as outfile:
            # Iterates over input json
            try:
                for data in json_data:
                    # Converts json to a Python dict
                    dict_data = data.to_python()
                    # Saves the output to output file
                    outfile.write(json.dumps(dict_data) + "\n")
            except Exception as e:
                print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
