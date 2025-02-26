from typing import Optional

from langflow.base.memory.memory import BaseMemoryComponent
from langflow.field_typing import Text
from langflow.schema.schema import Record

from langchain_core.messages import BaseMessage
from langchain_astradb import AstraDBChatMessageHistory


class AstraDBMessageWriterComponent(BaseMemoryComponent):
    display_name = "Astra DB Message Writer"
    description = "Writes a message to Astra DB."

    def build_config(self):
        return {
            "input_value": {
                "display_name": "Input Record",
                "info": "Record to write to Astra DB.",
            },
            "session_id": {
                "display_name": "Session ID",
                "info": "Session ID of the chat history.",
                "input_types": ["Text"],
            },
            "collection_name": {
                "display_name": "Collection Name",
                "info": "Collection name for Astra DB.",
                "input_types": ["Text"],
            },
            "token": {
                "display_name": "Astra DB Application Token",
                "info": "Token for the Astra DB instance.",
                "password": True,
            },
            "api_endpoint": {
                "display_name": "Astra DB API Endpoint",
                "info": "API Endpoint for the Astra DB instance.",
                "password": True,
            },
            "namespace": {
                "display_name": "Namespace",
                "info": "Namespace for the Astra DB instance.",
                "input_types": ["Text"],
                "advanced": True,
            },
        }

    def add_message(
        self,
        sender: str,
        sender_name: str,
        text: Text,
        session_id: str,
        metadata: Optional[dict] = None,
        **kwargs,
    ):
        """
        Adds a message to the AstraDBChatMessageHistory memory.

        Args:
            sender (Text): The type of the message sender. Valid values are "Machine" or "User".
            sender_name (Text): The name of the message sender.
            text (Text): The content of the message.
            session_id (Text): The session ID associated with the message.
            metadata (dict | None, optional): Additional metadata for the message. Defaults to None.
            **kwargs: Additional keyword arguments.

        Raises:
            ValueError: If the AstraDBChatMessageHistory instance is not provided.

        """
        memory: AstraDBChatMessageHistory | None = kwargs.pop("memory", None)
        if memory is None:
            raise ValueError("AstraDBChatMessageHistory instance is required.")

        text_list = [
            BaseMessage(
                content=text,
                sender=sender,
                sender_name=sender_name,
                metadata=metadata,
                session_id=session_id,
            )
        ]

        memory.add_messages(text_list)

    def build(
        self,
        input_value: Record,
        session_id: Text,
        collection_name: str,
        token: str,
        api_endpoint: str,
        namespace: Optional[str] = None,
    ) -> Record:
        try:
            pass
        except ImportError:
            raise ImportError(
                "Could not import langchain Astra DB integration package. "
                "Please install it with `pip install langchain-astradb`."
            )

        memory = AstraDBChatMessageHistory(
            session_id=session_id,
            collection_name=collection_name,
            token=token,
            api_endpoint=api_endpoint,
            namespace=namespace,
        )

        self.add_message(**input_value.data, memory=memory)
        self.status = f"Added message to Astra DB memory for session {session_id}"

        return input_value
