Feature: Check simple object rendering

    Scenario Outline: Render test of an arbitrary object
        Given Blender is installed and prepared
        When <size> <mesh> is added to the scene
        Then it can be rendered in <resolution>

    Examples:
        |size   |mesh 	  |resolution |
        |small  |circle   |640x480 	  |
        |normal |circle   |10x10  	  |
        |huge   |circle   |1000x10000 |
        |small  |uv_sphere|10x10   	  |
        |normal |uv_sphere|1000x10000 |
        |huge   |uv_sphere|1920x1080  |
        |huge   |uv_sphere|640x480 	  |
        |normal |torus	  |1920x1080  |
        |huge   |torus	  |640x480 	  |
        |huge   |torus	  |10x10   	  |
        |small  |torus	  |1000x10000 |
        |small  |circle   |1920x1080  |
        |normal |circle   |640x480 	  |





    