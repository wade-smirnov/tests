Feature: Check simple material rendering

    Scenario Outline: Render test of simple material
        Given Blender with empty world is prepared
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
        

