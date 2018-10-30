<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			div
			{
				width: 400px;
				height: 300px;
				border: 1px solid black;
				margin: auto;
				position: relative;
				overflow: hidden;
			}
			ul
			{
				margin: 0;
				padding: 0;
				list-style: none;
				width: 1600px;
				height: 100%;
				position: relative;
			}
			ul li
			{
				width: 400px;
				height: 300px;
				float: left;
				text-align: center;
				line-height: 300px;
				font-size: 100px;
			}
			span
			{
				position: absolute;
				background: yellowgreen;
				margin-top: -10.5px;
			}
			span:nth-of-type(1)
			{
				left: 0;
				top: 50%;
			}
			span:nth-of-type(2)
			{
				right: 0;
				top: 50%;
			}
			ol
			{
				padding: 0;
				margin: 0;
				list-style: none;
				position: absolute;
				right: 10px;
				bottom: 10px;
			}
			ol li
			{
				width: 10px;
				height: 10px;
				border-radius: 50%;
				border: 2px solid white;
				float: left;
				margin-left: 5px;
			}
			.active
			{
				background: white;
			}
		</style>
		<script src="js/jquery-1.12.3.js" type="text/javascript" charset="utf-8"></script>
	</head>
	<body>
		<div>
			<ul>
				<li style="background: red;">1</li>
				<li style="background: orange;">2</li>
				<li style="background: cyan;">3</li>
				<li style="background: yellow;">4</li>
			</ul>

			<span>上一页</span>
			<span>下一页</span>

			<ol>
				<li class="active"></li>
				<li></li>
				<li></li>
				<li></li>
			</ol>
		</div>

		<script type="text/javascript">
			//复制第一个ul li,加到最ul li末尾
			var $newLi = $("ul li").first().clone()
			$("ul").append($newLi)

			//获取一个ul li的宽度
			var liWidth = $newLi.width()

			//修改整个ul的宽度
			$("ul").width(  liWidth*$("ul li").length  )

			var  count = 0

			//定时器
			var timer =  setInterval(function(){
				count++
				move()
			},1000)

			//鼠标放到div之上时,就要立刻停掉定时器
			$("div").mouseenter(function(){
				clearInterval(timer)
			})
			//离开div,定时器要继续
			$("div").mouseleave(function(){
				//这个timer要是全局变量,否则上面的函数是无法停掉的
				timer =  setInterval(function(){
					count++
					move()
				},1000)
			})

			function move()
			{
				//没有动画
				//$("ul").css("left",-(count*liWidth)+"px")

				if (count<0)
				{
					//不使用动画,将ul移动到最后一张图,即最后一张1的位置
					$("ul").css("left",-liWidth*($("ul li").length-1)+"px")
					//再从最后这个1移动到前面的4
					//从倒数第1张,移到倒数第2张
					count = $("ul li").length-2
				}


				//到达最后一个
				if (count>= $("ul li").length)
				{
					$("ul").css("left","0")  //不使用动画归零
					count = 1                //归零后的下一张,还是第二张图,但是1*liWidth整个偏移量就是第二张图
				}

				//动画中不用带像素
				$("ul").animate({left:-count*liWidth})


				if (count == $("ul li").length-1)
				{
					//当滚动到最后一张图时,让第0个li元素高亮
					$("ol li")
					.eq( 0 ).addClass("active")
					.siblings().removeClass("active")
				}else
				{
					//正常切
					//小圆点的高亮效果和滚动的图片自动对应
					//ul的li  和ol 的li    下标是对应的
					$("ol li")
					.eq( count ).addClass("active")
					.siblings().removeClass("active")
				}

			}


			//上一页下一页
			$("span").eq(0).click(function(){
				count--
				move()
			})

			$("span").eq(1).click(function(){
				count++
				move()
			})

			//鼠标放到ol li上面,也能自动切图.
			//如果从第4个,直接移到第一个,会出现多张图片滚动效果,所以这里不加动画
			$("ol li").mouseenter(function(){
				//高亮
				$(this).addClass("active").siblings().removeClass("active")

				//切图
				$("ul").css("left",-(  $(this).index()*liWidth )+"px")

				//使用动画不好看
				//$("ul").animate({left:-$(this).index()*liWidth})
			})

		</script>
	</body>
</html>
