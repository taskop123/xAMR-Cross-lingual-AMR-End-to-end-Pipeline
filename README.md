# xAMR: Cross-lingual ARM End-to-end Pipeline
In this repository we share the code for the xAMR cross-lingual AMR end-to-end pipeline.
## Languages
As we state in the paper, we evaluate xAMR for Macedonian, Bulgarian, German, Spanish and Italian language. Furthermore,
this methodology can be used for different languages as well.

## Requirements
For the purpose of running this code, you need to install the dependencies in requirements.txt.

    pip install -r requirements.txt


## Example 
In main.py there is an example for running the pipeline in x language. The class xAMR expects 2 arguments, 
the first one is the source language that you are using as input to the pipeline and the second argument is
the sentence in the corresponding language.
