#!/bin/sh

# run_travis_tests.sh: Run the tests for Travis CI.

python -m test.test_pi_versions &&
python -m test.test_init &&
python -m test.test_sftp &&
python -m test.test_run &&
python -m test.test_status &&
python -m test.test_delete 
