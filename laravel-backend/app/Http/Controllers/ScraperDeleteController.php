<?php

namespace App\Http\Controllers;

use App\Models\Scraper;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ScraperDeleteController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraper_id' => 'required',
        ]);
        Scraper::where("scraper_id",$request->get('scraper_id'))->first()->delete();
        return response()->json(['message' => 'Scraper deleted']);
    }
}
