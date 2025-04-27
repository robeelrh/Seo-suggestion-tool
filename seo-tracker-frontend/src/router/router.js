import Vue from "vue";
import Router from "vue-router";
import DashBoard from "@/Views/DashBoard.vue";
import ScraperDetailsPage from "@/Views/ScraperDetailsPage.vue";
import UrlDetailsPage from "@/Views/UrlDetailsPage.vue";
import ScraperComparePage from "@/Views/ScraperComparePage.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: DashBoard,
    },
    {
      path: "/scraperdetails",
      name: "scraperDetails",
      component: ScraperDetailsPage,
      props: true,
    },
    {
      path: "/urldetails",
      name: "urlDetails",
      component: UrlDetailsPage,
    },
    {
      path: "/scraperCompare",
      name: "scraperCompare",
      component: ScraperComparePage,
    },
  ],
});
