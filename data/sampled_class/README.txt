The datasets in this directory were sampled from ../merged/merged_data.csv, using this code


```
for n_rows in [100, 1000, 10_000, 100_000]:
	sampled_data = merged_data.sample(n=n_rows)
	sampled_data.write_csv(f"./data/sampled_class/sampled_data_{n_rows}.csv")
```