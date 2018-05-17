#!/bin/sh

# run_travis_tests.sh: Run the tests for Travis CI.

cd tests &&
python -m test_pi_versions &&
python -m test_init &&
python -m test_sftp &&
python -m test_run &&
python -m test_status &&
python -m test_delete 
