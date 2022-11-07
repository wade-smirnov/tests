Feature: Check simple object rendering

    Scenario Outline: Render test of an arbitrary object
        Given Blender with empty world is prepared
        When <size> <mesh> is added to the scene
        Then it can be rendered in <resolution>

    Examples:
        |size   |mesh 	  |resolution |
        |small  |circle   |640x480 	  |




    