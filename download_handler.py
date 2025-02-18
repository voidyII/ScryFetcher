import scryfall_handler
import requests
from tqdm import tqdm    

headers = {'User-Agent': 'ScryFetcher/0.1', 'Accept': '*/*'}

def default_bulk_dl():
    dc_bulk = scryfall_handler.get_dcbulk()

    dl_uri = dc_bulk["download_uri"]
    dcdl_res = requests.get(dl_uri, stream=True, headers=headers)

    total_size = dc_bulk["size"]
    block_size = 1024
    progress_size = 0

    with tqdm(total=total_size, unit="B", unit_scale=True, desc="Downloading", bar_format="{l_bar}{bar:30} | {n_fmt}/{total_fmt} [{rate_fmt}] | {remaining} left") as progress_bar:
        with open("./json_dump/dc_bulk.json", "wb") as file:
            for data in dcdl_res.iter_content(block_size):
                file.write(data)
                progress_size += len(data)
                progress_bar.update(len(data))

def all_bulk_dl():
    ac_bulk = scryfall_handler.get_acbulk()

    dl_uri = ac_bulk["download_uri"]
    acdl_res = requests.get(dl_uri, stream=True, headers=headers)

    total_size = ac_bulk["size"]
    block_size = 1024
    progress_size = 0

    with tqdm(total=total_size, unit="B", unit_scale=True, desc="Downloading", bar_format="{l_bar}{bar:30}| {n_fmt}/{total_fmt} [{rate_fmt}] | {remaining} left") as progress_bar:
        with open("./json_dump/ac_bulk.json", "wb") as file:
            for data in acdl_res.iter_content(block_size):
                file.write(data)
                progress_size += len(data)
                progress_bar.update(len(data))