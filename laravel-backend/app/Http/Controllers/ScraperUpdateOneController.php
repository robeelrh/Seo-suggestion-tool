<?php

namespace App\Http\Controllers;

use App\Models\Scraper;
use Illuminate\Http\Request;

class ScraperUpdateOneController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraper_id' => 'required',
        ]);

        $scraper = Scraper::where('id', $request->get('scraper_id'))->first();

        if ($request->has('status')) {
            $scraper->status = $request->status;
        }
        if ($request->has('ended_at')) {
            $scraper->ended_at = $request->ended_at;
        }
        if ($request->has('follow_index')) {
            $scraper->follow_index = $request->follow_index;
            $scraper->follow_noindex = $request->follow_noindex;
            $scraper->nofollow_index = $request->nofollow_index;
            $scraper->nofollow_noindex = $request->nofollow_noindex;
            $scraper->no_meta_no_robots = $request->no_meta_no_robots;
        }
        $scraper->save();

        return response()->json($scraper, 200);
    }
}
