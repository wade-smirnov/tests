Feature: Check simple material rendering

    Scenario Outline: Render test of simple material
        Given Blender with empty world is prepared
        When material with <color> <metal> and <specular> intensity is applied to <mesh>
        Then scene can be rendered

    Examples:
        | color  | metal    |specular |mesh         |
        | random | high		|high	  |circle   	|

