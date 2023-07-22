import argparse

import torch
import numpy as np


def set_seed(seed: int) -> None:
    """Sets various random seeds."""
    torch.manual_seed(seed)
    np.random.seed(seed)


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Atlas expansion script.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    required_named = parser.add_argument_group("required named arguments")
    required_named.add_argument(
        "--bibtex_fp",
        required=True,
        type=str,
        # default="data/hafenLowredshiftLymanLimit2017.bib",
        help="Bibtex file containing the initial (and center, if appropriate) publication.",
    )
    required_named.add_argument(
        "--atlas_dir",
        required=True,
        type=str,
        # default="outputs/default_atlas_dir",
        help="Atlas binary files will be saved/overwritten in this directory.",
    )

    parser.add_argument("--seed", type=int, default=42, help="Specify the random seed.")
    parser.add_argument(
        "--target_size",
        type=int,
        default=10000,
        help="The target size for an Atlas to attain via iterative expansion.",
    )
    parser.add_argument(
        "--max_pubs_per_expand",
        type=int,
        default=1000,
        help="The maximum number of publications to query an API for in one expand call.",
    )
    parser.add_argument(
        "--centered",
        type=bool,
        default=True,
        help="Whether to retrieve publications in order of similarity to the center publication. If False, retrieves a random sample of citations and references in the Atlas accumulated from the previous iteration.",
    )
    parser.add_argument(
        "--center_idx",
        type=int,
        default=0,
        help="The index of the entry in the bibtex file to use as the center of expansion.",
    )

    args = parser.parse_args()
    return args
