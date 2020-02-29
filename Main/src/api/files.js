/**
 * files模块接口列表
 * 关于阅读文章文件上传 获取文件名列表 显示文章内容
 */

import {instance,host} from '../utils/http'; // 导入http中创建的axios实例

const files = {
    // 文章文件上传（pdf）binary （不允许重名文件）// 文件file为urf-8的txt文本
    fileUpload(filename,file){
        let uploadParam = {
            "filename":filename,
            "data":file,
        }
        console.log(uploadParam)
        return instance.post(`${host.first}/files/upload`,uploadParam)
    },
    // 获取所有上传成功了的文件名
    getFileList(){
        return instance.get(`${host.first}/files/names`)
    },
    // 根据选择文件名，返回该文件中文章的内容 param:文件名
    getFileContent(filename){
        return instance.get(`${host.first}/files/content?name=${filename}`)
    }
}

export default files