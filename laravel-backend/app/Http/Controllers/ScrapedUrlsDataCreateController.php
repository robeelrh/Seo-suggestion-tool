<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Models\SeoTestFavicon;
use App\Models\SeoTestTitleTag;
use App\Models\SeoTestMetaDescription;
use App\Models\SeoTestHeaderTag;
use App\Models\SeoTestImgTagsSizeDim;
use App\Models\SeoTestKeywordOptimization;
use App\Models\SeoTestMetaTag;
use App\Models\SeoTestHttpLinks;
use App\Models\SeoTestDocType;
use App\Models\SeoTestIframesCount;
use App\Models\SeoTestMetaEncoding;
use App\Models\SeoTestResourcesCompression;
use App\Models\SeoTestOpenGraphProtocols;
use App\Models\SeoTestContentEncoding;
use App\Models\SeoTestCanonicalUrl;
use App\Models\SeoTestAssetsCaching;

use App\Models\SeoTestContent;
use App\Models\SeoTestSitemapIndexing;
use App\Models\SeoTestSitemapSizeLink;

class ScrapedUrlsDataCreateController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
            'scraper_id' => 'required',
            'url' => 'required',
            'data' => 'required',
        ]);

        foreach ($request->get('data') as $originalTableName => $dataItem) {

            if ($originalTableName === 'favicons') {
                $seoTestFavicon = new SeoTestFavicon();
                $seoTestFavicon->url = $request->get("url");
                $seoTestFavicon->scraper_id = $request->get('scraper_id');
                $seoTestFavicon->scraped_url_id = $request->get('scraped_url_id');

                $seoTestFavicon->link = $dataItem["link"];
                $seoTestFavicon->is_satisfied = $dataItem['is_satisfied'];
                $seoTestFavicon->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestFavicon->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestFavicon->suggestion = $dataItem['suggestion'];
                }
                
                

                $seoTestFavicon->save();
                // return response()->json(['message' =>  $seoTestFavicon], 201);
            }

            if ($originalTableName === 'title_tags') {
                $seoTestTitleTag = new SeoTestTitleTag();
                $seoTestTitleTag->url = $request->get("url");
                $seoTestTitleTag->scraper_id = $request->get('scraper_id');
                $seoTestTitleTag->scraped_url_id = $request->get('scraped_url_id');

                $seoTestTitleTag->title = $dataItem["title"];
                $seoTestTitleTag->is_satisfied = $dataItem['is_satisfied'];
                $seoTestTitleTag->weight = $dataItem['weight'];
                $seoTestTitleTag->title_len = $dataItem['title_len'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestTitleTag->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestTitleTag->suggestion = $dataItem['suggestion'];
                }

                $seoTestTitleTag->save();
                // return response()->json(['message' =>  $seoTestTitleTag], 201);
            }

            if ($originalTableName === 'meta_descriptions') {
                $seoTestMetaDescription = new SeoTestMetaDescription();
                $seoTestMetaDescription->url = $request->get("url");
                $seoTestMetaDescription->scraper_id = $request->get('scraper_id');
                $seoTestMetaDescription->scraped_url_id = $request->get('scraped_url_id');

                $seoTestMetaDescription->is_satisfied = $dataItem["is_satisfied"];
                $seoTestMetaDescription->weight = $dataItem['weight'];
                $seoTestMetaDescription->description = $dataItem['description'];
                $seoTestMetaDescription->description_length = $dataItem['description_length'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestMetaDescription->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestMetaDescription->suggestion = $dataItem['suggestion'];
                }

                $seoTestMetaDescription->save();
                // return response()->json(['message' =>  $seoTestMetaDescription], 201);
            }

            if ($originalTableName === 'header_tags') {
                $seoTestHeaderTag = new SeoTestHeaderTag();
                $seoTestHeaderTag->url = $request->get("url");
                $seoTestHeaderTag->scraper_id = $request->get('scraper_id');
                $seoTestHeaderTag->scraped_url_id = $request->get('scraped_url_id');

                $seoTestHeaderTag->is_satisfied = $dataItem["is_satisfied"];
                $seoTestHeaderTag->is_h2_satisfied = $dataItem['is_h2_satisfied'];
                $seoTestHeaderTag->weight = $dataItem['weight'];
                $seoTestHeaderTag->headers = json_encode($dataItem['headers']);
                $seoTestHeaderTag->keyword_count_outside_h1 = $dataItem['keyword_count_outside_h1'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestHeaderTag->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestHeaderTag->suggestion = $dataItem['suggestion'];
                }


                $seoTestHeaderTag->save();
                // return response()->json(['message' =>  $seoTestHeaderTag], 201);
            }

            if ($originalTableName === 'img_tags_size_dims') {
                $seoTestImgTagsSizeDim = new SeoTestImgTagsSizeDim();
                $seoTestImgTagsSizeDim->url = $request->get("url");
                $seoTestImgTagsSizeDim->scraper_id = $request->get('scraper_id');
                $seoTestImgTagsSizeDim->scraped_url_id = $request->get('scraped_url_id');

                $seoTestImgTagsSizeDim->is_alt_satisfied = $dataItem["is_alt_satisfied"];
                $seoTestImgTagsSizeDim->is_size_satisfied = $dataItem['is_size_satisfied'];
                $seoTestImgTagsSizeDim->is_dimension_satisfied = $dataItem['is_dimension_satisfied'];
                $seoTestImgTagsSizeDim->weight = $dataItem['weight'];
                $seoTestImgTagsSizeDim->missing_alt_tags = json_encode($dataItem["missing_alt_tags"]);
                $seoTestImgTagsSizeDim->with_alt_tags = json_encode($dataItem['with_alt_tags']);
                $seoTestImgTagsSizeDim->correct_size = json_encode($dataItem['correct_size']);
                $seoTestImgTagsSizeDim->large_size = json_encode($dataItem['large_size']);
                $seoTestImgTagsSizeDim->correct_dimensions = json_encode($dataItem['correct_dimensions']);
                $seoTestImgTagsSizeDim->incorrect_dimensions = json_encode($dataItem['incorrect_dimensions']);
                if (isset($dataItem['suggestion'])) {
                    $seoTestImgTagsSizeDim->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestImgTagsSizeDim->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestImgTagsSizeDim->save();
                // return response()->json(['message' =>  $seoTestImgTagsSizeDim], 201);
            }

            if ($originalTableName === 'keyword_optimizations') {
                // $seoTestKeywordOptimization = new SeoTestKeywordOptimization();
                // $seoTestKeywordOptimization->url = $request->get("url");
                // $seoTestKeywordOptimization->scraper_id = $request->get('scraper_id');
                // $seoTestKeywordOptimization->scraped_url_id = $request->get('scraped_url_id');

                // $seoTestKeywordOptimization->is_alt_satisfied = $dataItem["is_alt_satisfied"];
                // $seoTestKeywordOptimization->is_size_satisfied = $dataItem['is_size_satisfied'];
                // $seoTestKeywordOptimization->is_dimension_satisfied = $dataItem['is_dimension_satisfied'];
                // $seoTestKeywordOptimization->weight = $dataItem['weight'];
                // $seoTestKeywordOptimization->missing_alt_tags = json_encode($dataItem["missing_alt_tags"]);
                // $seoTestKeywordOptimization->with_alt_tags = json_encode($dataItem['with_alt_tags']);
                // $seoTestKeywordOptimization->correct_size = json_encode($dataItem['correct_size']);
                // $seoTestKeywordOptimization->large_size = json_encode($dataItem['large_size']);
                // $seoTestKeywordOptimization->correct_dimensions = json_encode($dataItem['correct_dimensions']);
                // $seoTestKeywordOptimization->incorrect_dimensions = json_encode($dataItem['incorrect_dimensions']);
                
                // $seoTestKeywordOptimization->save();
                // return response()->json(['message' =>  $seoTestKeywordOptimization], 201);
            }

            if ($originalTableName === 'meta_tags') {
                $seoTestMetaTag = new SeoTestMetaTag();
                $seoTestMetaTag->url = $request->get("url");
                $seoTestMetaTag->scraper_id = $request->get('scraper_id');
                $seoTestMetaTag->scraped_url_id = $request->get('scraped_url_id');

                $seoTestMetaTag->is_satisfied = $dataItem["is_satisfied"];
                $seoTestMetaTag->is_description_length_satisfied = $dataItem['is_description_length_satisfied'];
                $seoTestMetaTag->is_title_length_satisfied = $dataItem['is_title_length_satisfied'];
                $seoTestMetaTag->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestMetaTag->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestMetaTag->suggestion = $dataItem['suggestion'];
                }

                
                $seoTestMetaTag->save();
                // return response()->json(['message' =>  $seoTestMetaTag], 201);
            }

            if ($originalTableName === 'sitemap_size_and_links') {
                $seoTestSitemapSizeLink = new SeoTestSitemapSizeLink();
                $seoTestSitemapSizeLink->url = $request->get("url");
                $seoTestSitemapSizeLink->scraper_id = $request->get('scraper_id');
                $seoTestSitemapSizeLink->scraped_url_id = $request->get('scraped_url_id');

                $seoTestSitemapSizeLink->is_satisfied = $dataItem["is_satisfied"];
                $seoTestSitemapSizeLink->no_of_links = $dataItem['no_of_links'];
                $seoTestSitemapSizeLink->size = $dataItem['size'];
                $seoTestSitemapSizeLink->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestSitemapSizeLink->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestSitemapSizeLink->suggestion = $dataItem['suggestion'];
                }

                
                $seoTestSitemapSizeLink->save();
                // return response()->json(['message' =>  $seoTestSitemapSizeLink], 201);
            }

            if ($originalTableName === 'sitemap_indexing') {
                $seoTestSitemapIndexing = new SeoTestSitemapIndexing();
                $seoTestSitemapIndexing->url = $request->get("url");
                $seoTestSitemapIndexing->scraper_id = $request->get('scraper_id');
                $seoTestSitemapIndexing->scraped_url_id = $request->get('scraped_url_id');

                $seoTestSitemapIndexing->is_satisfied = $dataItem["is_satisfied"];
                $seoTestSitemapIndexing->noindex_urls = json_encode($dataItem['noindex_urls']);
                $seoTestSitemapIndexing->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestSitemapIndexing->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestSitemapIndexing->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestSitemapIndexing->save();
                // return response()->json(['message' =>  $seoTestSitemapIndexing], 201);
            }

            if ($originalTableName === 'check_page_content') {
                $seoTestContent = new SeoTestContent();
                $seoTestContent->url = $request->get("url");
                $seoTestContent->scraper_id = $request->get('scraper_id');
                $seoTestContent->scraped_url_id = $request->get('scraped_url_id');

                $seoTestContent->is_empty = $dataItem["is_empty"];
                $seoTestContent->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestContent->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestContent->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestContent->save();
                // return response()->json(['message' =>  $seoTestContent], 201);
            }

            if ($originalTableName === 'http_links') {
                $seoTestHttpLinks = new seoTestHttpLinks();
                $seoTestHttpLinks->url = $request->get("url");
                $seoTestHttpLinks->scraper_id = $request->get('scraper_id');
                $seoTestHttpLinks->scraped_url_id = $request->get('scraped_url_id');

                $seoTestHttpLinks->is_satisfied = $dataItem["is_satisfied"];
                $seoTestHttpLinks->http_links = json_encode($dataItem["http_links"]);
                $seoTestHttpLinks->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestHttpLinks->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestHttpLinks->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestHttpLinks->save();
                // return response()->json(['message' =>  $seoTestHttpLinks], 201);
            }

            if ($originalTableName === 'doc_type') {
                $seoTestDocType = new SeoTestDocType();
                $seoTestDocType->url = $request->get("url");
                $seoTestDocType->scraper_id = $request->get('scraper_id');
                $seoTestDocType->scraped_url_id = $request->get('scraped_url_id');

                $seoTestDocType->is_satisfied = $dataItem["is_satisfied"];
                $seoTestDocType->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestDocType->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestDocType->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestDocType->save();
                // return response()->json(['message' =>  $seoTestDocType], 201);
            }

            if ($originalTableName === 'iframes_count') {
                $seoTestIframesCount = new SeoTestIframesCount();
                $seoTestIframesCount->url = $request->get("url");
                $seoTestIframesCount->scraper_id = $request->get('scraper_id');
                $seoTestIframesCount->scraped_url_id = $request->get('scraped_url_id');

                $seoTestIframesCount->is_satisfied = $dataItem["is_satisfied"];
                $seoTestIframesCount->iframes_count = $dataItem["iframes_count"];
                $seoTestIframesCount->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestIframesCount->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestIframesCount->suggestion = $dataItem['suggestion'];
                }
                
                
                $seoTestIframesCount->save();
                // return response()->json(['message' =>  $seoTestIframesCount], 201);
            }

            if ($originalTableName === 'meta_encoding') {
                $seoTestMetaEncoding = new SeoTestMetaEncoding();
                $seoTestMetaEncoding->url = $request->get("url");
                $seoTestMetaEncoding->scraper_id = $request->get('scraper_id');
                $seoTestMetaEncoding->scraped_url_id = $request->get('scraped_url_id');

                $seoTestMetaEncoding->is_satisfied = $dataItem["is_satisfied"];
                $seoTestMetaEncoding->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestMetaEncoding->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestMetaEncoding->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestMetaEncoding->save();
                // return response()->json(['message' =>  $seoTestMetaEncoding], 201);
            }

            if ($originalTableName === 'resources_compression') {
                $seoTestResourcesCompression = new SeoTestResourcesCompression();
                $seoTestResourcesCompression->url = $request->get("url");
                $seoTestResourcesCompression->scraper_id = $request->get('scraper_id');
                $seoTestResourcesCompression->scraped_url_id = $request->get('scraped_url_id');

                // $seoTestResourcesCompression->is_satisfied = $dataItem["is_satisfied"];
                // $seoTestResourcesCompression->weight = $dataItem['weight'];
                // $seoTestResourcesCompression->suggestion = $dataItem['suggestion'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestResourcesCompression->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestResourcesCompression->suggestion = $dataItem['suggestion'];
                }
                $seoTestResourcesCompression->save();
                // return response()->json(['message' =>  $seoTestResourcesCompression], 201);
            }

            if ($originalTableName === 'og_meta_content') {
                $seoTestOpenGraphProtocols = new SeoTestOpenGraphProtocols();
                $seoTestOpenGraphProtocols->url = $request->get("url");
                $seoTestOpenGraphProtocols->scraper_id = $request->get('scraper_id');
                $seoTestOpenGraphProtocols->scraped_url_id = $request->get('scraped_url_id');

                $seoTestOpenGraphProtocols->is_satisfied = $dataItem["is_satisfied"];
                $seoTestOpenGraphProtocols->weight = $dataItem['weight'];

                $seoTestOpenGraphProtocols->og_image = $dataItem['og_image'];
                $seoTestOpenGraphProtocols->og_type = $dataItem['og_type'];
                $seoTestOpenGraphProtocols->og_title = $dataItem['og_title'];
                $seoTestOpenGraphProtocols->og_description = $dataItem['og_description'];
                $seoTestOpenGraphProtocols->og_locale = $dataItem['og_locale'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestOpenGraphProtocols->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestOpenGraphProtocols->suggestion = $dataItem['suggestion'];
                }
                // $seoTestOpenGraphProtocols->suggestion = $dataItem['suggestion'];

                
                $seoTestOpenGraphProtocols->save();
                // return response()->json(['message' =>  $seoTestOpenGraphProtocols], 201);
            }

            if ($originalTableName === 'content_encoding') {
                $seoTestContentEncoding = new SeoTestContentEncoding();
                $seoTestContentEncoding->url = $request->get("url");
                $seoTestContentEncoding->scraper_id = $request->get('scraper_id');
                $seoTestContentEncoding->scraped_url_id = $request->get('scraped_url_id');

                $seoTestContentEncoding->is_content_encoding = $dataItem["is_content_encoding"];
                $seoTestContentEncoding->is_satisfied = $dataItem["is_satisfied"];
                $seoTestContentEncoding->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestContentEncoding->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestContentEncoding->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestContentEncoding->save();
                // return response()->json(['message' =>  $seoTestContentEncoding], 201);
            }

            if ($originalTableName === 'canonical_url') {
                $seoTestCanonicalUrl = new SeoTestCanonicalUrl();
                $seoTestCanonicalUrl->url = $request->get("url");
                $seoTestCanonicalUrl->scraper_id = $request->get('scraper_id');
                $seoTestCanonicalUrl->scraped_url_id = $request->get('scraped_url_id');

                $seoTestCanonicalUrl->is_canonical = $dataItem["is_canonical"];
                $seoTestCanonicalUrl->is_satisfied = $dataItem["is_satisfied"];
                $seoTestCanonicalUrl->weight = $dataItem['weight'];
                $seoTestCanonicalUrl->canonical_url = $dataItem['url'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestCanonicalUrl->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestCanonicalUrl->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestCanonicalUrl->save();
                // return response()->json(['message' =>  $seoTestCanonicalUrl], 201);
            }

            if ($originalTableName === 'assets_caching') {
                $seoTestAssetsCaching = new SeoTestAssetsCaching();
                $seoTestAssetsCaching->url = $request->get("url");
                $seoTestAssetsCaching->scraper_id = $request->get('scraper_id');
                $seoTestAssetsCaching->scraped_url_id = $request->get('scraped_url_id');

                $seoTestAssetsCaching->is_satisfied = $dataItem["is_satisfied"];
                $seoTestAssetsCaching->weight = $dataItem['weight'];
                if (isset($dataItem['suggestion'])) {
                    $seoTestAssetsCaching->suggestion = $dataItem['suggestion'];
                } else {
                    $seoTestAssetsCaching->suggestion = $dataItem['suggestion'];
                }
                
                $seoTestAssetsCaching->save();
                // return response()->json(['message' =>  $seoTestAssetsCaching], 201);
            }

        }

        
        return response()->json(['message' => 'Tables and data created successfully'], 201);
    }
}

