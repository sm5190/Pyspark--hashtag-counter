# Pyspark--hashtag-counter
## Overview:
This project involves a comprehensive analysis of a dataset containing tweets, aiming to identify the top 20 hashtags prevalent within the collection. The data is hosted on an AWS S3 bucket, demonstrating the project's integration with cloud storage solutions.
## Data Processing with Apache Spark
To handle the dataset efficiently, we leveraged Apache Spark, a powerful big data processing framework. Spark's robust capabilities enable it to process large datasets with high speed and efficiency.
## Custom Map-Reduce Code
The core of our analysis is the hashtag_code.py script, which contains custom-written parallel processing logic. This script employs a map-reduce approach, a standard in big data processing, to aggregate and analyze hashtag occurrences across the dataset efficiently.
## Deployment on Amazon EMR
To scale up the data processing, we utilized Amazon Elastic MapReduce (EMR), a cloud-based big data platform that simplifies running big data frameworks, such as Apache Spark, on AWS. By deploying our processing tool on Amazon EMR, we benefitted from its distributed data processing capabilities.
## Output Storage and Accessibility
Upon completion of the data processing, the output - which includes the top 20 hashtags - is automatically stored in a specified folder within the same Amazon S3 bucket. This setup ensures that the results are easily accessible and securely stored.

Through this project, we showcased the integration of several advanced technologies to analyze big data efficiently. The combination of Python for data processing, Apache Spark for handling large datasets, Amazon EMR for scalable computing, and Amazon S3 for data storage and retrieval demonstrates a robust big data solution.
