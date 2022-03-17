# PsdCompiler

### Tool to generate photoshop file with multiple pages (currently manga translation template)

---
<br/>

## How to use

- you must have installed Adobe Photoshop. (Tested with Photoshop 2021)
- [download program](https://github.com/Bohdan-TheOne/PsdCompiler/releases)
  - download executable and create or copy config.yaml file. Place them in same directory 
  - OR download source and execute with python3
- create referenced file (*.psd). This will set main options for resulting file (size, colormode, resolution).
- edit [config.yaml](https://github.com/Bohdan-TheOne/PsdCompiler/blob/master/config.yaml) file filling with prefered options
- start executable

---
<br/>

## Configuration

program is configured via config.yaml which has such structure:
```
config:
  source: 
    value: '.source/first/source'
    type: path
  destination: 
    value: ''
    type: path
  template: 
    value: '.source/sample.psd'
    type: path
  precise: 
    value: true
    type: boolean
```

| option      | description                                                                        | type          | required |
| ----------- | ---------------------------------------------------------------------------------- | ------------- | -------- |
| source      | folder that contains images, pages in output would be named accordingly            | path (string) | Yes      |
| destination | path and name of resulting file. save file near source folder with name output.psd | path (string) | No       |
| template    | sample file with basic photoshop document configuration                            | path (string) | Yes      |
| precise     | generate separate files for images that have different size                        | boolean       | Yes      |

---
<br/>

## Starting from source
```
python3 main.py
```

optional positional parameter - config file
```
python3 main.py custom_config.yaml
```
