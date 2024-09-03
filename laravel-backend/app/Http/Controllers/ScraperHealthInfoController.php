<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
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

class ScraperHealthInfoController extends Controller
{
    public function handle( Request $request){
        $this->validate($request, [
            'scraper_id' => 'required|int',
        ]);
        $scraperId = $request->input('scraper_id');
        
        $tests = [
            'assets_caching' => SeoTestAssetsCaching::where('scraper_id', $scraperId)->get(),
            'canonical_url' => SeoTestCanonicalUrl::where('scraper_id', $scraperId)->get(),
            'content' => SeoTestContent::where('scraper_id', $scraperId)->get(),
            'content_encoding' => SeoTestContentEncoding::where('scraper_id', $scraperId)->get(),
            'doc_type' => SeoTestDocType::where('scraper_id', $scraperId)->get(),
            'favicon' => SeoTestFavicon::where('scraper_id', $scraperId)->get(),
            'header_tag' => SeoTestHeaderTag::where('scraper_id', $scraperId)->get(),
            'http_links' => SeoTestHttpLinks::where('scraper_id', $scraperId)->get(),
            'iframes_count' => SeoTestIframesCount::where('scraper_id', $scraperId)->get(),
            'img_tags_size_dim' => SeoTestImgTagsSizeDim::where('scraper_id', $scraperId)->get(),
            'keyword_optimization' => SeoTestKeywordOptimization::where('scraper_id', $scraperId)->get(),
            'meta_description' => SeoTestMetaDescription::where('scraper_id', $scraperId)->get(),
            'meta_encoding' => SeoTestMetaEncoding::where('scraper_id', $scraperId)->get(),
            'meta_tag' => SeoTestMetaTag::where('scraper_id', $scraperId)->get(),
            'open_graph_protocols' => SeoTestOpenGraphProtocols::where('scraper_id', $scraperId)->get(),
            'resources_compression' => SeoTestResourcesCompression::where('scraper_id', $scraperId)->get(),
            'sitemap_indexing' => SeoTestSitemapIndexing::where('scraper_id', $scraperId)->get(),
            'sitemap_size_link' => SeoTestSitemapSizeLink::where('scraper_id', $scraperId)->get(),
            'title_tag' => SeoTestTitleTag::where('scraper_id', $scraperId)->get(),
            'url_format' => SeoTestUrlFormat::where('scraper_id', $scraperId)->get(),
        ];
        $totalWeight = 0;
        $totalTests = 0;
        foreach($tests as $test){
            foreach($test as $instance){
                $totalWeight +=$instance->weight;
                $totalTests ++;
            }
        }
        $percentageWeight = 0;
        if($totalTests != 0){
            $percentageWeight = $totalWeight/ ($totalTests *3);
            $percentageWeight *=100;
        }

        return response()->json([
            'health_precentage' => $percentageWeight
        ]);
    }
}
