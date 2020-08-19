# NOQA: D100

import json
import subprocess

DEFAULT_EXECUTABLE = "ffprobe"

def probe_streams(  # NOQA: D103, E302
    mediafile,
    streams=None,
    executable=DEFAULT_EXECUTABLE,
):
    command = [
        executable,
        "-loglevel", "fatal",
        "-print_format", "json",
        "-show_entries", "stream",
    ]
    if streams:
        command.extend(["-select_streams", streams])
    command.append(mediafile)

    completed = subprocess.run(command, stdout=subprocess.PIPE)

    metadata = completed.stdout.decode("utf-8")
    metadata = json.loads(metadata)
    return metadata["streams"]
