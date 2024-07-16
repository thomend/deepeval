import logging
from typing import Any

class Integrations:

    @staticmethod
    def trace_langchain():
        try:
            from wrapt import wrap_function_wrapper
            from deepeval.integrations.langchain.callback import (
                LangChainCallbackHandler,
            )
            from deepeval.integrations.langchain import _BaseCallbackManagerInit

            wrap_function_wrapper(
                module="langchain_core.callbacks",
                name="BaseCallbackManager.__init__",
                wrapper=_BaseCallbackManagerInit(LangChainCallbackHandler(send_trace=False)),
            )
            logging.info("Langchain tracing setup completed.")
        except Exception as e:
            logging.error(f"Error setting up Langchain tracing: {e}")

    @staticmethod
    def trace_llama_index():
        try:
            from deepeval.integrations.llama_index.callback import LlamaIndexCallbackHandler
            import llama_index.core
            
            llama_index.core.global_handler = LlamaIndexCallbackHandler(send_trace=False)
            logging.info("Llama Index tracing setup completed.")
        except Exception as e:
            logging.error(f"Error setting up Llama Index tracing: {e}")
