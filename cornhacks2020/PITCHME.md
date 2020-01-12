# Javascript Sucks

---
## Probably some stuff about me


---
@snap[north span-100]
### Warmup
```javascript```
> 100 == 100
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript```
> 100 == 100
true
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript```
> 100 == 100
true
> 100 == "100"
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript```
> 100 == 100
true
> 100 == "100"
true
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript```
> 100 == 100
true
> 100 == "100"
true
> 100 == ["100"]
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
> "asdf" == "asdf"
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
> "asdf" == "asdf"
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
> [] == []
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
> let a = new String("100");
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
> let a = new String("100");
> a == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
> let a = new String("100");
> a == a
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
> let a = new String("100");
> a == a
true
> a = [];
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
> let a = new String("100");
> a == a
true
> a = [];
> a == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
> ["1", "2", "3"].map(parseInt)
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```javascript```
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```javascript```
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```javascript```
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
"123"
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```javascript```
> ["1", "2", "3"].map(parseInt)
[1, NaN, NaN]
> [1] + [2] + [3]
"123"
> [1, 2] + [3, 4]
```
@snapend

@snap[north span-100 fragment]
### Fun with arrays
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
> [1, 2, 3] == [1, 2, 3]
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```javascript```
> [1, 2, 3] == [1, 2, 3]
false
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```javascript```
> [1, 2, 3] == [1, 2, 3]
false
> [1, 2, 3] < [1, 2, 3]
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```javascript```
> [1, 2, 3] == [1, 2, 3]
false
> [1, 2, 3] < [1, 2, 3]
false
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```javascript```
> [1, 2, 3] == [1, 2, 3]
false
> [1, 2, 3] < [1, 2, 3]
false
> [1, 2, 3] <= [1, 2, 3]
```
@snapend

@snap[north span-100 fragment]
### <= != < || ==
```javascript```
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
### Wat
```javascript```
> [] + []
```
@snapend

@snap[north span-100 fragment]
### Wat
```javascript```
> [] + []
""
```
@snapend

@snap[north span-100 fragment]
### Wat
```javascript```
> [] + []
""
> [] + {}
```
@snapend

@snap[north span-100 fragment]
### Wat
```javascript```
> [] + []
""
> [] + {}
"[Object object]"
```
@snapend

@snap[north span-100 fragment]
### Wat
```javascript```
> [] + []
""
> [] + {}
"[Object object]"
> {} + []
```
@snapend

@snap[north span-100 fragment]
### Wat
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
> ""*"" == 0
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```javascript```
> ""*"" == 0
true
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```javascript```
> ""*"" == 0
true
> ""**"" == 1
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```javascript```
> ""*"" == 0
true
> ""**"" == 1
true
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```javascript```
> ""*"" == 0
true
> ""**"" == 1
true
> ""***"" == 2
```
@snapend

@snap[north span-100 fragment]
### Wat 2
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
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
```javascript```
> 42.toFixed(2)
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```javascript```
> 42.toFixed(2)
SyntaxError: Invalid or unexpected token
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```javascript```
> 42.toFixed(2)
SyntaxError: Invalid or unexpected token
> 42 .toFixed(2)
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```javascript```
> 42.toFixed(2)
SyntaxError: Invalid or unexpected token
> 42 .toFixed(2)
42.00
```
@snapend

@snap[north span-100 fragment]
### A footnote on whitespace
```javascript```
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
```javascript```
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
