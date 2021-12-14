"""
CSC110 Final Project: Main file

Module Description
==================
This module contains the main file for our project. Please 'run' this file.
IMPORTANT: Make sure you 'run' the file and do not 'Run File in Python Console'

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of TAs and instructors
teaching CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Chenika Bukes, Krishna Cheemalapati, Aryan Goel, and Dhairya Khara.
"""
from user_interface import *

if __name__ == '__main__':
    try:
        main_loop(PHOTO_ERROR, PHOTO_UNEMPLOYMENT_BEFORE, PHOTO_UNEMPLOYMENT_COVID, PHOTO_JOB_OPENINGS_BEFORE,
                  PHOTO_JOB_OPENINGS_COVID)
    except urllib.error.HTTPError:
        print("Yahoo Finance is unavailable at the moment. Please try again in two minutes")
    except urllib.error.URLError:
        print("Yahoo Finance is unavailable at the moment. Please try again in two minutes")
