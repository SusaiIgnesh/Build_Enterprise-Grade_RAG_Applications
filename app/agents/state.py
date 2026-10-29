from typing import Annotated, List, TypedDict
import operator


class AgentState(TypedDict):
    ### Using Annotated with operator.add ensure that messages
    ## are appended to the history rather that replace

    messages: Annotated[List[dict], operator.add]
    current_query: str
    documents: List[str]
    plan: List[str]
    status: str
    final_answer: str