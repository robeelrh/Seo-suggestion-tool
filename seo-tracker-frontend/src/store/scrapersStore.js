import { defineStore } from "pinia";

export const useScrapersStore = defineStore("scrapers", {
  state: () => ({
    scraperId: sessionStorage.getItem("scraperId") || null,
    scrapedUrlId: sessionStorage.getItem("scrapedUrlId") || null,
    projectId: 1,
  }),
  actions: {
    setScraperId(id) {
      this.scraperId = id;
      sessionStorage.setItem("scraperId", id);
    },
    setScrapedUrlId(id) {
      this.scrapedUrlId = id;
      sessionStorage.setItem("scrapedUrlId", id);
    },
    setProjectId(id) {
      this.projectId = id;
      sessionStorage.setItem("projectId", id);
    },
  },
});
