
import axios from 'axios'; // 引入axios
var instance = axios.create({timeout: 1000 * 12});
instance.defaults.withCredentials = true //开启后服务器才能拿到cookie
instance.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8'//配置默认请求头
instance.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
const host = {
    first: "http://localhost:5000",//todo:set the url
    second: "http://xxxxx22222.com/api"//todo: set the url
}
export {
    host,instance
}
