#!/bin/bash

function convert_nb {
    echo $1
    FILE=$(basename "$1" | cut -d '.' -f1)
    FILE_PATH=$(dirname "${1}")
    PY_FILE="$FILE_PATH/test_${FILE}.py"
    echo "Converting Notebook: $line into Test: ${PY_FILE}"
    jupyter nbconvert "${1}" --to script --output="test_${FILE}"
    echo "Linux"
    sed -i 's/^/     /' "${PY_FILE}" #add space
    TEST_FUNC="def test_${FILE}() -> None:"
    sudo echo "$(echo ${TEST_FUNC}; cat ${PY_FILE})" > $PY_FILE
}
