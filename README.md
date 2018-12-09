# picbot
一个很丑的Discord图片bot 基于 Rapptz/discord.py

## 使用方法
1.安装依赖的第三方库[discord.py](https://github.com/Rapptz/discord.py)

2.在main.py的第12行token中输入bot的token，headers末尾的Cookie用来模拟登陆[yande.re](https://yande.re)，可不写（登陆后可以看到更激进的R18内容）

3.运行脚本

## 命令说明
以感叹号开头，有两种命令<br>
>1.!pic<br>
不需要加任何参数，bot随机发一张来自[yande.re](https://yande.re/)的图片<br>
<br>
>2 !tag tag1 tag2 tag3......<br>
指定tag（标签）搜索图片，搜索结果内随机选择一张发出来  
<br>
例如:<br>
   >!tag no_bra azur_lane score:>=500  
        不戴bra  碧蓝航线   分数大于等于500  
   >!tag rating:safe loli<br>
        等级为安全    萝莉<br>
   >!tag wallpaper touhou<br>
        壁纸       东方project<br>
   >!tag user:kaz source:http://site.com id:>=100 date:2007-01-01<br>
        用户kaz上传的 来自xxx网站         图片id大于等于100    日期为2007-01-01<br>
   ↑这几条很少能用到<br>
   更详细的请参考yande.re内置的[指令表](https://yande.re/help/cheatsheet)<br>

