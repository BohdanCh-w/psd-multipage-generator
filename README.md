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

currenly template file must have next structure. This will be changed in future versions
```
page (group)
|--- text (group)
|--- clean (clear layer)
|--- img (clear layer)
```

program is configured via config.yaml which has such structure:
```
source: 'path/to/project/images'
destination: 'path/to/project/result.psd'
template: 'C:/user/user/sample.psd'
precise: false
```

| option      | description                                                                    | type          | required |
| ----------- | ------------------------------------------------------------------------------ | ------------- | -------- |
| source      | folder that contains images, pages in output would be named accordingly        | path (string) | Yes      |
| destination | path to resulting file. Default - file near source folder with name output.psd | path (string) | No       |
| template    | sample file with basic photoshop document configuration                        | path (string) | Yes      |
| precise     | generate separate files for images that have different size                    | boolean       | Yes      |

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
