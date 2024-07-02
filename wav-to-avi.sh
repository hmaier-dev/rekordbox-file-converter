#!/usr/bin/bash
ffmpeg -loop 1 \
    -i input.png -i audio.wav \
    -c:v mpeg4 -tune stillimage \
    -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,format=yuv420p" \
    -c:a copy -shortest out.avi
