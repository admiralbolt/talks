# Javascript Sucks

---

## Add Some Slide Candy

![IMAGE](assets/img/presentation.png)

---
@snap[north span-100]
### Warmup
```javascript zoom-35```
> 100 == 100
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript zoom-35```
> 100 == 100
true
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript zoom-35```
> 100 == 100
true
> 100 == "100"
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript zoom-35```
> 100 == 100
true
> 100 == "100"
true
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript zoom-35```
> 100 == 100
true
> 100 == "100"
true
> 100 == ["100"]
```
@snapend

@snap[north span-100 fragment]
### Warmup
```javascript zoom-35```
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
```javascript zoom-35```
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
```javascript zoom-35```
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
```javascript zoom-35```
> "asdf" == "asdf"
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-35```
> "asdf" == "asdf"
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-35```
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-35```
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-35```
> "asdf" == "asdf"
true
> new String("asdf") == new String("asdf")
false
> [] == []
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-35```
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
```javascript zoom-35```
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
```javascript zoom-35```
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
```javascript zoom-35```
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
```javascript zoom-35```
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
```javascript zoom-20```
> let a = new String("100");
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
true
> a = [];
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
true
> a = [];
> a == a
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
true
> a = [];
> a == a
true
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
true
> a = [];
> a == a
true
> a = {};
```
@snapend

@snap[north span-100 fragment]
### Are things equal to themselves?
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
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
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
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
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
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
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
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
```javascript zoom-20```
> let a = new String("100");
> a == a
true
> 100 == a
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
