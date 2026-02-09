## Design Decisions

The refactoring focuses on separating responsibilities and making dependencies explicit. Core concerns such as embedding generation, document storage, retrieval logic, and HTTP handling are split into dedicated modules and classes. The RAG workflow is encapsulated in a RagWorkflow class, while storage is abstracted behind a DocumentStore interface with interchangeable implementations (Qdrant or in-memory). This structure removes global state, improves readability, and allows each component to be reasoned about and tested independently.

## Trade-off Considered

For simplicity and to preserve existing behavior, application dependencies (embedding service, document store, and workflow graph) are initialized at startup rather than using a full dependency injection framework. Additionally, the Qdrant collection is recreated on startup to keep the demo deterministic, even though this would be unsafe in a production environment. These choices favor clarity and predictability over production robustness, which is acceptable given the scope of the task.

## Maintainability Improvements

Compared to the original single-file implementation, the refactored version improves maintainability by enforcing clear boundaries between layers, reducing coupling, and making future changes localized. New storage backends, embedding strategies, or workflow steps can be added with minimal impact on existing code. The design also makes unit testing straightforward, as each service can be instantiated and validated in isolation.
