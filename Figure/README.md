Different basic Latex Figure for data visualization 

To run the PDF figure 

```
pdflatex main.tex
```

## Fast Guide

1. [Color](http://latexcolor.com)

```tex
\usepackage[usenames,dvipsnames]{xcolor}
\definecolor{airforceblue}{rgb}{0.36, 0.54, 0.66}
airforceblue!30
```
2. Size

```tex
height=6cm, width=8.5cm,

``` 


3. Legend 

```tex
% position 
legend pos=south east,
legend pos=north east,
legend pos=outer north east

% No fill 
legend style={fill=none},

% customized 
legend style={
            at={(0.5,0.96)},
            anchor=west,
            mark size=1pt,
           legend columns=-1,
           /tikz/every even column/.append style={column sep=0.cm}
           every node near coord/.append style={font=\tiny}Sim
        },
```
4. Grid
```tex
% auto 
grid=major,
% y custom 
ymajorgrids, tick align=inside,
        
% color and style 
major grid style={draw=white}, 
major grid style={dashed, gray},
major grid  style={dashed,draw=gray!15},       
        
```        
        
5. Border line 

```tex
% Remove border line 
axis x line*=bottom,
axis y line*=bottom,
```



