/**
 * files模块接口列表
 * 关于阅读文章文件上传 获取文件名列表 显示文章内容
 */

import base from './base'; // 导入接口域名列表
import axios from '../utils/http'; // 导入http中创建的axios实例
import qs from 'qs'; // 根据需求是否导入qs模块

const files = {
    // 文章文件上传（pdf）binary （不允许重名文件）// 文件file为urf-8的txt文本
    fileUpload(filename,file){
        return axios.post(`${base.first}/files/${filename}`,
            qs.stringify(file))
    },
    // 获取所有上传成功了的文件名 todo:数据类型用什么？可以存储信息的列表？
    getFileList(){
        return axios.get(`${base.first}/files/names`)
    },
    // 根据选择文件名，返回该文件中文章的内容 param:文件名
    getFileContent(filename){
        return axios.get(`${base.first}/files/content/${filename}`)
    }
}

export default files