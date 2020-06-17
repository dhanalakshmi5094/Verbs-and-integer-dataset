### Data pipeline - 1 hour

You should allow ~1 hour to complete this task.

You have been tasked with developing a new processing pipeline which extracts features from long texts. Each feature is identified by a regular expression. You are provided a list of features in the `patterns.json` file.

```json
[
    {
        "feature": string,
        "regex": string,
    }, ...
]
```

We require you to use `Python >= 3.7` or `Node >= 12 (ES6)`. 

__Python:__

You have been provided an interfacing function (`process_document`) which will be called by legacy code. This function accepts the document as UTF-8 encoded `bytes`. The result would be a dictionary containing the name (key) and number of occurrences (value) for each feature. Feel free to improve/customise the return value if you have a justified reason. Below is an example function:

```python
def process_document(document: bytes) -> Dict[str, str]:
```

We expect your code to be well tested. You may use whichever testing framework you wish, however we use `pytest`.

__JavaScript/TypeScript__

You have been provided an interfacing function (`processDocument`) which will be called by legacy code. This function accepts the document as `string` filled `Buffer`. The result would be an object containing the name (key) and number of occurrences (value) for each feature. Feel free to improve/customise the return value if you have a justified reason. Below is an example function:

```javascript
function processDocument(document: ArrayBuffer): object {...}
```

We expect your code to be well tested. You may use whichever testing framework you wish, however we use `mocha` for JavaScript/TypeScript.

**Documents**

You have been provided with 4 example documents in the `./documents/` folder.

__Scoring__

This is a test of your ability to solve technical problems within our domain through code and therefore you will be tested on: 

1. Code Performance.

2. Code Quality

3. Test Quality

4. Code Documentation