"""A script to generate slide content for my presentation.

You see, to get the display that I want I would have to retype a lot of
stuff. This script works by passing in lines of code you want fragmentized,
and then all you have to do is copy paste it into your pitchme.
"""

def fragmentize(title, lines, zoom=35):
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
        slide_content.extend(get_snap_block(title, lines[:i+1], zoom, fragment=(i != 0), endline=(i != len(lines) - 1)))
    return "\n".join(slide_content)


def get_snap_block(title, lines, zoom=35, fragment=True, endline=True):
    snap_lines = [
        "@snap[north span-100 fragment]" if fragment else "@snap[north span-100]",
        f"### {title}",
        f"```javascript zoom-{zoom}```"
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
        "> 100 == a",
        "true",
        "> a = [];",
        "> a == a",
        "true",
        "> a = {};",
        "> a == a",
        "true",
        "> a = NaN;",
        "> a == a",
        "false"
    ], zoom=30))
    return

if __name__ == "__main__":
    make_slides()
