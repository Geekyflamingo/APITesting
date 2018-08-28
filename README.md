# APITesting

## Installation:


## Test cases:

| Test Case ID  | Test Scenario | Test Steps | Test Data | Expected | Actual | Pass/Fail |
|:-------------:|:-------------:|:----------|:---------:|:--------:|:------:|:---------:|
| T001		| It should answer on the PORT specified in the PORT environment variable. | <ol><li>Go to site <a href=http://todomvc.com/examples/angular2>todomvc</a></li><li>Click on input.</li><li>Type a todo.</li><li>Hit ENTER</li></ol> | input = {normal length, long length, weird characters, space before characters} | Todos are added to the page. | As Expected | Pass |
| T002	      	| Create Todo :sadpath:      |  <ol><li>Go to site <a href=http://todomvc.com/examples/angular2>todomvc</a></li><li>Click on input.</li><li>Hit ENTER</li><li>Hit space</li><li>Hit ENTER</li></ol> | input = {empty, empty string, only spaces} | Todos are not added to the page. | As Expected | Pass |
| T003          | Edit a Todo      |    <ol> <li> Test case T001</li> <li> Double Click on a todo</li> <li> Click on todo</li> <li> change input</li> <li> Hit ENTER</li></ol>| edit = {add characters, remove characters and change, remove characters} | Todos are edited except if they are an empty string. | As Expected | Pass |
| T004		| Delete a Todo | <ol> <li> Test case T001</li> <li> Hover over a todo</li> <li> Click on the x</li></ol> | T001 | Todos are deleted when the x is clicked. | As Expected | Pass |
| T005	      	| Check off a Todo      |   <ol> <li> Test case T001</li> <li> click on circle of a todo</li> <li> observe it gets striked out</li></ol> | T001 | Todos are marked as complete when the circle is clicked. | As Expected | Pass |
| T006          | Clear Completed Todos      |   <ol> <li> Test case T001</li> <li> Test case T005</li> <li> click on Clear Completed</li> <li> click on triangle to select all todos.</li> <li> click on Clear Completed to clear all.</li></ol> | T001 | Todos are marked as complete when the triangle is clicked and removed when Clear Completed is clicked. | As Expected | Pass |
