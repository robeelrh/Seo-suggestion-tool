<?php

namespace App\Http\Controllers;

use App\Models\ScrapedNetworkContent;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class ScrapedURLNetworkController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
            'network_array' => 'required'
        ]);

        $urls = $request->get('network_array');


        foreach ($urls as $urlData) {
            $scraperUrl = new ScrapedNetworkContent;
            $scraperUrl->scraper_id = $request->get('scraped_url_id');
            $scraperUrl->scraped_url = $urlData['url'];
            $scraperUrl->status_code = $urlData['status_code'];
            $scraperUrl->out_going = $urlData['time'];
            $scraperUrl->save();
        }

        return response()->json($scraperUrl, 201);
    }

}
