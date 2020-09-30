// 实现复制到剪贴板功能函数
function copy(id){

  // 获取输入框元素
  let input = document.getElementById(id)

  // 选中元素中的文本（必须可编辑）
  input.select()

  // 检测复制命令返回值（是否可用）
  if(document.execCommand('copy')){
    document.execCommand('copy')//执行复制到剪贴板
    window.alert('已复制！')//反馈信息
  }
  
  // 无法复制（不可用）
  else{
    window.alert('复制失败！')//反馈信息
  }
}

function getYesterday() {
    return document.getElementById('startDate').valueAsDate=new Date()
}