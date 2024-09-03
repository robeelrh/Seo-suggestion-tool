<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Scraper;
use App\Models\ScrapedUrls;

class DashboardCrawledUrlsInfoController extends Controller
{
    public function handle(Request $request){
        $this->validate($request, [
            'project_id' => 'required|int',
        ]);

        $projectId = $request->input('project_id');
        $scrapers = Scraper::where('project_id', $projectId)->get();
        $totalCount = 0; 

        foreach($scrapers as $scraper){
            $scraperId = $scraper->id;
            $totalCount += ScrapedUrls::where('scraper_id', $scraperId)->count();
        }
        
        return response()->json([
            'crawled_urls' => $totalCount,
        ]);
    }
}
