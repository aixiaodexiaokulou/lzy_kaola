// 此为登录页面！！
// window.onload=function(){
//   let success = $.cookie("signin");
//   if (success) {
//     let count = JSON.parse($.cookie("user"));
//     $('#userName').val(count[0].name);
//     $('#userPass').val(count[0].pass);
//     $('#remeber-signin').prop('checked',true);
//   }
//
//   let arr = $.cookie("user"),
//       registerCount=null,
//       registerPass =null,
//       currentCount =null,
//       currentPass  =null;
//   if (arr) {
//     arr = JSON.parse(arr);
//         registerCount = arr[0].name,
//         registerPass  = arr[0].pass;
//   }
//
//
//   $('.btn-signin').click(function(event) {
//   	currentCount = $('#userName').val();
// 		currentPass  = $('#userPass').val();
//     if (currentCount === registerCount && currentPass === registerPass) {
//       //成功登陆，判断是否勾选了十天免登陆
//       if ($('.free-box>input:checked')) {
//         $.cookie('signin',true,{expires:10,path:"/"});
//       }
//       location.href="http://localhost:3000/src/index.html"
//     }
//   });
// }

// 自己改的登录验证

$(function () {
    $('#subButton').on('click', function () {
        console.log('登录')

        temp1 = checkingAccount()
        temp2 = checkingPassword()
        if (temp1 && temp2) {
            $('.signBox form').submit()
        }
    })


    function checkingAccount() {
        // 数字、字母
        var reg = /^[A-Za-z0-9]+$/
        var accountInput = $('#userName')
        if (reg.test(accountInput.val())) {  // 符合
            $('.usernameBox b').hide()
            // $('#userName').removeClass('errorBorder').css('border', '1px solid rgb(15, 157, 85)')

            return true

        } else {    // 不符合
            $('.usernameBox b').show()
            // $('#userName').removeClass('errorBorder').css('border', '1px solid rgb(15, 157, 85)')
            $('.usernameBox b').css('color', 'red')

            return false
        }
    }

    function checkingPassword() {
        // 数字
        var reg = /^[\d]{6,12}$/
        var passwordInput = $('#userPass')
        if (reg.test(passwordInput.val())) {  // 符合
            $('.userpassBox b').hide()
            // $('#userPass').removeClass('errorBorder').css('border', '1px solid rgb(15, 157, 85)')
            return true
        } else {    // 不符合
            $('.userpassBox b').show()
            // $('#userPass').removeClass('errorBorder').css('border', '1px solid rgb(15, 157, 85)')
            $('.userpassBox b').css('color', 'red')

            return false
        }
    }
})