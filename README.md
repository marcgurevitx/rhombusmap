# rhombusmap

```python
from rhombusmap import RhombusMap
rm = RhombusMap(diagonal=7)

rm[0, 0] = 13
assert rm[4, 3] == 13

rm[6, 2] = 7
assert rm[2, -1] == 7
```

![](rm-1.png)
