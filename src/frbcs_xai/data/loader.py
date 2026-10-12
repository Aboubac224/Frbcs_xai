

"""Load the banknote authentication dataset from UCI."""


from ucimlrepo import  fetch_ucirepo


def load_uci_dataset(dataset_id: int):
    """Load features and targets from UCI."""

    dataset = fetch_ucirepo(id=dataset_id)

    X = dataset.data.features
    y = dataset.data.targets

    if X is None or y is None:
        raise ValueError("Dataset features or targets are unavailable.")

    return X, y
