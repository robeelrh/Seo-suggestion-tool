<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Project;

class DashboardCrawlerFrequencyInfoController extends Controller
{
    public function handle(Request $request){
        $this->validate($request, [
            'project_id' => 'required|int',
        ]);
        $projectId = $request->input('project_id');
        $project = Project::where('id', $projectId)->first();
        
        return response()->json([
            "crawling_frequency" => $project->crawling_frequency
        ]); 
    }
}
