from faststream import FastStream, Logger
from faststream.kafka import KafkaBroker

broker = KafkaBroker("localhost:9092")

app = FastStream(broker)


@broker.subscriber("in")
@broker.publisher("out")
async def handler(msg: str, logger: Logger):
    """
    handler.
    """
    print("-----------------------------")
    print(f"Handling message: {msg}")
    print("-----------------------------")
    # logger.info(msg)
