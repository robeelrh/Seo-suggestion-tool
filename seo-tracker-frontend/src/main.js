import Vue from "vue";
import App from "./App.vue";
import router from "./router/router";
import { createPinia } from "pinia";
import VueCompositionAPI from "@vue/composition-api";
import VueApexCharts from "vue-apexcharts";
import "./tailwind.css";

Vue.use(VueCompositionAPI);
Vue.use(VueApexCharts);
// eslint-disable-next-line vue/multi-word-component-names
Vue.component("apexchart", VueApexCharts);

const pinia = createPinia();
Vue.use(pinia);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
