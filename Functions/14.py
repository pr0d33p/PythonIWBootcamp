phones = [
    {'manufacturer':'Xiaomi', 'model':'Mi Note 8 Pro'},
    {'manufacturer':'Apple', 'model':'iPhone 12 Pro Max'},
    {'manufacturer':'Samsung', 'model': 'S21 Ultra'}
]
sorted_models = sorted(phones, key = lambda x: x['model'])
print("Sorted Dict: {}".format(sorted_models))