# IDAO 2021 Finals - Final submission

This is the final submission that gave us the highest score in public LB. Although we tried different solutions with multiple csv files data, the solutions were giving some errors which we could not debug in time. So we could only use the trxn.csv and aum.csv file data properly.
As we have used the code structure given by the organizers, you can follow the following steps to run the codes.

## Files to add:
We have used the original trxn.csv, aum.csv, client.csv and funnel.csv, you have to copy the original data csv files (trxn.csv, aum.csv, client.csv and funnel.csv) to the "tests/train_data_sample" folder.

## TLDR; running train script and submitting solution
1. Run `docker-compose -f docker-compose.train.yaml up`. This should produce a `submission/model.joblib` file with trained model and a tar archive with your model in `generated_submissions` folder. First time docker-compose could run for some time to build the docker image. Next time it will be much quicker.
2. Run `docker-compose -f docker-compose.test.yaml up`. This will produce a .csv file with your predictions in `generated_submissions` folder.


