<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Scraper;
use App\Models\ScrapedUrls;

class ScraperPageStatusCodeStatusController extends Controller
{
    public function handle(Request $request){
        $this->validate($request, [
            'scraper_id' => 'required|int',
        ]);

        $scraperId = $request->input('scraper_id');
        $indexedCount = ScrapedUrls::where('scraper_id', $scraperId)->where('indexed', 1)->count();
        $nonIndexedCount = ScrapedUrls::where('scraper_id', $scraperId)->where('indexed', 0)->count();

        return response()->json([
            'indexable_url_count' => $indexedCount,
            'non_indexable_url_count' => $nonIndexedCount,

        ]);
    }
}
