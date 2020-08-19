# NOQA: D100

import argparse

from .cropscale import cropscale_filter
from .cropscale import DEFAULT_SAR_HEIGHT
from .cropscale import DEFAULT_SAR_WIDTH
from .cropscale import DEFAULT_WANTED
from .utils import DEFAULT_EXECUTABLE
from .utils import probe_streams

def _split_area(area):  # NOQA: D103, E302
    return tuple(map(int, area.split(":", 1)))

def main():  # NOQA: D103, E302
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-g", "--given",
        metavar="AREA",
        dest="given",
        action="store",
        type=_split_area,
        help="given area",
    )
    parser.add_argument(
        "-w", "--wanted",
        metavar="AREA",
        dest="wanted",
        action="append",
        type=_split_area,
        help="wanted area"
    )
    parser.add_argument(
        "-x", "--executable",
        metavar="EXECUTABLE",
        dest="executable",
        action="store",
        default=DEFAULT_EXECUTABLE,
        help="path to ffprobe",
    )
    parser.add_argument(
        "videofile",
        metavar="VIDEOFILE",
        type=str,
        nargs="?",
        help="videofile"
    )
    args = parser.parse_args()

    if args.given:
        width, height = args.given
        sar_width, sar_height = DEFAULT_SAR_WIDTH, DEFAULT_SAR_HEIGHT
    elif args.videofile:
        videofile = args.videofile
        executable = args.executable
        metadata = probe_streams(
            videofile,
            streams="v:0",
            executable=executable,
        )

        width = metadata[0]["width"]
        height = metadata[0]["height"]
        sar = metadata[0].get("sample_aspect_ratio", None)
        if sar:
            sar_width, sar_height = _split_area(sar)
        else:
            sar_width, sar_height = DEFAULT_SAR_WIDTH, DEFAULT_SAR_HEIGHT

    if args.wanted:
        wanted = args.wanted
    else:
        wanted = DEFAULT_WANTED

    result = cropscale_filter(
        width=width,
        height=height,
        sar_width=sar_width,
        sar_height=sar_height,
        wanted=wanted,
    )
    print(result)
