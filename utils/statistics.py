def get_stat_dict(characteristics: dict) -> dict:

    keys = ['diag', 'volume', 'surface_area', 'alpha', 'beta', 'gamma',
        'radius_described_sphere', 'volume_described_sphere']

    all_values = {key: [] for key in keys}
    avg_values = {}

    for figure in characteristics.values():
        for key in keys:
            all_values[key].append(float(figure[key]))

    for key in keys:
        avg_values[f"avg_{key}"] = str(round(sum(all_values[key]) / len(all_values[key]), 2))

    statistics = avg_values

    print(f'\n{"-"*45}')
    print('###___STATISTICS__###\n\n')
    for k, v in statistics.items():
        print(f'\t{k}\t\t\t\t{v}')
    print(f'\n{"="*45}')


    return statistics
