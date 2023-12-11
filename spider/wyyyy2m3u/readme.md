[Exporter.exe][1]（需要本机安装网易云音乐客户端）:默认位置的wyyyy(大概指歌的储存) 歌单to m3u，但是这个m3u里面充斥着只能用网易云客户端播放的格式(*.ncm)

[ncmdump-windows-386.exe][2]:解码*.ncm(网易云音乐的ncm格式)->(flac/mp3)(直接将ncm拖过来使用)

导出的m3u需要将格式转换为UTF8-BOM（可使用notepad++）后，导入[music center][3]后导入耳放使用

1.py : 一个脚本，完成将Exporter.exe导出的m3u中的所有ncm自动使用上述工具解码然后生成新的m3u，使用格式为 `python 1.py old.m3u [new.m3u]`

主要流程：直接双击Exporter.exe 导出想要的歌单，然后打开当前位置命令行（可直接在当前资源管理器地址栏输入cmd），在其中使用脚本解码后，导出新的m3u使用

[1]:https://github.com/xyqyear/create_m3u_from_NeteaseCloudMusic
[2]:https://github.com/yoki123/ncmdump
[3]: https://musiccenter.sony.net/
[4]:https://www.python.org/downloads/

