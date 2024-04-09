from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='3.109.237.85:9092')
# Sending a simple string message
producer.send('my-topic', key=b'abc', value=b'Hello Kafka!')

# Ensure all messages are sent before exiting
producer.flush()
producer.close()
