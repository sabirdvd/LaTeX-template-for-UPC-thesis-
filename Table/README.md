## How to make nice Table 

```tex 

\section{Table}
% First version of table.
\begin{tabular}{|l|c|c|c|c|c|c|}\hline
Model & \multicolumn{3}{c|}{Unigram} & \multicolumn{3}{c|}{Bigram}\\
           & $word$  & score &  run time    & word count  & score  & run time  \\\hline
Baseline   & 11034 & 1.3e-7 & 3.9 & 15846 & 2.7e-11 & 5.6 \\
A (cite)  & 21952 & 1.3e-7 & 6.2 & 31516 & 2.7e-11 & 8.8 \\
B (cite)  & 15883 & 5.2e-8 & 7.1 & 32023 & 1.1e-11 & 1.4\\
C (cite)   & 11180 & 8.0e-9 & 4.3 & 17348 & 1.5e-11 & 6.6 \\\hline
\end{tabular}


\section{Better version with booktabs}

% better version with booktabs.
\begin{tabular}{lcccccc}\toprule
& \multicolumn{3}{c}{Unigram} & \multicolumn{3}{c}{Bigram}
\\\cmidrule(lr){2-4}\cmidrule(lr){5-7}
           & $word$  & score &  run time    & word count  & score  & run time  \\\hline
Baseline   & 11034 & 1.3e-7 & 3.9 & 15846 & 2.7e-11 & 5.6 \\
A (cite)  & 21952 & 1.3e-7 & 6.2 & 31516 & 2.7e-11 & 8.8 \\
B (cite)  & 15883 & 5.2e-8 & 7.1 & 32023 & 1.1e-11 & 1.4\\
C (cite)   & 11180 & 8.0e-9 & 4.3 & 17348 & 1.5e-11 & 6.6 \\\bottomrule
\end{tabular}

``` 

```
pdflatex main.tex
```
output sample ``main.pdf``
