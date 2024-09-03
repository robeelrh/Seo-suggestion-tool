<?php

namespace App\Http\Controllers;

use App\Models\Scraper;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use App\Services\ScriptRunner;
use App\Services\Envoy;

class ScraperCreateController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'domain_url' => 'required',
            'tracing' => 'required',
            'follow_links' => 'required',
            'project_id' => 'required'
        ]);

        do {
            $randomString = 'sess_' . Str::random(6);
        } while (Scraper::where('scraper_id', $randomString)->exists());

        $scraper = new Scraper;
        $scraper->scraper_id = $randomString;
        $scraper->project_id = $request->get('project_id');
        $scraper->domain_url = $request->get('domain_url');
        $scraper->trace_able = $request->get('tracing');
        $scraper->follow_links = $request->get('follow_links');
        $scraper->sleep_time = $request->get('sleep_time');

        $scraper->status = $request->get('status');
        $scraper->started_at = $request->get('started_at');
        $scraper->ended_at = $request->get('ended_at');

        $scraper->follow_index = $request->get('follow_index');
        $scraper->follow_noindex = $request->get('follow_noindex');
        $scraper->nofollow_index = $request->get('nofollow_index');
        $scraper->nofollow_noindex = $request->get('nofollow_noindex');
        $scraper->no_meta_no_robots = $request->get('no_meta_no_robots');

        $scraper->save();

        return response()->json($scraper, 201);
    }
}
