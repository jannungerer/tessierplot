import os

asset_directory = os.path.join(os.path.dirname(__file__), 'assets')

def get_asset(filename):
    return os.path.join(asset_directory, filename)