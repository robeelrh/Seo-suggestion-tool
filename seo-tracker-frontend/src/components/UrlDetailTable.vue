<template>
  <div class="overflow-x-auto w-full">
    <div class="bg-gray-50">
      <table class="min-w-full">
        <thead class="sticky top-0 z-1 bg-white">
          <tr>
            <td class="py-4 px-6 bg-gray-100 text-left text-gray-400">ID</td>
            <td class="py-4 px-6 bg-gray-100 text-left text-gray-400">Error</td>
            <td class="py-4 px-6 bg-gray-100 text-center text-gray-400">
              Status
            </td>
            <td class="py-4 px-6 bg-gray-100 text-center text-gray-400">
              Weight
            </td>
            <td class="py-4 pl-6 bg-gray-100 text-center text-gray-400">
              Priority
            </td>
            <td class="py-4 px-6 bg-gray-100 text-center text-gray-400">
              Action
            </td>
          </tr>
        </thead>
      </table>
    </div>

    <div class="overflow-y-auto mt-4 space-y-4">
      <div
        v-for="(row, index) in rows"
        :key="index"
        class="bg-white p-6 py-8 mx-auto border-b border-blue-200"
      >
        <UrlDetailsTableRow
          :originalError="String(row.originalError)"
          :index="String(index + 1)"
          :error="String(row.error)"
          :status="String(row.status)"
          :weight="String(row.status)"
          :priority="String(row.priority)"
          :action="String(row.action)"
          :suggestion="String(row.suggestion)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import apiService from "@/api/service";
import { useScrapersStore } from "@/store/scrapersStore";
import UrlDetailsTableRow from "@/components/UrlDetailTableRow.vue";

export default {
  name: "ScrapersDataTable",
  components: {
    UrlDetailsTableRow,
  },
  data() {
    return {
      rows: [],
      originalErrors: [],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      const store = useScrapersStore();
      try {
        const response = await apiService.post("/scrapers/urls/data/get", {
          scraped_url_id: parseInt(store.scrapedUrlId),
        });
        this.rows = response.data;
        this.rows = this.processResponse(this.rows);
        this.originalError = Object.keys(response.data);

        if (Array.isArray(this.rows)) {
          this.rows = this.rows.map((row, index) => {
            row.originalError = this.originalError[index];
            return row;
          });
        } else {
          console.error(
            "this.rows is not an array or is not properly defined."
          );
        }
      } catch (error) {
        console.error("There was an error fetching the data:", error);
      }
    },
    processResponse(data) {
      let processedRows = [];
      Object.entries(data).forEach(([testName, testValue]) => {
        if (Array.isArray(testValue) && testValue.length > 0) {
          const item = testValue.at(-1);
          let error = "No error";
          let status = "Not Fixed";
          let weight = item.weight || "N/A";
          const suggestion = item.suggestion;
          switch (testName) {
            case "seo_test_check_content":
              error = item.is_empty ? "No content found" : "Content found";
              status = item.is_empty ? "Not Fixed" : "Fixed";
              break;
            case "seo_test_doc_type":
            case "seo_test_favicons":
            case "seo_test_http_links":
              error = `${testName.replace(/_/g, " ")}: ${item.is_satisfied ? "Issue detected" : "No issues"}`;
              status = item.is_satisfied ? "Not Fixed" : "Fixed";
              break;
            case "seo_test_iframes_counts":
              error = `Iframes count: ${item.iframes_count}, ${item.is_satisfied ? "Issue detected" : "No issues"}`;
              status = item.is_satisfied ? "Not Fixed" : "Fixed";
              break;
            case "seo_test_meta_descriptions":
              error = `Meta description: ${item.description}, ${item.is_satisfied ? "Satisfies requirements" : "Does not satisfy requirements"}`;
              status = item.is_satisfied ? "Not Fixed" : "Fixed";
              break;
            case "seo_test_meta_encodings":
            case "seo_test_open_graph_protocols":
            case "seo_test_resources_compressions":
            case "seo_test_sitemap_size_and_links":
              error = `${testName.replace(/_/g, " ")}: ${item.is_satisfied ? "No issues" : "Issue detected"}`;
              status = item.is_satisfied ? "Not Fixed" : "Fixed";
              break;
            case "seo_test_header_tags":
              error =
                "Header tags check, H2 tags: " +
                (item.is_h2_satisfied ? "Satisfies" : "Does not satisfy");
              status = item.is_h2_satisfied ? "Fixed" : "Not Fixed";
              break;
            case "seo_test_img_tags_size_dims":
              error =
                "Image tags size and dimensions check, Alt and Size: " +
                (item.is_alt_satisfied && item.is_size_satisfied
                  ? "Satisfies"
                  : "Does not satisfy");
              status =
                item.is_alt_satisfied && item.is_size_satisfied
                  ? "Fixed"
                  : "Not Fixed";
              break;
            case "seo_test_meta_tags":
              error = `Meta tags: Description length satisfied: ${item.is_description_length_satisfied ? "Yes" : "No"}, Title length satisfied: ${item.is_title_length_satisfied ? "Yes" : "No"}`;
              status =
                item.is_description_length_satisfied &&
                item.is_title_length_satisfied
                  ? "Not Fixed"
                  : "Fixed";
              break;
            case "seo_test_noindex_in_sitemap":
              error = `${testName.replace(/_/g, " ")}: ${item.is_satisfied ? "No issues" : "Issue detected"}`;
              status = item.is_satisfied ? "Not Fixed" : "Fixed";
              break;
            case "seo_test_title_tags":
              error = `Title: ${item.title}, Length: ${item.title_len}, ${item.is_satisfied ? "Satisfies requirements" : "Does not satisfy requirements"}`;
              status = item.is_satisfied ? "Not Fixed" : "Fixed";
              break;
            default:
              error = `Unhandled test: ${testName}`;
              status = "Check manually";
          }

          processedRows.push({
            error,
            status,
            weight,
            suggestion,
            priority: "Medium", // Adjust priority as needed
            action: "See Solution",
          });
          console.log(error);
        } else {
          // Handling cases where data is not an array or empty
          processedRows.push({
            error: `${testName.replace(/_/g, " ")}: ${testValue.message || "No data"}`,
            status: "N/A",
            weight: "N/A",
            priority: "N/A",
            action: "N/A",
          });
        }
      });

      return processedRows;
    },

    getStatusClass(status) {
      switch (status) {
        case "Fixed":
          return "bg-green-50 text-green-400 py-3 px-5 rounded-lg";
        case "Not Fixed":
          return "text-red-500 bg-red-100 py-3 px-5 rounded-lg";
        default:
          return "";
      }
    },
    getPriorityClass(priority) {
      switch (priority) {
        case "Low":
          return "text-green-400";
        case "High":
          return "text-red-500";
        case "Medium":
          return "text-yellow-400";
        default:
          return "";
      }
    },
  },
};
</script>
