from os import environ

sample_file = """---
config: 
    theme: 'base'
    themeVariables:
        primaryColor: '#BB2528'
        primaryTextColor: '#fff'
        primaryBorderColor: '#7C0000'
        lineColor: '#F8B229'
        secondaryColor: '#006100'
        tertiaryColor: '#fff'
---
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop HealthCheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!"""

with open(
    f"{environ['OUTPUT_DIR']}/{environ['BASENAME']}.{environ['EXTENSION']}", "w"
) as file:
    print(sample_file, file=file)
