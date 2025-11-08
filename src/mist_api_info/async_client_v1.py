import os
import requests
import json
import time
import logging
import argparse
import asyncio
import aiohttp


async def get_devices(session, headers, mist_url, site_id):
    """
    Retrieve information about the devices in a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of information about the devices in the network.
    """
    device_url = f"{mist_url}sites/{site_id}/devices"
    async with session.get(device_url, headers=headers) as resp:
        if resp.status != 200:
            raise Exception(f"Failed to get devices. Status code: {resp.status}")
        return await resp.json()


async def get_device_stats(session, headers, mist_url, site_id):
    """
    Retrieve statistics about the devices in a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of device statistics.
    """
    device_stats_url = f"{mist_url}sites/{site_id}/stats/devices"
    async with session.get(device_stats_url, headers=headers) as resp:
        if resp.status != 200:
            raise Exception(f"Failed to get device stats. Status code: {resp.status}")
        return await resp.json()


async def get_wlans(session, headers, mist_url, site_id):
    """
    Retrieve information about the WLANs in a Mist network.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of information about the WLANs in the network.
    """
    wlan_url = f"{mist_url}sites/{site_id}/wlans"
    async with session.get(wlan_url, headers=headers) as resp:
        if resp.status != 200:
            raise Exception(f"Failed to get WLANs. Status code: {resp.status}")
        return await resp.json()


async def get_beacons(headers, mist_url, site_id, session):
    """
    Retrieve information about the beacons in a Mist network asynchronously.

    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :param session: The aiohttp session object to be used for making the API request.
    :return: A dictionary of information about the beacons in the network.
    """
    
    beacons_url = f'{mist_url}sites/{site_id}/beacons'
    async with session.get(beacons_url, headers=headers) as response:
        if response.status != 200:
            raise Exception(f"Failed to get beacons. Status code: {response.status}")
        return await response.json()

async def get_wlans(session, headers, mist_url, site_id):
    """
    Retrieve information about the WLANs in a Mist network.

    :param session: A session object created using aiohttp.ClientSession.
    :param headers: A dictionary containing the HTTP headers required for the API request.
    :param mist_url: The URL of the Mist API.
    :param site_id: The ID of the network.
    :return: A dictionary of information about the WLANs in the network.
    """
    wlan_url = '{0}sites/{1}/wlans'.format(mist_url,site_id)
    async with session.get(wlan_url, headers=headers) as response:
        if response.status != 200:
            raise Exception(f"Failed to get WLANs. Status code: {response.status}")
        return await response.json()


async def write_to_json(data, file_name):
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


async def write_to_html(data, file_name):
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


def read_config(file_path):
    """
    Reads configuration from a JSON file.

    :param file_path: The path to the JSON file.
    :return: A dictionary containing the configuration data.
    """
    
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config



async def main(config_file, output_file, log_file):
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
    
    async with aiohttp.ClientSession() as session:
        try:
            devices = await get_devices(session, headers, mist_url, site_id)
            logging.info('Retrieved devices information')

            device_stats = await get_device_stats(session, headers, mist_url, site_id)
            logging.info('Retrieved device statistics')

            wlans = await get_wlans(session, headers, mist_url, site_id)
            logging.info('Retrieved WLAN information')

            beacons = await get_beacons(session, headers, mist_url, site_id)
            logging.info('Retrieved beacon information')

            clients = await get_clients(session, headers, mist_url, site_id)
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
    asyncio.run(main(config_file, output_file, log_file))
    run_time = time.time() - start_time
    print(f'\nTotal runtime: {run_time:.2f} seconds')
