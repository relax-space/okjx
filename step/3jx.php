<!DOCTYPE html><html><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <meta charset="UTF-8">
    <style type="text/css">
		body,
		html,
		.content {
			background-color: black;
			padding: 0;
			margin: 0;
			width: 100%;
			height: 100%;
			color: #999;
		}

		@keyframes masked-animation {
			0% {
				background-position: 0 0;
			}

			100% {
				background-position: -100%, 0;
			}
		}
    #my-loading{
        width: 100%;
        height: 100%;
        position: absolute;
        left: 0;
        top: 0;
        z-index: 99999;
        background-color:#000;
    }
    .iframeStyle{
        width: 100%;
        height: 100%;
        border: 0px;
    }
</style>
    <script src="https://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <title>不定期更换域名，请勿直接调用</title>
</head><body>
        <div id="my-loading" align="center">
			<strong><br>
				<br>
				<br>
				<br>
				<br>
				<span class="tips">
					<p style="color:white;">
						正在加载中,请稍等....
						<font class="timemsg">0</font>s
					</p>
				</span></strong> <span class="timeout" style="display:none;color:#f90;">服务器响应超时，请切换线路或刷新重试！</span>
		</div>
				<script type="text/javascript">
			function tipstime(count) {
				$('.timemsg').text(count);
				if (count == 20) {
					$('.tips').hide();
					$('.timeout').show();
				} else {
					count += 1;
					setTimeout(function() {
						tipstime(count);
					}, 1000);
				}
			}
			tipstime(0);

				//dp.notice('11', 2000, 0.8); 提示文本
				

		</script>
            <iframe src="m3.php?url=https://v.qq.com/x/cover/mzc00200tgro986.html" allowfullscreen="true" class="iframeStyle" id="myiframe" ></iframe>
     </body>
</html>
