import Vue from 'vue'
import App from './App.vue'
import './quasar'
import $ from 'jquery'
Vue.use($);

import TreeChart from "vue-tree-chart";
Vue.use(TreeChart);
import VueParticles from 'vue-particles'
Vue.use(VueParticles);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
