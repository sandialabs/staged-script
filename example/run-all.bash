#!/usr/bin/env bash
quote_arg() {
    if [[ "$1" =~ ( ) ]]; then
        echo -n "'$1' "
    else
        echo -n "$1 "
    fi
}

run_script() {
    echo
    echo -n "~~~~~  Running "
    for arg in "$@"; do
        quote_arg "${arg}"
    done
    echo " ~~~~~"
    echo
    python3 "$@"
    echo
}

ORIG_DIR=$(pwd)
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
cd "${SCRIPT_DIR}" || exit 1
python3 -m pip uninstall -y staged-script
cd ..
python3 -m pip install .
cd "${SCRIPT_DIR}" || exit 1
run_script ex_0_the_basics.py --help
run_script ex_0_the_basics.py --stage hello
run_script ex_1_removing_the_retry_arguments.py --help
run_script ex_1_removing_the_retry_arguments.py --stage hello
run_script ex_2_running_certain_stages_by_default.py
run_script ex_3_adding_arguments.py --some-file foo.txt
run_script ex_4_customizing_stage_behavior.py --some-file foo.txt --some-flag --stage goodbye
run_script ex_5_customizing_individual_stages.py --some-file foo.txt
run_script ex_6_creating_retryable_stages.py --help
run_script ex_6_creating_retryable_stages.py --some-file foo.txt
run_script ex_6_creating_retryable_stages.py --some-file foo.txt --flaky-retry-attempts 0
run_script ex_7_customizing_the_summary.py --some-file foo.txt --stage hello
cd "${ORIG_DIR}" || exit 1
