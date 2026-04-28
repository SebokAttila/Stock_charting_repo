*** Settings ***
Library     Collections
Library     ../data/yahoo_data_fetch.py

*** Variables ***
${TEST_CSV}    ${CURDIR}/test_data/Test_Yahoo_OHLCV_Hourly.csv


*** Test Cases ***
CSV Reading is Successful
    ${df}=    Get Historical Data From Csv    ${TEST_CSV}
    Should Not Be Empty    ${df}

CSV Contains Close Column
    ${df}=    Get Historical Data From Csv    ${TEST_CSV}
    ${columns}=    Evaluate    list($df.columns)
    Should Contain    ${columns}    Close

CSV Number of Rows is Right
    ${df}=    Get Historical Data From Csv    ${TEST_CSV}
    ${row_count}=    Evaluate    len($df)
    Should Be Equal As Integers    ${row_count}    1738

CSV Given Value is Right
    ${df}=    Get Historical Data From Csv    ${TEST_CSV}
    ${close}=    Evaluate    $df["Close"].iloc[0]
    Should Be Equal As Numbers    ${close}    219.74000549316406
