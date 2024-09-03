<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\ScrapedURLURL;

class ScrapedURLURLCreateController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id'=>'required',
            'urls' => 'required',
        ]);

        $urls = $request->get('urls');

        foreach ($urls as $urlData) {
            $scraperUrl = new ScrapedURLURL;
            $scraperUrl->scraped_url_id = $request->get('scraped_url_id');
            $scraperUrl->url = $urlData;
            $scraperUrl->save();
        }

        return response()->json(['message' => 'Data saved'], 200);
    }
}
