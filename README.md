# IDAO 2021 Finals - Final submission

This is the final submission that gave us our highest score in public LB. Our final score in public LB is 3436.63 and we are 26th among the 30 participant teams.

## Files to add:
We have used the original trxn.csv, aum.csv, client.csv and funnel.csv, you have to copy the original data csv files (trxn.csv, aum.csv, client.csv and funnel.csv) to the "tests/train_data_sample" folder.

## TLDR; running train script and submitting solution
1. Run `docker-compose -f docker-compose.train.yaml up`. This should produce a `submission/model.joblib` file with trained model and a tar archive with your model in `generated_submissions` folder. First time docker-compose could run for some time to build the docker image. Next time it will be much quicker.
2. Run `docker-compose -f docker-compose.test.yaml up`. This will produce a .csv file with your predictions in `generated_submissions` folder.


