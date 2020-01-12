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
