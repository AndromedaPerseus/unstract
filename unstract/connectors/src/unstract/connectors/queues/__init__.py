from unstract.connectors import ConnectorDict  # type: ignore
from unstract.connectors.queues.register import register_connectors

connectors: ConnectorDict = {}
register_connectors(connectors)
