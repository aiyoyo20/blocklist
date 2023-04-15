#### 项目起源

原来的 `bypass-List.txt` 文件只有主域名，而使用代理的时候不少资源的请求是来自于子域名和很多跨域的域名下。

举个例子，在百度搜索`域名`，主链接为`http://www.baidu.com/s?wd=%E5%9F%9F%E5%90%8D`，通过在控制台导出`.har`文件再从里面过滤出链接再提取域名去重排序。选取了涉及到的有明显关联的域名，其他的还有很多，就不给出了。

涉及到的子域名：
```
28608.recommend_list.baidu.com
activity.baidu.com
ada.baidu.com
api.open.baidu.com
b2b.baidu.com
baozhang.baidu.com
bdimg.share.baidu.com
bjyz-mco-searchbox201609-m12xi3-044.bjyz.baidu.com
boxer.baidu.com
bzclk.baidu.com
cache.baidu.com
chat.baidu.com
click.hm.baidu.com
clientmap.baidu.com
dlswbr.baidu.com
dss0.baidu.com
dss1.baidu.com
e.baidu.com
e.baidu.com?refer=889
eclick.baidu.com
ext.baidu.com
f3.baidu.com
fclick.baidu.com
fj-chat.baidu.com
gips0.baidu.com
gips1.baidu.com
gips3.baidu.com
gt1.baidu.com
gt2.baidu.com
hba-chat.baidu.com
hbe-chat.baidu.com
hectorstatic.baidu.com
help.baidu.com
hku.baidu.com
hm.baidu.com
hna-chat.baidu.com
hnb-chat.baidu.com
hpd.baidu.com
hs.baidu.com
i.baidu.com
image.baidu.com
isphijack.baidu.com
iwenjuan.baidu.com
j.br.baidu.com
jiankang.baidu.com
jubao.baidu.com
koubei.baidu.com
map.baidu.com
m.baidu.com
mbd.baidu.com
news.baidu.com
nj-chat.baidu.com
njjs-chat.baidu.com
nourl.ubs.baidu.com
nsclick.baidu.com
open.baidu.com
opendata.baidu.com
passport.baidu.com
passport.qatest.baidu.com
photo.baidu.com
sclick.baidu.com
sensearch.baidu.com
sestat.baidu.com
shadu.baidu.com
snsyun.baidu.com
sp0.baidu.com
sp1.baidu.com
sp2.baidu.com
sp3.baidu.com
sptidchk.baidu.com
sptidcjp.baidu.com
sptidcsfo.baidu.com
sptidcsin.baidu.com
srf.baidu.com
ss0.baidu.com
ss1.baidu.com
ss2.baidu.com
ss3.baidu.com
s.share.baidu.com
suggestion.baidu.com
t10.baidu.com
t11.baidu.com
t12.baidu.com
t14.baidu.com
t1.baidu.com
t2.baidu.com
t3.baidu.com
t7.baidu.com
t8.baidu.com
t9.baidu.com
tag.baidu.com
talent.baidu.com
tb.himg.baidu.com
tieba.baidu.com
top.baidu.com
ufo.baidu.com
ug.baidu.com
ulinkmvideo.baidu.com
v.baidu.com
velocity.baidu.com
voice.baidu.com
vse.baidu.com
vv.baidu.com
wakeup.baidu.com
wappass.baidu.com
wappass.qatest.baidu.com
wenku.baidu.com
www.baidu.com
xueshu.baidu.com
zhidao.baidu.com
b1.bdstatic.com
b2.bdstatic.com
b.bdstatic.com
bdimg.share.baidu.com
dss0.bdstatic.com
dss1.bdstatic.com
dss2.bdstatic.com
dss3.bdstatic.com
ecmb.bdimg.com
mbd.baidu.com
mbdp02.bdstatic.com
pss.bdstatic.com
ss.bdimg.com
```

多的太明显，所以将其一个文件改为这个小项目。


#### 文件说明
`bypass-List-detail.txt`，较为简单的存储格式，带`#`后为请求的域名，后续行紧跟请求涉及到的域名，空格区分不同域名块内容。

`cnDomain.txt`，`cn`后缀的域名应该都不用代理吧，独立存放。

`total.txt`，`bypass-List-detail.txt`的内容有很多重复的，这个文件是过滤的，可直接复制到`SwitchyOmega Proxy`的`bypass List` 列表中。

`txt2json.py`，将`bypass-List-detail.txt`的内容转为字典后并添加`cnDomain.txt`的内容，后续可能转到数据库上并部署到线上，查询、删除、更新、增加。

#### 使用的一些 `shell`命令

1. 从`.har`文件提取域名

`cat file.har | grep -o 'http[s]*://[a-zA-Z0-9./?=_-]*' | sort | uniq | tr "/" " " | cut -d " " -f 3 | sort | uniq`

2. `bypass-List-detail.txt`过滤掉空行和带`#`行输出到`total.txt`

`cat bypass-List-detail.txt| grep -v "#" | grep -v '^$' >> total.txt`

3. `cnDomain.txt` 的内容添加到`total.txt`

`cat cnDomain.txt >> total.txt`

4. 过滤`total.txt`重复内容

`cat total.txt | sort | uniq > tmp && mv tmp total.txt`