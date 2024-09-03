<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use App\Models\ScrapedUrlsZipFile;
use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use DB;
class ScrapedURLDataGetController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
        ]);
        $tables = [
            'seo_test_assets_caching',
            'seo_test_canonical_urls',
            'seo_test_check_content',
            'seo_test_content_encodings',
            'seo_test_doc_type',
            'seo_test_favicons',
            'seo_test_header_tags',
            'seo_test_http_links',
            'seo_test_iframes_counts',
            'seo_test_img_tags_size_dims',
            'seo_test_keyword_optimizations',
            'seo_test_meta_descriptions',
            'seo_test_meta_encodings',
            'seo_test_meta_tags',
            'seo_test_noindex_in_sitemap',
            'seo_test_open_graph_protocols',
            // 'seo_test_outgoing_links',
            'seo_test_resources_compressions',
            'seo_test_sitemap_size_and_links',
            'seo_test_title_tags',
            'seo_test_url_formats'
        ];
        $result = [];
        foreach ($tables as $tableName) {
            // Check if the table exists
            if (Schema::hasTable($tableName)) {
                // Use the dynamic table name in the query
                $data = \DB::table($tableName)
                    ->where('scraped_url_id', $request->get('scraped_url_id'))
                    ->get();
                if ($data->count() > 0) {
                    $result[$tableName] = $data;
                } else {
                    $result[$tableName] = ['message' => 'No data found for the scraped_url_id'];
                }
            } else {
                $result[$tableName] = ['message' => 'Table does not exist for the scraped_url_id'];
            }
        }
        $scrapedUrlData = ScrapedUrlsZipFile::where('scraped_url_id', $request->get('scraped_url_id'))->get();
        $result['scraped_urls_analyzed'] = $scrapedUrlData;
        return response()->json($result, 200);
    }
}