<?php

namespace App\Http\Controllers;

use App\Models\Project;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ProjectGetController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'project_id' => 'required',
        ]);
        $project = Project::where([
            ['id', '=', $request->get('project_id')]
        ])->get();

        if (empty($project)) {
            return response()->json([
                'errors' => [
                    'project' => 'The project does not exist',
                ]
            ], 422);
        }
        return response()->json($project);
    }
}
