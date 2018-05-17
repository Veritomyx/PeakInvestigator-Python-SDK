#!/bin/sh

# run_travis_tests.sh: Run the tests for Travis CI.

python -m tests.test_pi_versions &&
python -m tests.test_init &&
python -m tests.test_sftp &&
python -m tests.test_run &&
python -m tests.test_status &&
python -m tests.test_delete 
