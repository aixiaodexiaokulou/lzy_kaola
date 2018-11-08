let dialogObj = {
  dialogTit: '提示',
  dialogContentTxt: '确定移入我的收藏？',
  dialogDesTxt: '商品买不起，将不在购物车显示',
  btnConfirm: '确定哈哈哈',
  btnCancle : '呵呵取消',
 }
 // $('#btnConfirm').html(dialogObj.btnConfirm);
const dialog1 = $('<div class="dialog-Component" id="dialogComponent">'+
'<div class="dialog-container abcenter">'+
         '<div class="dialog-tit">'+
          '<div class="tit" id="dialogTit">提示</div>'+
          '<div class="btn-cls" title="关闭弹窗口"></div>'+
      '  </div>'+
      '  <div class="dialog-content">'+
      '    <div class="content-txt">'+
      '      <div class="content-tit">'+
      '        <i class="notice-icon" id="dialogContentIcon">!</i>'+
      '        <h2 class="notice-txt" id="dialogContentTxt">确定移入我的收藏？</h2>'+
      '      </div>'+
      '      <div class="content" id="dialogDesTxt">'+
      '        商品移入我的收藏后，将不在购物车显示'+
      '      </div>'+
      '    </div>'+
          '<div class="content-button">'+
            '<button type="button" name="button" class="btn-confirm" id="btnConfirm">确定</button>'+
            '<button type="button" name="button" class="btn-cancle btn-cls" id="btnCancle">取消</button>'+
          '</div>'+
        '</div>'+
    '</div>'+
    '<div class="body-mask"></div>'+
  '</div>');
  // console.log(dialog1);
$('body').append(dialog1);
for(let i in dialogObj){
  $("#"+i).html(dialogObj[i]);
}

$('#btnShow').click(function(){
  $('#dialogComponent').fadeToggle('400', function() {
  });
})

$('.btn-cls').click(function() {
  $('#dialogComponent').fadeToggle('400', function() {
  });
});
