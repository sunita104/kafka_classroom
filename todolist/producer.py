from confluent_kafka import Producer

def produce_kafka_message(topic, message):
    producer = Producer({'bootstrap.servers': 'localhost:9092'})  

    message_json = json.dumps(message)
    producer.produce(topic, key=None, value=message_json)
    producer.flush()

if __name__ == '__main__': 
    message_data = {
        'action': 'add',
        'task': 'Complete assignment'
    }

    topic_name = 'my-topic'
    produce_kafka_message(topic_name, message_data)
