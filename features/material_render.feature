Feature: Check simple material rendering

    Scenario Outline: Render test of simple material
        Given Blender is installed and prepared
        When material with <color> <metal> and <specular> intensity is applied to <mesh>
        Then scene can be rendered

    Examples:
        | color  | metal    |specular |mesh         |
        | random | high		|high	  |circle   	|
        | random | low	 	|low	  |torus		|
        | random | normal	|normal   |uv_sphere	|
        | random | low	 	|normal   |circle		|
        | random | normal	|high	  |torus		|
        | random | high		|low	  |uv_sphere	|
        | random | normal	|low	  |circle		|
        | random | high     |normal   |torus		|
        | random | low	 	|high	  |uv_sphere	|

    
    Scenario Outline: Render test of different lightning
    Given Blender is installed and prepared
    When <mesh> with <material> is added to the world
    Then scene can be rendered with <light> as light source

    Examples:
    | light | material | mesh      |
    | sun   | random   | circle    |
    | sun   | random   | torus     |
    | sun   | random   | uv_sphere |
    | point | random   | uv_sphere |
    | point | random   | circle    |
    | point | random   | torus     |
    | spot  | random   | circle    |
    | spot  | random   | torus     |
    | spot  | random   | uv_sphere |
    | area  | random   | uv_sphere |
    | area  | random   | circle    |
    | area  | random   | torus     |




        

