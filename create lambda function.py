aws lambda create-function \
--function-name salesAnalysisReport \
--runtime python3.7 \
--zip-file fileb://salesAnalysisReport-v2.zip \
--handler salesAnalysisReport.lambda_handler \
--region us-west-2 \
--role arn:aws:iam::988800437405:role/salesAnalysisReportRole