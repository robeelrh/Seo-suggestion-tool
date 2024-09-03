<?php

namespace App\Http\Controllers;

use App\Models\Scraper;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ScraperUpdateController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraper_id' => 'required',
        ]);
        $scraper = Scraper::where('scraper_id',$request->get('scraper_id'))->first();
        $scraper->domain_url =$request->get('domain_url');
        $scraper->update();
        return response()->json($scraper);
    }
}
