<template>
  <div class="overflow-x-auto w-full">
    <div class="bg-white rounded-lg">
      <SearchBar title="Pages Status Code Percentage" v-model="searchQuery" />
    </div>
    <div>
      <table class="min-w-full bg-white">
        <thead class="sticky top-0 z-10 bg-white border-r-2 border-l-2">
          <tr>
            <th
              class="py-2 px-6 bg-gray-50 text-left font-bold uppercase text-sm text-gray-500"
            >
              ID
            </th>
            <th
              class="py-2 px-6 bg-gray-50 text-left font-bold uppercase text-sm text-gray-500"
            >
              URL
            </th>
            <th class="py-2 px-6 bg-gray-50 font-bold text-sm text-gray-500">
              Status
            </th>
            <th class="py-2 px-6 bg-gray-50 font-bold text-sm text-gray-500">
              Indexed
            </th>
            <th class="py-2 px-6 bg-gray-50 font-bold text-sm text-gray-500">
              Action
            </th>
          </tr>
        </thead>
        <tbody class="border">
          <tr
            v-for="(row, index) in filteredRows"
            :key="index"
            class="hover:bg-grey-lighter"
          >
            <td class="py-6 px-6 text-gray-600">{{ row.id }}</td>
            <td
              class="py-6 px-6 text-gray-600 max-w-sm whitespace-normal break-words"
            >
              {{ row.scraped_url }}
            </td>
            <td class="py-6 px-6 text-gray-600 text-center">
              {{ row.status_code }}
            </td>
            <td class="py-6 px-6 text-gray-600 text-center">
              <span
                :class="{
                  'bg-green-50 text-green-400': row.indexed,
                  'bg-yellow-50 text-yellow-400': !row.indexed,
                }"
                class="py-3 px-3 rounded-lg"
              >
                {{ row.indexed ? "Indexable" : "Not Indexable" }}
              </span>
            </td>
            <td class="flex flex-row py-6 justify-center">
              <span
                @click="redirect(row.url)"
                class="text-red-500 bg-red-100 hover:bg-white rounded-lg cursor-pointer px-2 py-2 mx-2"
              >
                <img
                  src="/icons/attachment-icon.svg"
                  alt="attachment-icon Icon"
                />
              </span>
              <span
                @click="copyLink(row.url)"
                class="text-red-500 bg-red-100 hover:bg-white rounded-lg cursor-pointer px-2 py-2 mx-2"
              >
                <img src="/icons/refresh-icon.svg" alt="refresh-icon Icon" />
              </span>
              <span>
                <button
                  @click="analyze(row)"
                  class="border border-red-500 text-red-500 hover:bg-red-500 hover:text-white text-sm px-3 py-2 rounded-lg mx-2"
                >
                  Analyze
                </button>
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import apiService from "@/api/service";
import SearchBar from "@/components/SearchBar.vue";
import { useScrapersStore } from "@/store/scrapersStore";

export default {
  name: "DataTable",
  components: {
    SearchBar,
  },
  data() {
    return {
      rows: [],
      searchQuery: "",
    };
  },
  computed: {
    filteredRows() {
      if (!this.searchQuery) return this.rows;
      return this.rows.filter((row) =>
        row.scraped_url.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      const store = useScrapersStore();
      const scraperId = store.scraperId;

      apiService
        .post("/scrapers/urls/get_by_session", {
          scraper_id: scraperId,
        })
        .then((response) => {
          this.rows = response.data.map((item) => ({
            id: item.id,
            scraped_url: item.scraped_url,
            status_code: item.status_code,
            indexed: item.indexed,
          }));
        })
        .catch((error) => {
          console.error("There was an error fetching the data", error);
        });
    },
    analyze(row) {
      const store = useScrapersStore();
      store.setScrapedUrlId(row.id);

      const params = {
        status: row.status_code,
        indexable: row.indexed,
      };
      this.$router.push({ name: "urlDetails", params: params });
    },
  },
};
</script>
