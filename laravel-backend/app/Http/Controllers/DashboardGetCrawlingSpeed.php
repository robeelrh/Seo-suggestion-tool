<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Project;

class DashboardGetCrawlingSpeed extends Controller
{
    public function handle(Request $request){
        $this->validate($request, [
            'project_id' => 'required|int',
        ]);
        $projectId = $request->input('project_id');
        $project = Project::where('id', $projectId)->first();
        
        return response()->json([
            "crawler_speed" => $project->crawler_speed
        ]); 
    }
}
