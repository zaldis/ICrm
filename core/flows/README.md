# Business flows

It is used when few tasks are interconnected, and it is necessary to control their dependencies flexibly.

Oftentimes it is related when several users are involved in a business process.

`Client` should not call Tasks and Processes directly.
Instead of it the API should be implemented in the `node_runner.py` module.


### API

```mermaid
---
title: Class Diagram
---
classDiagram
    Node *-- Flow
    Process *-- Flow
    Task *-- Process
    Task <.. Node
        
    class Flow{
        +nodes: Node
        -process: Process
    }
    class Process{
        +flow_process: str
        +task_set: list[Task]
        +artifact: object
        +status: str
    }
    class Node{
        +run(task: Task)
    }
    class Task{ 
       +flow_task: str
       +status: str
    }
```


### DB representation

`Process` entity saves the state of entire business process.

`Task` entity saves the state of separated tasks.

```mermaid
---
title: ER Diagram
---
erDiagram
    Process {
        integer id
        string status
        datetime created
        datetime finished
    }
    Task {
        integer id
        integer process_id
        integer previous
        string status
        datetime created
        datetime started
        datetime finished
    }
    Process ||--o{ Task : process_id
    Task ||--o{ Task : previous
```
