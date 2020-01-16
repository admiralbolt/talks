@snap[north span-100]
### The Year is 2020

@css[fragment](Javascript had been the most popular language for the past 6 consecutive years.)
@css[fragment](As of January, NPM had 1.1 million packages)

@snap[fragment]
![React](/cornhacks2020/assets/images/react.png)
![Angular](/cornhacks2020/assets/images/angular.png)
![Vue](/cornhacks2020/assets/images/vue.png)
![Ember](/cornhacks2020/assets/images/ember.png)
@snapend

@snapend

---
@snap[north span-100]
### The Year is 2025

@css[fragment](Javascript was the **only** language used by a majority of developers.)

@snap[fragment]
![Electron](/cornhacks2020/assets/images/electron.png)
![Ionic](/cornhacks2020/assets/images/ionic.png)
![NodeJs](/cornhacks2020/assets/images/nodejs.png)
@snapend

@snap[span-100]
@css[fragment](Google finally released its highly anticipated 3rd rewrite of Angular:)
@css[fragment](Angular 2)
@css[fragment](Kernels were the only things left not written in javascript)
@snapend
---
@snap[north span-100]
### The Year is 2030

@css[fragment](Javascript is the **only** language run on most machines)
@snap[fragment]
![NodeOs](/cornhacks2020/assets/images/node_os.png)
@snapend
@snapend
---
# Javascript Sucks
---
@snap[north span-100]
### About Me

Graduated UNL in 2017.
Worked for Google for two years.
Currently working for Travefy.
@snapend

@snap[south span-100 text-left]
@fa[github] https://github.com/admiralbolt
@fa[linkedin] https://www.linkedin.com/in/aviknecht/
@snapend
---
@snap[north span-100]
### What I'm going to talk about
1. Convince you that javascript is a terrible language.
2. Talk about how it managed to become so popular despite being awful.
@snapend
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
> a = {};
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```js
> let a = new String("100");
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
> Object.keys(a)
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> Object.keys(a)
[""]
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
> Object.keys(a)
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
> Object.keys(a)
["", "1,2,3"]
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
> Object.keys(a)
["", "1,2,3"]
> a[{}] = 3
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
> Object.keys(a)
["", "1,2,3"]
> a[{}] = 3
> a[{b: 1}]
```
@snapend

@snap[north span-100 fragment]
### Fun with objects
```js
> let a = {}
> a[[]] = "yes"
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
> Object.keys(a)
["", "1,2,3"]
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
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
> Object.keys(a)
["", "1,2,3"]
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
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
> Object.keys(a)
["", "1,2,3"]
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
> Object.keys(a)
[""]
> a[[1, 2, 3]] = 5
> Object.keys(a)
["", "1,2,3"]
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
---
### Is Javascript a "bad" language?
---
### Yeah it sucks.
---
### How is a language so bad so popular?
---
@snap[north span-100]
### The year is 1995
@snapend

@snap[west span-33 fragment text-center]
![Netscape Communicator](/cornhacks2020/assets/images/netscape.png)
Netscape Navigator, the most popular browser at the time.
@snapend

@snap[midpoint span-33 fragment text-center]
![Marc Andreessen](/cornhacks2020/assets/images/marc_andreessen.jpeg)
Marc Andreessen, founder of Netscape.
@snapend

@snap[east span-33 fragment text-center]
![Sun](/cornhacks2020/assets/images/sun_microsystems.png)
Sun is already working with Netscape.
@snapend
---
@snap[north span-100]
### Mocha
@snapend

@snap[west span-33 fragment text-center]
![Mocha](/cornhacks2020/assets/images/mocha.jpg)
Mocha was born!
@snapend

@snap[midpoint span-33 fragment text-center]
![Brendan Eich](/cornhacks2020/assets/images/brendan_eich.jpg)
Created by Brendan Eich in 10 days.
@snapend

@snap[east span-33 fragment text-center]
![Javascript](/cornhacks2020/assets/images/javascript.png)
Eventually renamed to Javascript due to licensing with Sun.
@snapend
---
@snap[north span-100]
### JScript
@snapend

@snap[west span-33 fragment text-center]
![Internet Explorer](/cornhacks2020/assets/images/ie.png)
Other browsers needed javascript implementations.
@snapend

@snap[midpoint span-33 fragment text-center]
![Microsoft](/cornhacks2020/assets/images/microsoft.png)
Microsoft began working on reverse engineering Javascript.
@snapend

@snap[east span-33 fragment text-center]
![JScript](/cornhacks2020/assets/images/jscript.png)
Created their own implementation, JScript.
@snapend
---
@snap[north span-100]
### ECMAScript
@snapend

@snap[west span-33 fragment text-center]
![W3C](/cornhacks2020/assets/images/w3c.png)
Netscape initially went to W3C
@snapend

@snap[midpoint span-33 fragment text-center]
![ECMA](/cornhacks2020/assets/images/ecma.jpg)
Eventually landed on ECMA.
@snapend

@snap[east span-33 fragment text-center]
![ECMAScript](/cornhacks2020/assets/images/ecmascript.png)
Eventually the standard became ECMAScript.
@snapend
---
@snap[north span-100]
### Browser Wars
@snapend

@snap[midpoint span-100]
![Browser Wars](/cornhacks2020/assets/images/browser_wars.png)
@snapend
---
@snap[north span-100]
### Aftermath
@snapend

@snap[west span-33 fragment text-center]
![Firefox](/cornhacks2020/assets/images/firefox.png)
Netscape gave their code to Mozilla.
@snapend

@snap[midpoint span-33 fragment text-center]
![Trust Bust](/cornhacks2020/assets/images/trust_bust.jpg)
Microsoft got trust busted for bundling their browser & OS.
@snapend

@snap[east span-33 fragment text-center]
![No Internet](/cornhacks2020/assets/images/no_internet.png)
The war was won, Microsoft moved on to other things.
@snapend
---
### Javascript survived because of Microsoft.
---
### How is a language so bad so successful?
---
### It has no real competition.
---
@snap[north span-100]
### The Future?
@css[fragment](Full stack development can already be done in javascript.)

@snap[fragment]
![Doom](/cornhacks2020/assets/images/doom.png)
@snapend

@snapend
---
@snap[north span-100]
### History of JS Sources
[The History of Javascript](http://www.davevoyles.com/2014/10/24/history-javascript-told-douglas-crockford/) by Douglass Crockford
[The Javascript Programming Language](https://www.youtube.com/watch?v=v2ifWcnQs6M) by Douglass Crockford
[Brendan Eich's Blog](https://brendaneich.com)
[An Introduction to Javascript](https://www.youtube.com/watch?v=1EyRscXrehw) by Brendan Eich
[Interview with Brendan Eich](https://www.infoworld.com/article/2653798/javascript-creator-ponders-past--future.html)
[A Brief History of Javascript](https://auth0.com/blog/a-brief-history-of-javascript/) by Sebastian Peyrott
@snapend
---
@snap[north span-100]
### JS Sucks Sources
[Wat](https://www.destroyallsoftware.com/talks/wat) by Gary Bernhardt
[The Birth & Death of Javascript](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) by Gary Bernhardt
[What the Javascript](https://www.youtube.com/watch?v=2pL28CcEijU&feature=youtu.be) by Kyle Simpson

https://gist.github.com/MichalZalecki/c964192f830360ce6361
https://wtfjs.com/
http://www.bradoncode.com/blog/2015/08/26/javascript-semi-colon-insertion/
@snapend
---
### Thank you!

@snap[south span-100 text-left]
@fa[github] https://github.com/admiralbolt
@fa[linkedin] https://www.linkedin.com/in/aviknecht/
@snapend
