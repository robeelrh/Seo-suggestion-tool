<?php
namespace App\Http\Controllers;

use App\Models\Scraper;
use App\Models\SeoTestAssetsCaching;
use App\Models\SeoTestCanonicalUrl;
use App\Models\SeoTestContent;
use App\Models\SeoTestContentEncoding;
use App\Models\SeoTestDocType;
use App\Models\SeoTestFavicon;
use App\Models\SeoTestHeaderTag;
use App\Models\SeoTestHttpLinks;
use App\Models\SeoTestIframesCount;
use App\Models\SeoTestImgTagsSizeDim;
use App\Models\SeoTestKeywordOptimization;
use App\Models\SeoTestMetaDescription;
use App\Models\SeoTestMetaEncoding;
use App\Models\SeoTestMetaTag;
use App\Models\SeoTestOpenGraphProtocols;
use App\Models\SeoTestResourcesCompression;
use App\Models\SeoTestSitemapIndexing;
use App\Models\SeoTestSitemapSizeLink;
use App\Models\SeoTestTitleTag;
use App\Models\SeoTestUrlFormat;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class DashboardScraperPerformanceController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'project_id' => 'required|int',
        ]);
        $projectId = $request->input('project_id');
        $scrapers = Scraper::where('project_id', $projectId)->orderBy('id')->get();
        $scraperPerformanceResults = [];
        foreach ($scrapers as $scraper) {
            $tests = [
                'assets_caching' => SeoTestAssetsCaching::where('scraper_id', $scraper->id)->get(),
                'canonical_url' => SeoTestCanonicalUrl::where('scraper_id', $scraper->id)->get(),
                'content' => SeoTestContent::where('scraper_id', $scraper->id)->get(),
                'content_encoding' => SeoTestContentEncoding::where('scraper_id', $scraper->id)->get(),
                'doc_type' => SeoTestDocType::where('scraper_id', $scraper->id)->get(),
                'favicon' => SeoTestFavicon::where('scraper_id', $scraper->id)->get(),
                'header_tag' => SeoTestHeaderTag::where('scraper_id', $scraper->id)->get(),
                'http_links' => SeoTestHttpLinks::where('scraper_id', $scraper->id)->get(),
                'iframes_count' => SeoTestIframesCount::where('scraper_id', $scraper->id)->get(),
                'img_tags_size_dim' => SeoTestImgTagsSizeDim::where('scraper_id', $scraper->id)->get(),
                'keyword_optimization' => SeoTestKeywordOptimization::where('scraper_id', $scraper->id)->get(),
                'meta_description' => SeoTestMetaDescription::where('scraper_id', $scraper->id)->get(),
                'meta_encoding' => SeoTestMetaEncoding::where('scraper_id', $scraper->id)->get(),
                'meta_tag' => SeoTestMetaTag::where('scraper_id', $scraper->id)->get(),
                'open_graph_protocols' => SeoTestOpenGraphProtocols::where('scraper_id', $scraper->id)->get(),
                'resources_compression' => SeoTestResourcesCompression::where('scraper_id', $scraper->id)->get(),
                'sitemap_indexing' => SeoTestSitemapIndexing::where('scraper_id', $scraper->id)->get(),
                'sitemap_size_link' => SeoTestSitemapSizeLink::where('scraper_id', $scraper->id)->get(),
                'title_tag' => SeoTestTitleTag::where('scraper_id', $scraper->id)->get(),
                'url_format' => SeoTestUrlFormat::where('scraper_id', $scraper->id)->get(),
            ];
            $totalWeight = 0;
            $totalTests = 0;
            foreach ($tests as $test) {
                foreach ($test as $instance) {
                    $totalWeight += $instance->weight;
                    $totalTests++;
                }
            }
            $percentageWeight = 0;
            if ($totalTests != 0) {
                $percentageWeight = $totalWeight / ($totalTests * 3);
                $percentageWeight *= 100;
            }
            // adding the results in the scraperPerformanceResults
            $scraperPerformanceResults[] = [
                'scraper_id' => $scraper->id,
                'total_weight' => $totalWeight,
                'percentage_weight' => $percentageWeight,
                'started_at' => $scraper->started_at,
            ];
        }
        return response()->json([
            'scraperPerformanceResults' => $scraperPerformanceResults,
        ]);
    }
}