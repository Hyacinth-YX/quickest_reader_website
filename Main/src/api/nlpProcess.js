/**
 * 与自然语言处理内容相关的接口
 * 包括思维导图json获取
 * 实体json获取（实体名:类型）
 * 自动文摘内容json
 * 实体关系（小思维导图）json
 */

import {instance,host} from '../utils/http'; // 导入http中创建的axios实例

const nlpProcess = {
    // 根据文件名返回思维导图处理完成的json， json格式参考public/mindGraphJson中的格式
    getMindGraph(filename){
        return instance.get(`${host.first}/nlpProcess/mindgraph?filename=${filename}`)
    },
    // 根据文件名返回该文件中识别出来的所有实体，用json格式，返回{'识别类型':['实体1','实体2','实体3']}
    getEntities(filename){
        return instance.get(`${host.first}/nlpProcess/ner?filename=${filename}`)
    },
    // 根据文件名返回该文件自动文摘得到的内容，可以也用json格式，返回：content：''
    getSummary(filename){
        return instance.get(`${host.first}/nlpProcess/summary?filename=${filename}`)
    },
    analyze(filename){
        return instance.get(`${host.first}/nlpProcess/analyze?filename=${filename}`)
    }
}

export default nlpProcess