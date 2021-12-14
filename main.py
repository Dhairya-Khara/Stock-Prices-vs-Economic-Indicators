"""Please run this file. Make sure you 'run' the file and not 'Run File in Python Console'"""
from user_interface import *

if __name__ == '__main__':
    try:
        main_loop(PHOTO_ERROR, PHOTO_UNEMPLOYMENT_BEFORE, PHOTO_UNEMPLOYMENT_COVID, PHOTO_JOB_OPENINGS_BEFORE,
                  PHOTO_JOB_OPENINGS_COVID)
    except urllib.error.HTTPError:
        print("Yahoo Finance is unavailable at the moment. Please try again in two minutes")
    except urllib.error.URLError:
        print("Yahoo Finance is unavailable at the moment. Please try again in two minutes")
