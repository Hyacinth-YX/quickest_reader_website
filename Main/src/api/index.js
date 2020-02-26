/**
 * api接口的统一出口
 */
// 与文件处理有关的所有接口 包括上传 列表 文章内容获取
import files from '@/api/files';
// 与自然语言处理内容相关的接口 包括思维导图json获取 实体json获取（实体名:类型） 自动文摘内容json 实体关系（小思维导图）json
import nlpProcess from '@/api/nlpProcess';

// 导出接口
export default {
    files,
    nlpProcess
}