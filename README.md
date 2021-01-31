## Kafka Service 

Send JSON messages to a Kafka service by topic

Extra: Includes instructions to easily add metrics (including easy integration with monitoring) with Aiven DBaaS

## Installation intructions & env vars
Tested with: 
* Python version `3.8.0`
* Kafka `2.6.1`

Required environmental variables
* `KAFKA_URL` - host name and port in the following format -- hostname,port
* `KAFKA_CA` - ca.pem
* `KAFKA_SERVICE_CERT` - service.cert
* `KAFKA_SERVICE_KEY` - service.key

1. Clone this repo
2. Install the necessary Python libraries (use `requirements-dev.txt` for local mode instead of `requirements.txt`)
```
pip install -r requirements.txt
```

## Steps to run application
1. Run the producer to send one message to the Kafka service with the hostname as the key and the UTC time in JSON format 
```
python producer.py -t <topic-name>
```
**Required:**
* -t (topic name): Kafka topic name 

## Extra information

### Aiven instructions

Read on if you'd like to use Aiven DBaaS to help you power your application. Includes easy integration with a lot of monitoring and metric services. This demo uses InfluxDB and Grafana

Pre steps requirements:
- [ ] Aiven Kafka service and a kafka topic - [instructions](https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka)
- [ ] Aiven InfluxDB service - [instructions](https://help.aiven.io/en/articles/489570-getting-started-with-aiven-influxdb)
- [ ] Aiven Grafana service -  [instructions](https://help.aiven.io/en/articles/489587-getting-started-with-aiven-grafana)

*all Aiven Services need to be in the same project*

1. In your Aiven console, head to your InfluxDB service. On the **Overview** tab, enable **Kafka REST API (Karapace)**.
2. In the same overview tab, scroll down to the Service integrations row and click **Manage integrations**.
3. Use **Metrics** as an integration type, and choose your InfluxDB service.
4. Head to the Overview tab of your InfluxDB service and add the Grafana integration under the **Dashboard** integration type

All done! You've just set up your managed Kafka service, with monitoring and metrics enabled by InfluxDB and Grafana. 

#### Existing libraries used

- [kafka-python](https://github.com/dpkp/kafka-python) - Kafka client 

#### Attribution:

Aiven help center articles
* https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
* https://help.aiven.io/en/articles/489570-getting-started-with-aiven-influxdb
* https://help.aiven.io/en/articles/489587-getting-started-with-aiven-grafana
* https://help.aiven.io/en/articles/1456441-getting-started-with-service-integrations

#### To do
* Better logging 
* Tests
* Template Grafana panels/dashboards?
 
