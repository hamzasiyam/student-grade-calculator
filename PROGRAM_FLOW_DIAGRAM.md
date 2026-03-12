# Student Grade Calculator - Program Flow Diagram

## High-Level Module Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                         main.py                                  │
│                    (Orchestrates the flow)                       │
└───────────────┬─────────────────┬─────────────────┬────────────┘
                │                 │                 │
                ▼                 ▼                 ▼
        ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
        │ input_utils   │ │ calculations  │ │   display     │
        │               │ │               │ │               │
        │ • get_student_ │ │ • calculate_  │ │ • print_      │
        │   name()      │ │   student_    │ │   student_    │
        │ • get_student_│ │   average()   │ │   info()      │
        │   id()        │ │ • calculate_  │ │ • print_      │
        │ • get_validated│ │   class_      │ │   summary()   │
        │   _score()    │ │   average()   │ │               │
        │ • get_continue│ │               │ │               │
        │   _choice()   │ │               │ │               │
        └───────────────┘ └───────────────┘ └───────────────┘
```

## Detailed Program Flow (Mermaid)

```mermaid
flowchart TD
    Start([Start]) --> Init[Initialize: total_averages=0, student_count=0]
    Init --> LoopStart{Process Student}
    
    LoopStart --> GetName[get_student_name: First, Middle, Last]
    GetName --> GetID[get_student_id]
    GetID --> GetScore1[get_validated_score 1]
    GetScore1 --> Validate1{0 ≤ score ≤ 100?}
    Validate1 -->|No| GetScore1
    Validate1 -->|Yes| GetScore2[get_validated_score 2]
    GetScore2 --> Validate2{0 ≤ score ≤ 100?}
    Validate2 -->|No| GetScore2
    Validate2 -->|Yes| GetScore3[get_validated_score 3]
    GetScore3 --> Validate3{0 ≤ score ≤ 100?}
    Validate3 -->|No| GetScore3
    Validate3 -->|Yes| Calc[calculate_student_average]
    
    Calc --> AddTotal[total_averages += average]
    AddTotal --> PrintInfo[print_student_info]
    PrintInfo --> IncCount[student_count += 1]
    IncCount --> CalcClass[calculate_class_average]
    CalcClass --> AskContinue[get_continue_choice: y/n?]
    
    AskContinue --> Continue{Continue?}
    Continue -->|Yes| LoopStart
    Continue -->|No| PrintSummary[print_summary]
    PrintSummary --> End([End])
```

## Data Flow Between Modules

| Step | Module        | Function                 | Input                    | Output                    |
|------|---------------|--------------------------|--------------------------|---------------------------|
| 1    | input_utils   | get_student_name()       | (user input)             | first_name, middle, last  |
| 2    | input_utils   | get_student_id()         | (user input)             | student_id                |
| 3    | input_utils   | get_validated_score(n)   | prompt number            | score (0-100)             |
| 4    | calculations  | calculate_student_average| score1, score2, score3   | total, average            |
| 5    | display       | print_student_info()     | all student data         | (prints to console)       |
| 6    | calculations  | calculate_class_average  | total_averages, count    | class_average             |
| 7    | input_utils   | get_continue_choice()    | (user input)             | True/False                |
| 8    | display       | print_summary()          | count, class_average     | (prints to console)       |
