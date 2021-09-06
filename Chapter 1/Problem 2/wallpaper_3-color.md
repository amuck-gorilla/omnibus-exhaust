# 2-COLOR WALLPAPER

1. **input** *corna*, *cornb*
2. **input** *side*
3. **for** *i* <- 1 to 100
   1. **for** *j* <- 1 to 100
      1. *x* <- *corna* + *i* X *side*/100
      2. *y* <- *cornb* + *j* X *side*/100
      3. *c* <- *int*(*x<sup>2</sup>* + *y<sup>2</sup>*)
      4. **if** *c* modulo 3 = 0
         1. **then** *plot*(*i*, *j*, *first color*)
      5. **else if** *c* modulo 3 = 1
         1. **then** *plot*(*i*, *j*, *second color*)
      6. **else**
         1. **then** *plot*(*i*, *j*, *third color*)
