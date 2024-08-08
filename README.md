STEP  to Execute the Script 
step 1: install the python lib using command - pip install -r requirement.txt
step 2: Update config with file directory (optional), s3 details
step 3 : update client_secrete.json with actual clientId for google drive connection
step 4 : To run the script - C:/python/python.exe sacumen_py_assignment.py
step 5: Command to run the test cases -C:\python\Scripts\pytest.exe test_sacumen_py_assignment.py --html=unitTestReport.html 
step 6: Command to get the Code coverage, run below 2 command
    C:\python\Scripts\coverage.exe  run -m pytest
    C:\python\Scripts\pytest.exe  --cov --cov-report=html:code_coverage_details
