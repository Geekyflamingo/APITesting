# REST API SHA512 Test Suite

# Summary

### Description
This test suite is designed to run against the JumpCloud SHA512 API. This application can be downloaded from [broken_hash](https://s3.amazonaws.com/qa-broken-hashserve/broken-hashserve.tgz) and run in a virtual machine. From inside the VM terminal `export PORT=8088` and run the version of API for VM's os.

The test suite is able to be downloaded from git repo. Needs python 3.7.0 and pytest.

### Running
cd into repo. run `pytest test_hash_endpoint.py test_stats_endpoint.py test_shutdown.py` in terminal.

### Caveats
1. **No multithreading/multiprocessing (C005) was used.(Pool was preferred)** 
2. **Inferred Acceptance Criteria based on description.** 
3. **No Before/After test fixtures, so manually spin up application. (tear down is done with /shutdown tests)** 
4. **No Load Testing was done (Locust preferred tool)**

### Future Work
The test suite is minimal. It needs test fixtures to ensure the endpoint is up and in a consistent state before each set of tests. Also, the addition of testing multiple connections, and the different shutdown scenarios are needed. Finally, adding load testing to the endpoints through a framework like locust would make the tests more robust. 

### Final Thoughts
The suite was created hurriedly, meaning corners were cut, but the fundamental test cases are there, as well as a representative set of bugs and edge cases.

## Test Cases

Case Id | Explanation | Data Accepted | Data Format | Main Acceptance | Associated Bugs
------ | ----------- | ------------- | ----------- | --------------- | ---------------
C001 | When the /stats endpoint is called using GET; returns the total number and average runtime of calls to /hash | No | N/A | <ol><li>Should not accept POST<li>Should not accept data or params<li>Average Runtime should be in milliseconds<ol> | B004, B005
C002 | When the /hash endpoint is called using POST and data; returns job identifier and kicks off hashing job on data  | Required | JSON: {"password": "<STRING_VALUE>" } | <ol><li>Returns immediately<li>Password key is required<li>Blank password values Accepted by SHA512 spec (B002*) | B001, B002*, B002.1
C003 | When the /hash/job_id endpoint is called using GET; returns the hashed password value from job_id returned in C002 | No | N/A | <ol><li>Supplied job_id in endpoint name<li>Should return `Hash not found` for non-existent ids >= 1<li>`Malformed Input` or `Invalid Input` for job_ids <=0 <ol> | B003
C004 | When the /hash endpoint is called with data of `shutdown` using POST; service should gracefully shutdown (i.e. reject new jobs and bleed off still running jobs) |  No | N/A | <ol><li>Should not accept new jobs<li>Should finish currently running jobs<ol> |
C005 | All endpoints should be able to handle multiple connections | Dependent on Endpoint | N/A | <ol><li>All endpoints can be hit by multiple calls at a single time<li>Load limited to cpu and 5 second runtimes ||



## Bugs

Bug ID  | Bug Description | Steps to Reproduce | Expected | Actual 
------ | --------------- | ------------------ | -------- | ------
B001 | POST to /hash endpoint doesn't return identifier immediately | <ol><li>Launch application</li><li>Post to the /hash endpoint with this:<br> ```$ curl -X POST -H "application/json" -d '{"password":"angrymonkey"}' http://127.0.0.1:8088/hash```  </li><li>Notice identifier does not return immediately</li><li>Wait for identifier to return</li></ol> | Identifier returns immediately after curl command is run | Identifier returns after 5 seconds
B002* | POST to /hash endpoint with blank password | <ol><li>Launch application</li><li>Post to the /hash endpoint with this:<br> ```$ curl -X POST -H "application/json" -d '{"password":""}' http://127.0.0.1:8088/hash```  </li><li>Wait for identifier to return</li><li>Notice identifier is returned</li></ol> | Identifier is not returned, error message produced | Identifier is returned, job is run but blank password is used
B002.1 | POST to /hash endpoint without password key | <ol><li>Launch application</li><li>Post to the /hash endpoint with this:<br> ```$ curl -X POST -H "application/json" -d '{"muttonchop":"angrymonkey"}' http://127.0.0.1:8088/hash```  </li><li>Wait for identifier to return</li><li>Notice identifier is returned</li></ol> | Identifier is not returned, error message produced | Identifier is returned, job is run but blank password is used
B003 | GET to /hash with id less than 0 | <ol><li>Launch application</li><li>GET to the /hash endpoint with this:<br> ```$ curl -X GET http://127.0.0.1:8088/hash/0```  </li><li>`Hash not found` is returned </li></ol> | Error message produced (e.g.`Invalid Input`) | `Hash not found`
B004 | GET to /stats | <ol><li>Launch application</li><li>GET to the /stats endpoint with this:<br> ```$ curl -X GET http://127.0.0.1:8088/stats```  </li><li>Returns JSON</li></ol>  | JSON: {"TotalRequests": INTEGER, "AverageRuntime":INTEGER\* } <br> *Runtime in milliseconds (5000+) | JSON: {"TotalRequests": INTEGER, "AverageRuntime":INTEGER\* } <br> *Runtime in microseconds (5000000+)
B005 | POST to /stats | <ol><li>Launch application</li><li>Post to the /stats endpoint with this:<br> ```$ curl -X POST -H "application/json" http://127.0.0.1:8088/stats```  </li><li>Returns the same as GET /stats</li></ol> | Error message produced (e.g.`Invalid Request`) | Returns same as GET 
