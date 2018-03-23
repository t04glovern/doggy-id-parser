<img src="https://raw.githubusercontent.com/t04glovern/doggy-id-parser/master/img/project-banner.png" data-canonical-src="https://raw.githubusercontent.com/t04glovern/doggy-id-parser/master/img/project-banner.png" align="center"/>

<div align = "center">
    <h1>DoggyID <em>Parser</em></h1>
    <p>Official Doggy Generation Library for the CryptoDoggies Ethereum Smart Contract.</p>
    <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3.6.4-blue.svg" alt="Python"></a>
</div>

## About

This library exports a single function `doggyidparser` which takes a 5 byte hex `doggyId` and returns a 2D array of hex color value strings, or `null` for transparency.

You can view a demo of this library running here: [https://t04glovern.github.io/doggy-id-parser/](https://t04glovern.github.io/doggy-id-parser/)

### Setup

The PPM definitions for the types of images output can be found in `doggyidparser.js` under the `var designs` field. You can use the `image2ppm` python util that is also in this project. Check the [README](/image2ppm/README.md) for more inforamtion on how to generate lists of PPM strings.

## Web Example

```html
<!DOCTYPE HTML>
<html>
<head>
    <style>
        body {
            margin: 0px;
            padding: 0px;
            }
    </style>
</head>
    <body>
        <canvas id="canvas"></canvas>
        <script src="doggyidparser.js"></script>
        <script>

            generateDoggyImage("0x00f9e605e3", 2)

            function generateDoggyImage(doggyId, size){
                size = size || 10;
                var data = doggyidparser(doggyId);
                var canvas = document.getElementById("canvas");
                canvas.width = size * data.length;
                canvas.height = size * data[1].length;
                var ctx = canvas.getContext("2d");

                for(var i = 0; i < data.length; i++){
                    for(var j = 0; j < data[i].length; j++){
                        var color = data[i][j];
                        if(color){
                        ctx.fillStyle = color;
                        ctx.fillRect(i * size, j * size, size, size);
                        }
                    }
                }
                return canvas.toDataURL();
            }
        </script>
    </body>
</html>
```

Here's a couple example of different random IDs:

![0x00f9e605e3](/img/example-pic.png)

## Attribution

This library was based heavily on the work done by [ponderware](https://github.com/ponderware/mooncatparser)
