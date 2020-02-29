import Vue from 'vue'
import App from './App.vue'
import './quasar'
// 粒子动画
import VueParticles from 'vue-particles'
Vue.use(VueParticles);

import api from './api' // 导入api接口
Vue.prototype.$api = api; // 将api挂载到vue的原型上复制代码

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
