## Kafka Service 

Open source repo to send JSON data to a Kafka service. Includes instructions to easily set up your DB infrasture (including easy integration with monitoring) with Aiven

### Installation intructions & env vars

Tested on Python version `3.9`

Environmental variables
* ``

### Aiven instructions

Pre steps requirements:
- [ ] Aiven Kafka service and a kafka topic - [instructions](https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka)
- [ ] Aiven Influxdb service - [instructions](https://help.aiven.io/en/articles/489570-getting-started-with-aiven-influxdb)
- [ ] Aiven Grafana service - [instructions](https://help.aiven.io/en/articles/489587-getting-started-with-aiven-grafana)
**Note that all services need to be in the same Aiven project**

1. In your Aiven console, head to your Influxdb service. On the **Overview** tab, scroll down to the Service integrations row and click **Manage integrations**.
2. Use **Metrics** as an integration type, and choose your Kafka service
3. Add the Grafana integration under the **Dashboard** integration type


#### Existing libraries used

- [kafka-python](https://github.com/dpkp/kafka-python) client 

#### Attribution: 

Aiven help center articles
* https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
* https://help.aiven.io/en/articles/489570-getting-started-with-aiven-influxdb
* https://help.aiven.io/en/articles/489587-getting-started-with-aiven-grafana
* https://help.aiven.io/en/articles/1456441-getting-started-with-service-integrations
 