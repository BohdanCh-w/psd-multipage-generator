# PsdCompiler

### Tool to generate photoshop file with multiple pages

---
<br/>

## Getting started

- you must have installed Adobe Photoshop. (Tested with Photoshop 2021)
- [download program](https://github.com/BohdanCh-w/psd-multipage-generator/releases)
  - download executable and create or copy config.yaml file. Place them in same directory 
  - OR download source and execute with python3
- create referenced file (*.psd). This will set main options for resulting file (size, colormode, resolution, inner structure).
- edit [config.yaml](https://github.com/BohdanCh-w/psd-multipage-generator/blob/master/docs/config.yaml) file filling with prefered options
- start executable

---
<br/>

## Requirements

### python - v3.11+
### Packages:
 - PyYAML
 - pywin32

---
<br/>

## Configuration

Output .psd file is a copy of template file, preserving its configuration. Inner structure should contain only one group at the top level. This group must contain exactly one layer with name `img` where picture will be placed. Other layers will be copied.
Names of img layer and group layer will reflect corresponding name of source image.

```
page [group]
├── text
├── adjustment_layers
│   ├── levels
│   ├── brightness
├── img [empty layer]
```

So this kind of configuration will be copiled (assuming that source has files `01.png`, `02.png`, `03.png`) into:
```
01
├── text
├── adjustment_layers
│   ├── levels
│   ├── brightness
├── 01
02
├── text
├── adjustment_layers
│   ├── levels
│   ├── brightness
├── 02
03
├── text
├── adjustment_layers
│   ├── levels
│   ├── brightness
├── 03
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
| precise     | group files by dimensions                                                      | boolean       | No       |

---
<br/>

## Starting from source
```
python3 src/main.py
```

optional positional parameter - config file
```
python3 src/main.py custom_config.yaml
```
