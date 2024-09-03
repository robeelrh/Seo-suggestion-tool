<?php

namespace App\Http\Controllers;

use App\Models\ScrapedUrlSiteMapData;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class ScrapedURLSaveSiteMap extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
            'scraped_url' => 'required',
            'site_map_content' => 'required',
        ]);

        $scraped_url_site_map = new ScrapedUrlSiteMapData;
        $scraped_url_site_map->scraped_url_id = $request->get('scraped_url_id');
        $scraped_url_site_map->scraped_url = $request->get('scraped_url');
        $scraped_url_site_map->site_map_content = $request->get('site_map_content');

        $scraped_url_site_map->save();

        return response()->json($scraped_url_site_map, 201);
    }

}
