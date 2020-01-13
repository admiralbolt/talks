# Javascript Sucks

---
## Probably some stuff about me


---
@snap[north span-100]
### Warmup
```js
> 100 == 100
```
@snapend

@snap[north span-100 fragment]
### Warmup
```js
> 100 == 100
true
```
@snapend

@snap[north span-100 fragment]
### Warmup
```js
> 100 == 100
true
> 100 == "100"
```
@snapend

@snap[north span-100 fragment]
### Warmup
```js
> 100 == 100
true
> 100 == "100"
true
```
@snapend

@snap[north span-100 fragment]
### Warmup
```js
> 100 == 100
true
> 100 == "100"
true
> 100 == ["100"]
```
@snapend

@snap[north span-100 fragment]
### Warmup
```js
> 100 == 100
true
> 100 == "100"
true
> 100 == ["100"]
true
```
@snapend

@snap[north span-100 fragment]
### Warmup
```js
> 100 == 100
true
> 100 == "100"
true
> 100 == ["100"]
true
> 100 == ["1", "E", "2"].join("")
```
@snapend

@snap[north span-100 fragment]
### Warmup
```js
> 100 == 100
true
> 100 == "100"
true
> 100 == ["100"]
true
> 100 == ["1", "E", "2"].join("")
true
```
@snapend
---
@snap[north span-100]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
> [] == []
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
> [] == []
false
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
> [] == []
false
> {} == {}
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
> [] == []
false
> {} == {}
false
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
> [] == []
false
> {} == {}
false
> NaN == NaN
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
> [] == []
false
> {} == {}
false
> NaN == NaN
false
```
@snapend
---
@snap[north span-100]
### Are things equal to themselves?
```js
> let a = new String("100");
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
> a == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
> a == a
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
> a == a
true
> a = {};
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
> a == a
true
> a = {};
> a == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
> a == a
true
> a = {};
> a == a
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
> a == a
true
> a = {};
> a == a
true
> a = NaN;
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
> a == a
true
> a = {};
> a == a
true
> a = NaN;
> a == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
> a == a
true
> a = [];
> a == a
true
> a = {};
> a == a
true
> a = NaN;
> a == a
false
```
@snapend
---
@snap[north span-100]
### Fun with arrays
```js
> ["1", "2", "3"].map(parseInt)
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```js
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```js
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```js
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
"123"
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```js
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
"123"
> [1, 2] + [3, 4]
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```js
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
"123"
> [1, 2] + [3, 4]
"1,23,4"
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```js
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
"123"
> [1, 2] + [3, 4]
"1,23,4"
> [1, 2, 3][3, 2, 1]
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```js
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
"123"
> [1, 2] + [3, 4]
"1,23,4"
> [1, 2, 3][3, 2, 1]
2
```
@snapend
---
@snap[north span-100]
### <= != < || ==
```js
> [1, 2, 3] == [1, 2, 3]
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```js
> [1, 2, 3] == [1, 2, 3]
false
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```js
> [1, 2, 3] == [1, 2, 3]
false
> [1, 2, 3] < [1, 2, 3]
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```js
> [1, 2, 3] == [1, 2, 3]
false
> [1, 2, 3] < [1, 2, 3]
false
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```js
> [1, 2, 3] == [1, 2, 3]
false
> [1, 2, 3] < [1, 2, 3]
false
> [1, 2, 3] <= [1, 2, 3]
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```js
> [1, 2, 3] == [1, 2, 3]
false
> [1, 2, 3] < [1, 2, 3]
false
> [1, 2, 3] <= [1, 2, 3]
true
```
@snapend
---
@snap[north span-100]
### Fun with objects
```js
> let a = {}
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
> a["1, 2, 3"]
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
> a["1, 2, 3"]
5
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
> a["1, 2, 3"]
5
> a[{}] = 3
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
> a["1, 2, 3"]
5
> a[{}] = 3
> a[{b: 1}]
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
> a["1, 2, 3"]
5
> a[{}] = 3
> a[{b: 1}]
3
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
> a["1, 2, 3"]
5
> a[{}] = 3
> a[{b: 1}]
3
> a[a] = a
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
> a["1, 2, 3"]
5
> a[{}] = 3
> a[{b: 1}]
3
> a[a] = a
> a[{"was": "this"}][{"a": "mistake?"}][[]]
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> a[""]
"yes"
> a[[1, 2, 3]] = 5
> a["1, 2, 3"]
5
> a[{}] = 3
> a[{b: 1}]
3
> a[a] = a
> a[{"was": "this"}][{"a": "mistake?"}][[]]
"yes"
```
@snapend
---
@snap[north span-100]
### Wat
```js
> [] + []
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
0
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
0
> [] - []
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
0
> [] - []
0
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
0
> [] - []
0
> {} - []
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
0
> [] - []
0
> {} - []
-0
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
0
> [] - []
0
> {} - []
-0
> [] - {}
```
@snapend

@snap[north span-100 fragment]
### Wat
```js
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
0
> [] - []
0
> {} - []
-0
> [] - {}
NaN
```
@snapend
---
@snap[north span-100]
### Wat 2
```js
> ""*"" == 0
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
Syntax Error: Unexpected token *
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
Syntax Error: Unexpected token *
> typeof(NaN)
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
Syntax Error: Unexpected token *
> typeof(NaN)
number
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
Syntax Error: Unexpected token *
> typeof(NaN)
number
> Number(undefined)
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
Syntax Error: Unexpected token *
> typeof(NaN)
number
> Number(undefined)
NaN
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
Syntax Error: Unexpected token *
> typeof(NaN)
number
> Number(undefined)
NaN
> Number(null)
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```js
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
Syntax Error: Unexpected token *
> typeof(NaN)
number
> Number(undefined)
NaN
> Number(null)
0
```
@snapend
---
@snap[north span-100]
### A footnote on whitespace
```js
> 42.toFixed(2)
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```js
> 42.toFixed(2)
SyntaxError: Invalid or unexpected token
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```js
> 42.toFixed(2)
SyntaxError: Invalid or unexpected token
> 42 .toFixed(2)
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```js
> 42.toFixed(2)
SyntaxError: Invalid or unexpected token
> 42 .toFixed(2)
42.00
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```js
> 42.toFixed(2)
SyntaxError: Invalid or unexpected token
> 42 .toFixed(2)
42.00
> function asdf() {
    return
    {
      a: 1,
      b: 2
    }
  }
> asdf()
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```js
> 42.toFixed(2)
SyntaxError: Invalid or unexpected token
> 42 .toFixed(2)
42.00
> function asdf() {
    return
    {
      a: 1,
      b: 2
    }
  }
> asdf()
undefined
```
@snapend
