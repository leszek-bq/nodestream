from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from .desired_ingest import DesiredIngestion


JsonLikeDocument = Dict[str, Any]


@dataclass(slots=True)
class InterpreterContext:
    """Defines the state of the Interpretation at a given point of time.

    As a record from the pipeline traverses the series of components responsible for extracting data from it and
    converting it into a SubGraph, data must be viewed within the context of that pipeline. Variables and data mappings
    are stored that are later referenced by disperate components, each of which, coordinate through an InterpreterContext`.

    This data does live longer then the record's time spent in the pipeline and is discarded excepted for the stored `DesiredIngestion`.
    The `DesiredIngestion` represents the outcome of the work spent on the record as it passes through the pipeline.
    """

    document: JsonLikeDocument
    desired_ingest: DesiredIngestion
    mappings: Optional[Dict[Any, Any]] = field(default_factory=dict)
    variables: Optional[Dict[str, Any]] = field(default_factory=dict)
