import Vue from 'vue'
import App from './App.vue'
import store from './store'

import vuetify from './plugins/vuetify';
import UIkit from 'uikit'
 import UIkitIcons from 'uikit/dist/js/uikit-icons';
 import axios from 'axios';
 import { CSRF_TOKEN } from "./common/csrf_token"
 import VueCropper from 'vue-cropperjs';
import 'cropperjs/dist/cropper.css';
import router from './router';

Vue.component(VueCropper);
UIkit.use(UIkitIcons);
Vue.use(UIkitIcons)
Vue.config.productionTip = false

Vue.use(require('vue-moment'));
Vue.prototype.$http = axios
Vue.prototype.$http.defaults.headers.common['X-CSRFTOKEN'] = CSRF_TOKEN;
window.axios = axios

window.axios.defaults.headers.common['X-CSRFTOKEN'] = CSRF_TOKEN;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
