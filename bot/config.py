#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", 3509841)
    API_HASH = config("API_HASH", "68a5f01af74e8ef888458fdaea3376eb")
    BOT_TOKEN = config("BOT_TOKEN", "1906774383:AAFhkO9WuJseS4921bcvTwx3bxskqJTGbV8")
    DEV = 1477711713
    OWNER = config("OWNER", 1477711713)
    FFMPEG = config(
        "FFMPEG", default="ffmpeg -i '''{}'''  -filter_complex "drawtext=fontfile=njnaruto.ttf:fontsize=35:fontcolor=white:bordercolor=black@0.50:x=30:y=30:text='Animes-Encoded':enable='between(t,0,10)':alpha='if(lt(t,9)\,1\,if(lt(t\,10)\,(1-(t-9))/1\,0))', drawtext=fontfile=njnaruto.ttf:text='\|\| Download From The Original Place https\://t.me/Animes_Encoded \|\| And For Animes Request https\://t.me/Anime_Hub_Group':bordercolor=black@0.50:borderw=5:fontcolor=white:fontsize=33:x=w-((2*w-200)*(t-615)/60):y=lh+0.5:enable='between(t, 615,680)':alpha='if(lt(t,679)\,1\,if(lt(t\,680)\,(1-(t-679))/1\,0))'[out1]" -metadata:s:a:0 title="[Telegram: @Animes_Encoded]" -metadata:s:a:1 title="[Telegram: @Animes_Encoded]" -metadata:s:s:0 title="[Telegram: @Animes_Encoded]~English" -metadata:s:s:1 title="[Telegram: @Animes_Encoded]~English" -map [out1] -map 0:a? -map 0:s? -map 0:t? -metadata title="Animes_Encoded - 480p" -c:v libx265 -pix_fmt yuv420p -preset medium -s 846x480 -crf 31.8 -c:a libfdk_aac -profile:a aac_he_v2  -ac 2 -vbr 2 -c:s copy  -movflags +faststart '''{}'''  -y",
    )
    THUMB = config(
        "THUMBNAIL", "https://telegra.ph/file/501ead80cfbfde5087962.jpg"
    )
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
