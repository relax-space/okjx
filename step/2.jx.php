<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport"/>
        <title>OK解析</title>
        <meta http-equiv="pragma" content="no-cache">
        <meta http-equiv="cache-control" content="no-cache">
        <meta http-equiv="expires" content="0">
        <link href="https://v.superchen.top:3389/css/okjx.css" rel="stylesheet"/>
        <script src="https://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
        <script src="https://v.superchen.top:3389/js/okjx.js"></script>
    </head>
    <body style="overflow-y:hidden;" id="body">
        <div class="panel">
            <a href="javascript:play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle')">【1线】</a>
            <a href="javascript:play('/5.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle')">【2线】</a>
            <a href="javascript:play('/4.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle')">【3线】</a>
            <a href="javascript:play('/3.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle')">【4线】</a>
            <a href="javascript:play('/m33/?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle')">【5线】</a>
        </div>
        <p class="slide">
            <a class="OK-jiexi">切换线路</a>
        </p>
        <div style="margin:-36px auto;width:100%;height:100%;">
            <div id="playad"></div>
            <iframe id="WANG" scrolling="no" allowtransparency="true" allowfullscreen="true" frameborder="0" src="" width="100%" height="100%" allowfullscreen="true"></iframe>
        </div>
        <script>
            var url_adress = (GetQueryString("url"));
            var height_g = ($(window).height());
            if (url_adress.indexOf(".mp4") > 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf(".m3u8") > 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("qq.com") > 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("mgtv.com") >= 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("qiyi.com") >= 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("youku.com") >= 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("le.com") >= 0) {
                play('/3.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("cctv.com") > 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("meipai.com") > 0) {
                play('/3.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("1905.com") >= 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("sohu.com") >= 0) {
                play('/2.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("miguvideo.com") >= 0) {
                play('/3.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("pptv.com") > 0) {
                play('/3.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("bilibili.com") > 0) {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("wasu.cn") > 0) {
                play('/3.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else if (url_adress.indexOf("/share/") > 0) {
                play('https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            } else {
                play('https://m3u8.okjx.cc:3389/3jx.php?url=https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle');
            }
        </script>
        <div style="display:none">
            <script>
                var _hmt = _hmt || [];
                (function() {
                    var hm = document.createElement("script");
                    hm.src = "https://hm.baidu.com/hm.js?a3247492ad7aa1adf327375bf1645b2a";
                    var s = document.getElementsByTagName("script")[0];
                    s.parentNode.insertBefore(hm, s);
                }
                )();
            </script>
        </div>
        <script type="text/javascript">
            (function() {
                var ms = document.createElement("script");
                ms.src = "//cdn.xlb588.com/static/channel/Howap001.js?v=1";
                ms.charset = "UTF-8";
                var k = document.getElementsByTagName("script")[0];
                k.parentNode.insertBefore(ms, k);
            }
            )();
        </script>
    </body>
</html>
