<?php

namespace App\Http\Controllers;

use App\Models\ScrapedUrls;
use App\Models\ScrapedURLURL;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ScrapedURLGetFamousLinksController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
        ]);
        
        $scraped_url = ScrapedUrls::where('id', $request->scraped_url_id)->get();
        $scraped_url_url = ScrapedURLURL::where('scraped_url_id', $request->scraped_url_id)->get();

        $famousLinks = [];
        foreach ($scraped_url as $url) {
            $count = 0;
            foreach ($scraped_url_url as $urlUrl) {
                if ($urlUrl->url === $url->scraped_url) {
                    $count++;
                }
            }
            $famousLinks[$url->scraped_url] = $count;
        }

        if (empty($scraped_url)) {
            return response()->json([
                'errors' => [
                    'scraped' => 'The scraped_url_id does not exist',
                ]
            ], 422);
        }
        return response()->json($famousLinks);
    }
}

