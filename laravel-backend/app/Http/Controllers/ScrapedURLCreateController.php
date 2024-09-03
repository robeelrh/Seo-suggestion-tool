<?php

namespace App\Http\Controllers;

use App\Models\ScrapedUrls;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class ScrapedURLCreateController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraper_id' => 'required',
            'urls' => 'required'
        ]);

        $urls = $request->get('urls');
        $ids = []; // Array to store the IDs

        foreach ($urls as $urlData) {
            $scraperUrl = new ScrapedUrls;
            $scraperUrl->scraper_id = $request->get('scraper_id');
            $scraperUrl->scraper_timestamp = $request->get('scraper_timestamp');
            $scraperUrl->scraped_url = $urlData['url'];
            $scraperUrl->status_code = $urlData['status_code'];
            $scraperUrl->out_going = $urlData['out_going'];
            $scraperUrl->redirected_URL = $urlData['redirected_URL'];
            $scraperUrl->indexed = $urlData['indexed'];
            $scraperUrl->save();

            $resgistered_scrapers[] = $scraperUrl;
        }

        return response()->json(['resgistered_scrapers' => $resgistered_scrapers], 201);
    }

}
