<?php

namespace App\Http\Controllers;

use App\Models\ScrapedUrls;
use App\Models\ScrapedURLURL;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class ScrapedURLGetDepthController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
        ]);
        
        $scraped_url = ScrapedUrls::where('id', $request->scraped_url_id)->get();
        $scraped_url_url = ScrapedURLURL::where('scraped_url_id', $request->scraped_url_id)->get();

        foreach ($scraped_url as $url) {
            foreach ($scraped_url_url as $url_url) {
                if ($url_url->url === $url->scraped_url) {
                    Log::info('Link: ' .$url_url->url);
                }
            }
        }
    }
}