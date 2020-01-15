"""A script to generate slide content for my presentation.

You see, to get the display that I want I would have to retype a lot of
stuff. This script works by passing in lines of code you want fragmentized,
and then all you have to do is copy paste it into your pitchme.
"""

def fragmentize(title, lines):
    """Fragmentize some stuff.

    For example, if you call:
    fragmentize("js", ["> 1 == 1", "true"])

    You'll get:
    @snap[north span-100]
    ### JS
    ```javascript zoom-35
    > 1 == 1
    ```
    @snapend

    @snap[north span-100 fragment]
    ### JS
    ```javascript zoom-35
    > 1 == 1
    true
    ```
    @snapend
    """
    slide_content = []
    for i in range(len(lines)):
        slide_content.extend(get_snap_block(title, lines[:i+1], fragment=(i != 0), endline=(i != len(lines) - 1)))
    return "\n".join(slide_content)


def get_snap_block(title, lines, fragment=True, endline=True):
    snap_lines = [
        "@snap[north span-100 fragment]" if fragment else "@snap[north span-100]",
        f"### {title}",
        "```js"
    ]
    for line in lines:
        snap_lines.append(line.strip())
    snap_lines.extend(["```", "@snapend"])
    if endline:
        snap_lines.append("")
    return snap_lines

def make_slides():
    print(fragmentize("Warmup", [
        "> 100 == 100",
        "true",
        "> 100 == \"100\"",
        "true",
        "> 100 == [\"100\"]",
        "true",
        "> 100 == [\"1\", \"E\", \"2\"].join(\"\")",
        "true"
    ]))
    print("---")
    print(fragmentize("Are things equal to themselves?", [
        "> \"asdf\" == \"asdf\"",
        "true",
        "> new String(\"asdf\") == new String(\"asdf\")",
        "false",
        "> [] == []",
        "false",
        "> {} == {}",
        "false",
        "> NaN == NaN",
        "false"
    ]))
    print("---")
    print(fragmentize("Are things equal to themselves?", [
        "> let a = new String(\"100\");",
        "> a == a",
        "true",
        "> a = {};",
        "> a == a",
        "true",
        "> a = NaN;",
        "> a == a",
        "false"
    ]))
    print("---")
    print(fragmentize("Fun with arrays", [
        "> [\"1\", \"2\", \"3\"].map(parseInt)",
        "[1, NaN, NaN]",
        "> [1] + [2] + [3]",
        "\"123\"",
        "> [1, 2] + [3, 4]",
        "\"1,23,4\"",
        "> [1, 2, 3][3, 2, 1]",
        "2"
    ]))
    print("---")
    print(fragmentize("<= != < || ==", [
        "> [1, 2, 3] == [1, 2, 3]",
        "false",
        "> [1, 2, 3] < [1, 2, 3]",
        "false",
        "> [1, 2, 3] <= [1, 2, 3]",
        "true"
    ]))
    print("---")
    print(fragmentize("Fun with objects", [
        "> let a = {}",
        "> a[[]] = \"yes\"",
        "> Object.keys(a)",
        "[\"\"]",
        "> a[[1, 2, 3]] = 5",
        "> Object.keys(a)",
        "[\"\", \"1,2,3\"]",
        "> a[{}] = 3",
        "> a[{b: 1}]",
        "3",
        "> a[a] = a",
        "> a[{\"was\": \"this\"}][{\"a\": \"mistake?\"}][[]]",
        "\"yes\""
    ]))
    print("---")
    print(fragmentize("Wat", [
        "> [] + []",
        "\"\"",
        "> [] + {}",
        "\"[Object object]\"",
        "> {} + []",
        "0",
        "> [] - []",
        "0",
        "> {} - []",
        "-0",
        "> [] - {}",
        "NaN"
    ]))
    print("---")
    print(fragmentize("Misc", [
        "> \"\"*\"\" == 0",
        "true",
        "> \"\"**\"\" == 1",
        "true",
        "> \"\"***\"\" == 2",
        "Syntax Error: Unexpected token *",
        "> typeof(NaN)",
        "number",
    ]))
    print("---")
    print(fragmentize("A footnote on whitespace", [
        "> 42.toFixed(2)",
        "SyntaxError: Invalid or unexpected token",
        "> 42 .toFixed(2)",
        "42.00",
    ]))
    return

if __name__ == "__main__":
    make_slides()
