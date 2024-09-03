<?php

namespace App\Http\Controllers;

use App\Models\Project;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use App\Services\ScriptRunner;
use App\Services\Envoy;

class ProjectCreateController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'url' => 'required',
            'crawling_frequency' => 'required',
            'max_pages_to_crawl' => 'required',
            'crawler_speed' => 'required',
        ]);

        $project = new Project;
        $project->url = $request->get('url');
        $project->crawling_frequency = $request->get('crawling_frequency');
        $project->max_pages_to_crawl = $request->get('max_pages_to_crawl');
        $project->crawler_speed = $request->get('crawler_speed');

        $project->save();

        return response()->json($project, 201);
    }
}
