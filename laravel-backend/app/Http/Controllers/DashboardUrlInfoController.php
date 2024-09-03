<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Scraper;
use App\Models\ScrapedUrls;

class DashboardUrlInfoController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraper_id' => 'required|int',
        ]);

        $scraperId = $request->input('scraper_id');
        $totalCount = ScrapedUrls::where('scraper_id', $scraperId)->count();
        $outgoingCount = ScrapedUrls::where('scraper_id', $scraperId)->where('out_going', 1)->count();
        $ingoingCount = ScrapedUrls::where('scraper_id', $scraperId)->where('out_going', 0)->count();
        $indexedCount = ScrapedUrls::where('scraper_id', $scraperId)->where('indexed', 1)->count();
        $nonIndexedCount = ScrapedUrls::where('scraper_id', $scraperId)->where('indexed', 0)->count();


        return response()->json([
            'scraped_urls' => $scrapedUrls,
            'total_url_count' => $totalCount,
            'outgoing_url_count' => $outgoingCount,
            'ingoing_url_count' => $ingoingCount,
            'indexed_url_count' => $indexedCount,
            'non_indexed_url_count' => $nonIndexedCount,

        ]);
    }
}
