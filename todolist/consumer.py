from confluent_kafka import Consumer, KafkaError
import json

def consume_kafka_topic():
    conf = {
        'bootstrap.servers': 'localhost:9092',  
        'group.id': 'my-consumer-group',       
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(conf)
    consumer.subscribe(['my-topic'])  

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Reached end of partition')
            else:
               pass

        else:
            value = msg.value().decode('utf-8')
            message_data = json.loads(value)
        
            print(message_data)

if __name__ == '__main__':
    consume_kafka_topic()
