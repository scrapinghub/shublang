# Shublang (work in progress)

Pluggable DSL that uses pipes to perform a series of linear transformations to extract data. Provides several Python 
built-ins, list, string methods, JMESPath, XPath functions as well as allows creation of custom functions.  

Clear semantics makes for code that is easily understandable by non-technical business users and analysts. 
Also the grammar is terse enough for automatic generation through user guided interactions.

## Specification
Interpreted in Python. 

Directly translated or compiled to JS. The developer should have all the tools to debug the pipe in the browser.

Encompass Python built-ins, list and string methods, important functions from Cypher, JMESPath, XPath etc.

Proof of concept built using [pipe](https://github.com/JulienPalard/Pipe) 

Switch to using [Lark](https://github.com/lark-parser/lark), shlex, Ply, Antlr, TextX, PyParsing or 
another alternative.

## Example

Here is some Python [code](https://bitbucket.org/scrapinghub/smartersorting/src/f9b437f55b4895e9d9b88a8fae1d9462ab76c793/smartersorting/spiders/heb_com.py#lines-25) 
to extract data from a web page

```python

    values = map(clean_text, values)
    values = filter(None, values)
    text = ' '.join(values)
    text = text[:-1] if text[-1] == '.' else text
    text = re.sub(r'(active|other|inactive)\s+ingredients?\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\)\.\s*', '), ', text)
    text = re.sub(r'\s+\(', ' (', text)
```

Here is the code in shublang

```python
    data
    | sanitize
    | sub(r'(Active|Other|Inactive)\s+Ingredients?\s*:\s*', '')
    | sub(r'\)\.\s*', '), ')
    | sub(r'\s+\(', ' (',)
    | sub(r'.$', '',)
    | first

```


## Guideline on Using Pipes

Pipes are useful for rewriting a fairly short linear sequence of operations.

1. Pipes should ideally not be longer than 10 steps. In cases where pipes are exceeding this, create custom functions 
for the intermediate processing steps  

2. Pipe should transform a single primary object that return a single output. If there are multiple inputs/objects
being combined together, do not use a pipe.

3. Pipes are linear and expressing complex directed graph like relationships will result in convoluted code

General rule of thumb is to think of Shublang pipes as the code that is written inside Scrapy item loaders or pipelines.


## Features

Batteries included for quick and easy text extraction
Clean functional design
Pluggable architecture for adding custom functions
Directly translates to Javascript
Tracing to aid debugging


Shublang will look to support the following language features and functions.

|Logical and Execution Flow Constructs|
|-------------------------------------|
|skip_while                           |
|take_while                           |
|where                                |
|select                               |
|skip                                 |


|Predicate Functions                  |
|-------------------------------------|
|all                                  |
|any                                  |
|exists                               |
|none                                 |
|single                               |


|Scalar Functions                     |
|-------------------------------------|
|length                               |
|bool                                 |
|float                                |
|int                                  |
|timestamp                            |


|Aggregating Functions                |
|-------------------------------------|
|avg                                  |
|max                                  |
|min                                  |
|sum                                  |
|aggregate                            |
|groupby                              |


|List Functions|
|--------------|
|range         | 
|count         |
|reverse       |
|map           |
|filter        |
|sort          |
|slice         |
|append        |
|extend        |
|chain         |
|chain_with    |
|tail          |
|first         |

|Mathematical Functions|
|----------------------|
|abs                   |
|ceil                  |
|floor                 |
|rand                  |
|round                 |

|String Functions|
|----------------|
|format          |
|join            |
|split           |
|find            |
|capitalize      |
|strip           |
|replace         |
|startswith      |
|endswith        |
|encode          |
|decode          | 
|is_digit        |
|is_decimal      |
|rstrip          |
|lstrip          |


|Temporal Functions|
|------------------|
|date_format       |


|HTML and JSON Functions|
|-----------------------|
|jmespath               |
|remove_html            |
|clean_text             |
|xpath                  |
|css                    |
|table                  |



## Next Steps and Research

- Piping concepts from R (magritrr), Elixir and Javascript 
- Conventions from sed, awk, Perl to make the code terse (but not at the cost of semantics) 
- Pandas dataframe like fluent API to deal with HTML structures such as tables
- [Type-safe functional pipeline in TypeScript](https://github.com/ts-delight/pipe)
- Should be directly translated to Javascript. See [proposal](https://github.com/tc39/proposal-pipeline-operator) for 
pipelines in Javascript
- Rewrite pipe library with '|>' operator based on above findings
- Avoid the need to write lambdas
- DSL design and creation of EBNF grammar
- [cmd2's use of shlex](https://github.com/python-cmd2/cmd2)
- [Macropy's tracing](https://macropy3.readthedocs.io/en/latest/tracing.html) -  aid for debugging
- Overlap between functions exposed on Extraction UI and pertinent Microsoft Excel Formulae
- Auto-generation of code based on user interactions