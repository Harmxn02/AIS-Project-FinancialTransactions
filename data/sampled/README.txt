The datasets in this directory were sampled from ../merged/merged_data.csv, using this code


```
n_rows = 1000
sampled_data = merged_data.sample(n=n_rows)
sampled_data.write_csv(f"./data/sampled/sampled_data_{n_rows}.csv")
```