"""
Author: Kris Armstrong
Version: 1.0
Date: 2023-02-07

A Python3 script for retrieving information about a Mist network from the Mist API. The script uses the 'requests' library to send HTTP requests to the Mist API and retrieve information about devices, WLANs, beacons, clients, and radio frequency statistics. The information is returned as JSON and is printed to the console.

Dependencies:
    - requests library

Usage:
    - Provide the API token, URL of the Mist API, and site ID of the network.

Assumptions/Limitations:
    - If the API request fails, an exception will be raised.

Author:
    - Kris Armstrong

Contributors:
    - N/A

License:
    - Apache2 License

Disclaimer:
    - This code is provided as-is with no warranty or guarantee of functionality.
    - Use at your own risk.
"""


import os
import requests
import json
import time
import logging
import argparse


def get_devices(headers, mist_url, site_id):
    """
    Retrieve information about the devices in a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of information about the devices in the network.
    """
    
    device_url = '{0}sites/{1}/devices'.format(mist_url,site_id)
    response = requests.get(device_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get devices. Status code: {}".format(response.status_code))
    return response.json()


def get_device_stats(headers, mist_url, site_id):
    """
    Retrieve statistics about the devices in a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of device statistics.
    """
    
    device_stats_url = '{0}sites/{1}/stats/devices'.format(mist_url,site_id)
    response = requests.get(device_stats_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get device stats. Status code: {}".format(response.status_code))
    return response.json()
    
    
def get_wlans(headers, mist_url, site_id):
    """
    Retrieve information about the WLANs in a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of information about the WLANs in the network.
    """
    
    wlan_url = '{0}sites/{1}/wlans'.format(mist_url,site_id)
    response = requests.get(wlan_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get WLANs. Status code: {}".format(response.status_code))
    return response.json()
   

def get_beacons(headers, mist_url, site_id):
    """
    Retrieve information about the beacons in a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of information about the beacons in the network.
    """
    
    beacons_url = '{0}sites/{1}/beacons'.format(mist_url,site_id)
    response = requests.get(beacons_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get beaconss. Status codes: {}".format(response.status_code))
    return response.json()
 

def get_aps(headers, mist_url, site_id):
    '''
    '''
    ap_url = '{0}sites/{1}/stats/devices'.format(mist_url,site_id)
    response = requests.get(ap_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get APs")
    return response.json()
    

def get_bssids(headers, mist_url, site_id):
    return requests.Response.json()


def get_rf_stats(headers, mist_url, site_id):
    """
    Retrieve radio frequency statistics for a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of radio frequency statistics.
    """
    
    rf_stats_url = '{0}sites/{1}/stats/rf'.format(mist_url,site_id)
    response = requests.get(rf_stats_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get radio frequesency stats. Status code: {}".format(response.status_code))
    return response.json()


def get_clients(headers, mist_url, site_id):
    """
    Retrieve information about the client devices in a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of information about the client devices in the network.
    """
    
    client_url = '{0}sites/{1}/stats/clients'.format(mist_url,site_id)
    response = requests.get(client_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get client devices in network. Status code: {}".format(response.status_code))
    return response.json()


def write_to_json(data, file_name):
    """
    Writes the data to a JSON file.

    :param data: The data to be written to the file.
    :param file_name: The name of the file.
    :return: None.
    """
    try:
        print("Writing to file: {}".format(file_name))
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("An error occurred while writing to file: {}".format(e))


def write_to_html(data, file_name):
    """
    Writes the data to an HTML file.

    :param data: The data to be written to the file.
    :param file_name: The name of the file.
    :return: None.
    """
    try:
        print("Writing to file: {}".format(file_name))
        with open(file_name, 'w') as f:
            f.write("<html><head><title>Mist API Data</title>")
            f.write("<style>")
            f.write("body { font-family: Arial, sans-serif; }")
            f.write("pre { background-color: #f9f9f9; padding: 10px; }")
            f.write("</style>")
            f.write("</head><body>")
            for key, value in data.items():
                f.write("<h2>" + key + "</h2>")
                f.write("<pre>")
                f.write(json.dumps(value, indent=4))
                f.write("</pre>")
            f.write("</body></html>")
    except Exception as e:
        print("An error occurred while writing to file: {}".format(e))


def read_config(file_path):
    """
    Reads configuration from a JSON file.

    :param file_path: The path to the JSON file.
    :return: A dictionary containing the configuration data.
    """
    
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config


def parse_args():
    """
    Parses command line arguments using the argparse module.
    
    :return: A Namespace object containing the values of the command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file", default="config.json", help="Path to the config file")
    parser.add_argument("--output_file", default="mist_api_data.json", help="Name of the output file")
    parser.add_argument("--log_file", default="mist_api_log.log", help="Name of the log file")
    args = parser.parse_args()
    return args



def main(config_file, output_file, log_file):
    '''
    Main function to retrieve information from the Mist API.
    '''
    
    # Set up logging
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s %(message)s')
    
    # Read configuration
    config = read_config(config_file)
    token = config['token']
    mist_url = config['mist_url']
    site_id = config['site_id']
    
    # Set up headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token {}'.format(token)
    }

    try:
        devices = get_devices(headers, mist_url, site_id)
        logging.info('Retrieved devices information')

        device_stats = get_device_stats(headers, mist_url, site_id)
        logging.info('Retrieved device statistics')

        wlans = get_wlans(headers, mist_url, site_id)
        logging.info('Retrieved WLAN information')

        beacons = get_beacons(headers, mist_url, site_id)
        logging.info('Retrieved beacon information')

        clients = get_clients(headers, mist_url, site_id)
        logging.info('Retrieved client information')

        # Validate the data before writing to file
        write_to_json({
                'devices': devices,
                'device_stats': device_stats,
                'wlans': wlans,
                'beacons': beacons,
                'clients': clients
            }, output_file)
        
        write_to_html({
                'devices': devices,
                'device_stats': device_stats,
                'wlans': wlans,
                'beacons': beacons,
                'clients': clients
            }, output_file.replace('.json', '.html'))

    except Exception as e:    
        logging.error(f'An error occurred: {e}')    
  

if __name__ == '__main__':
    start_time = time.time()
    
    args = parse_args()
    
    config_file = args.config_file
    output_file = args.output_file
    log_file = args.log_file
    
    main(config_file, output_file, log_file)
    
    run_time = time.time() - start_time
    print(f'\nTotal runtime: {run_time:.2f} seconds')