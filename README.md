# nlpproject

### To run the project
use the following command to build hmmInput model
```
python hmmInput_learn.py
```
You can input your test data (pinyin) in the testData.txt.
Then use the following command to translate the input (pinyin) to Chinese characters.
```
python hmmInput.py
```
The results can be found both in the terminal and result.txt 

<br>
### Verification
To verify the correctness of our pinyin correction function, you can use the following command.
```
verifyCorrection.py
```
It will randomly modify the words in testData.txt to generate typos, call the correction function to correct the typos, and compare the corrected word with the original one. The output is the correctness rate.
