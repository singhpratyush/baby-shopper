# Baby Shopper

Simple program to find optimal shop for your baby shopping list.

### Requirements
`python>=3.5`

### Usage
```bash
$ python shopper.py <data_file.csv> [product1 product2 ...]
```

### Data File Format

The data file should be a CSV with delimiter `,`. Each line should contain
* Shop ID
* Price
* Products (separated by comma)
in exact order.

If the CSV has a header, modify the call to `data.read_data()` in `shopper.py` indicating argument 1 as `True`.


<br/><br/>

---
Created as a solution to challenge by DataOne Innovation Labs.